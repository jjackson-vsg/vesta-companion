"""Build public-only assets and release archives; no network or dependencies."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile
import companion

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = {"personal", ".work", ".git", "dist", "backups", "node_modules", "__pycache__"}

def adapters(root=ROOT):
    root = Path(root)
    for skill in sorted((root / "skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        name = re.search(r"^name: (.+)$", text, re.M).group(1)
        description = re.search(r"^description: (.+)$", text, re.M).group(1)
        for directory in [".agents/skills", ".claude/skills"]:
            dest = root / directory / name / "SKILL.md"
            body = f"---\nname: {name}\ndescription: {description}\n---\n\nRead ../../../skills/{name}/SKILL.md and follow it. The canonical skill is the source of truth. Read system/COMPANION.md from the project root. Keep personal data under personal/.\n"
            companion.atomic_write(dest, body.encode())

def demo(root=ROOT):
    root = Path(root)
    raw = (root/"examples/tasks.json").read_bytes()
    data = companion.validate_tasks(json.loads(raw))
    envelope = json.dumps({"document":data,"sourceHash":companion.digest(raw)},ensure_ascii=False)
    envelope = envelope.replace("&",r"\u0026").replace("<",r"\u003c").replace(">",r"\u003e")
    html = (root/"templates/board.html").read_text(encoding="utf-8").replace("@@TASK_DATA@@",envelope)
    html = html.replace("Make space for the work that matters.","Fictional demo tasks. Your own board starts empty.")
    companion.atomic_write(root/"examples/board.html",html.encode("utf-8"))

def allowed(root=ROOT):
    root = Path(root)
    lines = (root/"PUBLIC-FILES.txt").read_text(encoding="utf-8").splitlines()
    result = []
    for line in lines:
        if not line or line.startswith("#"):
            continue
        p = PurePosixPath(line)
        if line != p.as_posix() or p.is_absolute() or "\\" in line or ":" in line or any(part in PRIVATE or part in (".","..") for part in p.parts):
            raise ValueError("Unsafe release path: " + line)
        path = companion.safe_path(root, line)
        if not path.is_file():
            raise ValueError("Missing public file: " + line)
        result.append(line)
    if len(result) != len(set(result)) or not result:
        raise ValueError("Invalid public allowlist")
    return sorted(result)

def check(root=ROOT):
    root = Path(root)
    files = allowed(root)
    # Public checkout only. Never auto-stage all files.
    if (root/".git").exists():
        tracked = subprocess.check_output(["git","ls-files","-z"],cwd=root).decode().split("\0")
        extra = {p for p in tracked if p} - set(files) - {"PUBLIC-FILES.txt"}
        if extra:
            raise ValueError("Tracked files outside allowlist: " + ", ".join(sorted(extra)))
    for skill in (root/"skills").glob("*/SKILL.md"):
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "description:" not in text or f"name: {skill.parent.name}\n" not in text:
            raise ValueError("Invalid skill metadata")
        for adapter in (".agents/skills", ".claude/skills"):
            wrapped = root/adapter/skill.parent.name/"SKILL.md"
            if not wrapped.exists() or f"../../../skills/{skill.parent.name}/SKILL.md" not in wrapped.read_text():
                raise ValueError("Missing or stale skill adapter")
    for required in ["LICENSE","START-HERE.html","docs/Quick-start.pdf","scripts/companion.py","examples/board.html"]:
        if required not in files:
            raise ValueError("Missing required release file: " + required)
    # Heuristic checks supplement manual review; they do not establish confidentiality.
    secret_patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\b(?:ghp|gho)_[A-Za-z0-9]{30,}\b"),
        re.compile(r"\bsk-[A-Za-z0-9_-]{35,}\b"),
        re.compile(r"https://[^/\s]+\.sharepoint\.com/", re.I),
        re.compile(r"C:[\\/]+Users[\\/]+(?!<)[^\\/\s]+", re.I),
    ]
    for name in files:
        if name.endswith((".pdf",".png")):
            continue
        text = (root/name).read_text(encoding="utf-8")
        if any(p.search(text) for p in secret_patterns):
            raise ValueError("Potential secret/private identifier in " + name)
    return files

def package(root=ROOT):
    root = Path(root)
    files = check(root)
    version = (root/"VERSION").read_text().strip()
    out = root/"dist"
    out.mkdir(exist_ok=True)
    archive = out/"vesta-companion.zip"
    with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in files + ["PUBLIC-FILES.txt"]:
            info = zipfile.ZipInfo("vesta-companion/"+name, date_time=(2026,9,9,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, (root/name).read_bytes())
    manifest = {"version":version,"files":{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in files+["PUBLIC-FILES.txt"]}}
    companion.atomic_write(out/"manifest.json",companion.json_bytes(manifest))
    companion.atomic_write(out/"SHA256SUMS.txt",(hashlib.sha256(archive.read_bytes()).hexdigest()+"  vesta-companion.zip\n"+hashlib.sha256((root/"docs/Quick-start.pdf").read_bytes()).hexdigest()+"  Quick-start.pdf\n"+hashlib.sha256((out/"manifest.json").read_bytes()).hexdigest()+"  manifest.json\n").encode())
    # Verify extracted bytes in memory; no paths from untrusted archives are extracted.
    with zipfile.ZipFile(archive) as z:
        assert len(z.namelist()) == len(files)+1
        for name, value in manifest["files"].items():
            assert hashlib.sha256(z.read("vesta-companion/"+name)).hexdigest() == value
    return archive

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--assets",action="store_true")
    p.add_argument("--check",action="store_true")
    p.add_argument("--package",action="store_true")
    args=p.parse_args()
    if args.assets:
        adapters();demo();print("Generated adapters and fictional demo")
    if args.check:
        print("Public allowlist checked:",len(check()),"files")
    if args.package:
        print(package())

if __name__=="__main__":
    main()
