from pathlib import Path
import shutil
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import build_site

class SiteTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        for name in ["site/index.html","START-HERE.html","examples/board.html","docs/Quick-start.pdf"]:
            dest=self.root/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,dest)
    def tearDown(self):
        self.temp.cleanup()
    def test_site_contains_only_reviewed_public_inputs(self):
        private=self.root/"personal/private-note.md";private.parent.mkdir();private.write_text("fictional private sentinel")
        out=build_site.build(self.root)
        self.assertEqual({p.name for p in out.iterdir()},{"index.html","guide.html","demo.html","Quick-start.pdf"})
        self.assertFalse(any(b"fictional private sentinel" in p.read_bytes() for p in out.iterdir()))
        demo=(out/"demo.html").read_text(encoding="utf-8")
        self.assertIn("Fictional demo only",demo)
        self.assertIn('document.getElementById(id).hidden=true',demo)
    def test_site_refuses_unexpected_leftovers(self):
        out=self.root/"dist/site";out.mkdir(parents=True);(out/"private.txt").write_text("keep me private")
        with self.assertRaises(ValueError):build_site.build(self.root)
        self.assertEqual((out/"private.txt").read_text(),"keep me private")

if __name__=="__main__":unittest.main()
