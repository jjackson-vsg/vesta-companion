import importlib.util
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import build

class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        for name in ["LICENSE","START-HERE.html","docs/Quick-start.pdf","scripts/companion.py","examples/board.html","VERSION"]:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text("0.1.0-beta.1" if name=="VERSION" else "public fixture")
        (self.root/"skills").mkdir()
        self.allow=["LICENSE","START-HERE.html","docs/Quick-start.pdf","scripts/companion.py","examples/board.html","VERSION"]
        self.save_allow()

    def save_allow(self):
        (self.root/"PUBLIC-FILES.txt").write_text("\n".join(self.allow)+"\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_private_files_do_not_enter_zip(self):
        private=self.root/"personal/secret-note.md";private.parent.mkdir();private.write_text("fictional private sentinel")
        archive=build.package(self.root)
        with zipfile.ZipFile(archive) as z:
            self.assertEqual(len(z.namelist()),len(self.allow)+1)
            self.assertFalse(any("personal" in n for n in z.namelist()))
            self.assertFalse(any(b"fictional private sentinel" in z.read(n) for n in z.namelist()))

    def test_deterministic_archive(self):
        a=build.package(self.root).read_bytes()
        b=build.package(self.root).read_bytes()
        self.assertEqual(a,b)

    def test_unsafe_allowlist_rejected(self):
        for name in ["../outside","personal/profile.md","dist/file.zip","C:/outside","docs\\file.md"]:
            self.allow.append(name);self.save_allow()
            with self.assertRaises(ValueError):build.allowed(self.root)
            self.allow.pop()

    def test_duplicate_allowlist_rejected(self):
        self.allow.append("LICENSE");self.save_allow()
        with self.assertRaisesRegex(ValueError,"allowlist"):build.allowed(self.root)

    def test_missing_required_asset_fails(self):
        self.allow.remove("docs/Quick-start.pdf");self.save_allow()
        with self.assertRaisesRegex(ValueError,"required"):build.check(self.root)

if __name__=="__main__":
    unittest.main()
