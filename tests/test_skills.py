import re
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class SkillDiscoveryTests(unittest.TestCase):
    def test_all_skills_discoverable_with_valid_local_references(self):
        skills=sorted((ROOT/"skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills),21)
        index=(ROOT/"skills/INDEX.md").read_text(encoding="utf-8")
        for p in skills:
            text=p.read_text(encoding="utf-8")
            self.assertIn(f"({p.parent.name}/SKILL.md)",index)
            for adapter in [".agents/skills",".claude/skills"]:
                wrapper=ROOT/adapter/p.parent.name/"SKILL.md"
                target=re.search(r"Read (\S+/SKILL.md)",wrapper.read_text(encoding="utf-8")).group(1)
                self.assertEqual((wrapper.parent/target).resolve(),p.resolve())
            for ref in re.findall(r"(?:templates|docs)/[A-Za-z0-9_./-]+\.(?:md|html|json)",text):
                self.assertTrue((ROOT/ref).is_file(),ref)
        self.assertEqual((ROOT/"AGENTS.md").read_bytes(),(ROOT/"CLAUDE.md").read_bytes())
    def test_release_has_no_legacy_workspace_dependency(self):
        for p in (ROOT/"skills").glob("*/SKILL.md"):
            text=p.read_text(encoding="utf-8")
            self.assertNotIn("docs/ADVANCED.md",text)
            self.assertNotIn("compatibility-workspace",text)
