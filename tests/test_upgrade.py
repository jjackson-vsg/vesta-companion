"""Protect authoritative personal state when adopting a fresh kit."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("upgrade_companion", ROOT / "scripts/companion.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

class UpgradeTests(unittest.TestCase):
    def test_personal_copy_retains_state_and_original_recovery_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            old, new = Path(tmp) / "old", Path(tmp) / "new"
            personal = old / "personal"
            preserved = {
                "profile.md": b"Assistant: Rowan; prefer concise answers.\n",
                "HANDOVER.md": b"Continue the fictional orchard plan.\n",
                "vault/HOME.md": b"My existing vault index\n",
                "vault/knowledge/orchard.md": b"Fictional decision: blue labels.\n",
                "vault/.obsidian/app.json": b'{"userPreference":"keep"}\n',
                "journals/old.md": b"Keep legacy journal in place.\n",
                "skills/INDEX.md": b"Read orchard-review/SKILL.md.\n",
                "skills/orchard-review/SKILL.md": b"Local fictional review workflow.\n",
                "projects/orchard.md": b"Fictional project plan.\n",
                "outputs/draft.md": b"DRAFT: fictional update.\n",
                "automations/README.md": b"No active schedules.\n",
                "todo/history/old.json": b"{}\n",
            }
            task = dict(id="orchard-1", title="Review fictional orchard", notes="", owner="", project="Orchard", due="", priority="high", status="waiting", source="Fictional fixture", updatedAt="2026-09-10T00:00:00Z")
            preserved["todo/tasks.json"] = c.json_bytes(dict(schemaVersion=1, revision=7, updatedAt=None, tasks=[task]))
            for name, data in preserved.items():
                dest = personal / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
            (personal / "todo/board.html").write_text("Old generated view", encoding="utf-8")
            snapshot = lambda folder: {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob("*") if p.is_file()}
            before = snapshot(old)
            shutil.copytree(ROOT / "templates", new / "templates")
            shutil.copytree(personal, new / "personal")
            c.init(new)
            self.assertEqual(snapshot(old), before)
            for name, data in preserved.items():
                self.assertEqual((new / "personal" / name).read_bytes(), data, name)
            self.assertIn(task["title"], (new / "personal/todo/board.html").read_text(encoding="utf-8"))
            self.assertEqual(json.loads((new / "personal/todo/tasks.json").read_bytes())["revision"], 7)
            self.assertTrue((new / "personal/vault/journal/README.md").exists())
            self.assertTrue((new / "personal/vault/vault-conventions.md").exists())
            restored = Path(tmp) / "restored"
            shutil.copytree(personal, restored)
            self.assertEqual(snapshot(restored), snapshot(personal))
