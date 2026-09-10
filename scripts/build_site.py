"""Build only the public landing page, guide, PDF and fictional demo for Pages."""
from pathlib import Path
import companion

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ("index.html", "guide.html", "demo.html", "Quick-start.pdf")

def build(root=ROOT):
    root = Path(root)
    out = companion.safe_path(root, "dist/site")
    out.mkdir(parents=True, exist_ok=True)
    # Refuse unexpected site leftovers rather than uploading extra files.
    extras = {p.name for p in out.iterdir()} - set(OUTPUTS)
    if extras:
        raise ValueError("Unexpected site outputs; review before publishing")
    html = (root/"START-HERE.html").read_text(encoding="utf-8")
    html = html.replace('href="docs/COMPATIBILITY.md"', 'href="https://github.com/Vesta-Software-Group/vesta-companion/blob/main/docs/COMPATIBILITY.md"')
    demo = (root/"examples/board.html").read_text(encoding="utf-8")
    demo = demo.replace("Fictional demo tasks. Your own board starts empty.", "Interactive preview with fictional tasks. Keep real work in your local kit.")
    # A hosted preview is for fictional data only. Hide local-file/import/export controls.
    preview = """<script>
for(const id of ["open-file","save","export","fallback-file"]){document.getElementById(id).hidden=true;}
document.getElementById("savebar").style.display="none";
document.getElementById("open-file").onclick=()=>{};
document.getElementById("fallback-file").onchange=()=>{};
document.querySelector(".help").textContent="Fictional demo only. Changes here are temporary. Download the kit from the repository Releases page to keep your own tasks locally.";
document.getElementById("save-detail").textContent="Fictional preview. Explore adding, editing and completing tasks.";
</script>"""
    demo = demo.replace("</body>", preview+"</body>")
    sources = {"index.html":(root/"site/index.html").read_bytes(), "guide.html":html.encode("utf-8"),
               "demo.html":demo.encode("utf-8"), "Quick-start.pdf":(root/"docs/Quick-start.pdf").read_bytes()}
    for name, raw in sources.items():
        companion.atomic_write(companion.safe_path(root, "dist/site/"+name), raw)
    return out

if __name__ == "__main__":
    print(build())
