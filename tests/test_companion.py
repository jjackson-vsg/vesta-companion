import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("companion",ROOT/"scripts/companion.py")
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

class CompanionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        shutil.copytree(ROOT/"templates",self.root/"templates")
        c.init(self.root)
        self.source=self.root/"personal/todo/tasks.json"

    def tearDown(self):
        self.tmp.cleanup()

    def task(self,title="A useful task"):
        return dict(id="task-1",title=title,notes="",owner="",project="",due="",priority="high",status="todo",source="Fictional test",updatedAt=c.stamp())

    def export(self,tasks):
        raw=self.source.read_bytes()
        doc=json.loads(raw)
        out=dict(format="companion-task-edit",schemaVersion=1,baseRevision=doc["revision"],baseHash=hashlib.sha256(raw).hexdigest(),tasks=tasks,exportedAt=c.stamp())
        p=self.root/"changes.json"
        p.write_bytes(c.json_bytes(out))
        return p

    def test_setup_preserves_existing_profile_and_tasks(self):
        profile=self.root/"personal/profile.md"
        profile.write_text("My existing profile")
        raw=self.source.read_bytes()
        c.init(self.root)
        self.assertEqual(profile.read_text(),"My existing profile")
        self.assertEqual(self.source.read_bytes(),raw)

    def test_successful_import_persists_and_renders(self):
        self.assertEqual(c.import_tasks(self.export([self.task()]),self.root),1)
        data=json.loads(self.source.read_bytes())
        self.assertEqual(data["tasks"][0]["title"],"A useful task")
        self.assertIn("A useful task",(self.root/"personal/todo/board.html").read_text())
        self.assertEqual(len(list((self.root/"personal/todo/history").glob("*.json"))),1)

    def test_replay_is_rejected_without_mutation(self):
        export=self.export([self.task()])
        c.import_tasks(export,self.root)
        raw=self.source.read_bytes()
        with self.assertRaisesRegex(ValueError,"Stale"):
            c.import_tasks(export,self.root)
        self.assertEqual(raw,self.source.read_bytes())

    def test_hash_detects_changes_without_revision_increment(self):
        export=self.export([self.task()])
        self.source.write_bytes(self.source.read_bytes()+b" ")
        raw=self.source.read_bytes()
        with self.assertRaisesRegex(ValueError,"Stale"):
            c.import_tasks(export,self.root)
        self.assertEqual(raw,self.source.read_bytes())

    def test_missing_tasks_cannot_be_silently_removed(self):
        c.import_tasks(self.export([self.task()]),self.root)
        raw=self.source.read_bytes()
        with self.assertRaisesRegex(ValueError,"remove tasks"):
            c.import_tasks(self.export([]),self.root)
        self.assertEqual(raw,self.source.read_bytes())

    def test_html_injection_is_escaped(self):
        task=self.task('</script><script>window.pwned=true</script>')
        c.import_tasks(self.export([task]),self.root)
        html=(self.root/"personal/todo/board.html").read_text()
        self.assertNotIn(task["title"],html)
        self.assertIn(r"\u003c/script\u003e",html)

    def test_duplicates_and_bad_dates_rejected(self):
        doc={"schemaVersion":1,"revision":0,"updatedAt":None,"tasks":[self.task(),self.task()]}
        with self.assertRaisesRegex(ValueError,"duplicate"):
            c.validate_tasks(doc)
        for bad in ["2026-02-30","2026-13-01","09-09-2026"]:
            task=self.task();task["due"]=bad;doc["tasks"]=[task]
            with self.assertRaises(ValueError):c.validate_tasks(doc)

    def test_boolean_revision_and_unknown_payload_rejected(self):
        doc={"schemaVersion":1,"revision":True,"updatedAt":None,"tasks":[]}
        with self.assertRaises(ValueError):c.validate_tasks(doc)
        doc["revision"]=0;doc["extra"]="not allowed"
        with self.assertRaises(ValueError):c.validate_tasks(doc)

    def test_concurrent_lock_refuses_write(self):
        lock=self.root/"personal/todo/.write.lock"
        lock.write_text("existing writer")
        with self.assertRaisesRegex(ValueError,"in progress"):c.import_tasks(self.export([]),self.root)
        self.assertTrue(lock.exists())

    def test_compare_before_replace(self):
        self.source.write_text("changed")
        with self.assertRaisesRegex(ValueError,"changed"):
            c.atomic_write(self.source,b"replacement",expected=b"old")
        self.assertEqual(self.source.read_text(),"changed")

    def test_path_traversal_rejected(self):
        with self.assertRaises(ValueError):c.safe_path(self.root,"../outside.txt")

    def test_malformed_export_does_not_write(self):
        export=self.root/"bad.json";export.write_text('{"format":"unknown"}')
        raw=self.source.read_bytes()
        with self.assertRaises(ValueError):c.import_tasks(export,self.root)
        self.assertEqual(raw,self.source.read_bytes())

if __name__=="__main__":
    unittest.main()
