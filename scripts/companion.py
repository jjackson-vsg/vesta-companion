"""Optional local helper. Python 3.10+ standard library; no network access."""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TASK_KEYS = {"id", "title", "notes", "project", "owner", "due", "priority", "status", "source", "updatedAt"}

def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

def safe_path(root, relative):
    root = Path(root).resolve()
    path = root / relative
    # Reject symlinks/junctions at every existing component, including parents.
    cursor = path
    while cursor != root:
        if cursor.is_symlink() or (hasattr(cursor, "is_junction") and cursor.is_junction()):
            raise ValueError("Linked paths are not supported")
        cursor = cursor.parent
        if cursor == cursor.parent and cursor != root:
            raise ValueError("Path escapes the project")
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("Path escapes the project")
    return resolved

def validate_tasks(data):
    if not isinstance(data, dict) or set(data) != {"schemaVersion", "revision", "updatedAt", "tasks"}:
        raise ValueError("Invalid task document fields")
    if type(data["schemaVersion"]) is not int or data["schemaVersion"] != 1:
        raise ValueError("Unsupported schemaVersion")
    if type(data["revision"]) is not int or not 0 <= data["revision"] <= 9007199254740991:
        raise ValueError("Invalid revision")
    if data["updatedAt"] is not None and (not isinstance(data["updatedAt"], str) or len(data["updatedAt"]) > 50):
        raise ValueError("Invalid document updatedAt")
    if not isinstance(data["tasks"], list) or len(data["tasks"]) > 10000:
        raise ValueError("Invalid tasks list")
    ids = set()
    for task in data["tasks"]:
        if not isinstance(task, dict) or set(task) != TASK_KEYS:
            raise ValueError("Invalid task fields")
        limits = {"id":100, "title":240, "notes":10000, "project":120, "owner":120, "source":2000, "due":10, "updatedAt":50}
        for key, limit in limits.items():
            if not isinstance(task[key], str) or len(task[key]) > limit:
                raise ValueError("Invalid " + key)
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,100}", task["id"]) or task["id"] in ids:
            raise ValueError("Invalid or duplicate id")
        ids.add(task["id"])
        if not task["title"].strip():
            raise ValueError("Empty task title")
        if task["status"] not in ("todo", "doing", "waiting", "done") or task["priority"] not in ("high", "normal", "low"):
            raise ValueError("Invalid task status or priority")
        if task["due"]:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", task["due"]):
                raise ValueError("Invalid due date")
            dt.date.fromisoformat(task["due"])
    return data

def atomic_write(path, raw, expected=None, create_only=False):
    path = Path(path)
    if path.is_symlink():
        raise ValueError("Refusing linked destination")
    path.parent.mkdir(parents=True, exist_ok=True)
    if create_only and path.exists():
        return False
    if expected is not None and (not path.exists() or path.read_bytes() != expected):
        raise ValueError("File changed; refusing to overwrite")
    fd, name = tempfile.mkstemp(prefix="." + path.name + "-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        if expected is not None and path.read_bytes() != expected:
            raise ValueError("Concurrent change; refusing to overwrite")
        if create_only and path.exists():
            return False
        os.replace(name, path)
        if path.read_bytes() != raw:
            raise ValueError("Write verification failed")
    finally:
        if os.path.exists(name):
            os.unlink(name)
    return True

def read_tasks(path):
    raw = Path(path).read_bytes()
    if len(raw) > 2_000_000:
        raise ValueError("Task file too large")
    return raw, validate_tasks(json.loads(raw.decode("utf-8-sig")))

def render_board(root=ROOT):
    root = Path(root)
    path = safe_path(root, "personal/todo/tasks.json")
    raw, data = read_tasks(path)
    envelope = json.dumps({"document": data, "sourceHash": digest(raw)}, ensure_ascii=False)
    envelope = envelope.replace("&", r"\u0026").replace("<", r"\u003c").replace(">", r"\u003e")
    template = safe_path(root, "templates/board.html").read_text(encoding="utf-8")
    if template.count("@@TASK_DATA@@") != 1:
        raise ValueError("Invalid board template")
    board = safe_path(root, "personal/todo/board.html")
    atomic_write(board, template.replace("@@TASK_DATA@@", envelope).encode("utf-8"))
    return board

def init(root=ROOT):
    root = Path(root)
    for source, target in [
        ("templates/profile.md", "personal/profile.md"),
        ("templates/handover.md", "personal/HANDOVER.md"),
        ("templates/tasks.json", "personal/todo/tasks.json"),
    ]:
        atomic_write(safe_path(root, target), safe_path(root, source).read_bytes(), create_only=True)
    # Add missing starter files only. Existing notes and Obsidian settings are user-owned.
    day = dt.datetime.now(dt.timezone.utc).date().isoformat()
    starter_files = [(name, name) for name in ["HOME.md", "vault-conventions.md"]]
    starter_files += [(folder + "/README.md", folder + "/README.md") for folder in
                      ["inbox", "knowledge", "contacts", "decisions", "meetings", "journal", "attachments", "archive"]]
    starter_files += [("obsidian-app.json", ".obsidian/app.json"),
                      ("obsidian-community-plugins.json", ".obsidian/community-plugins.json")]
    for template_name, target_name in starter_files:
        source = safe_path(root, "templates/vault/" + template_name)
        target = safe_path(root, "personal/vault/" + target_name)
        content = source.read_text(encoding="utf-8").replace("{{date}}", day)
        atomic_write(target, content.encode("utf-8"), create_only=True)
    atomic_write(safe_path(root,"personal/skills/INDEX.md"), b"# My skills\n\nApproved personal workflows appear here. No custom skills yet.\n", create_only=True)
    return render_board(root)

def import_tasks(export_path, root=ROOT):
    root = Path(root)
    if Path(export_path).stat().st_size > 2_000_000:
        raise ValueError("Export too large")
    edit = json.loads(Path(export_path).read_text(encoding="utf-8-sig"))
    if not isinstance(edit, dict) or set(edit) != {"format","schemaVersion","baseRevision","baseHash","tasks","exportedAt"}:
        raise ValueError("Invalid export fields")
    if edit.get("format") != "companion-task-edit" or (type(edit.get("schemaVersion")) is not int or edit.get("schemaVersion") != 1) or type(edit.get("baseRevision")) is not int:
        raise ValueError("Unsupported export")
    source = safe_path(root, "personal/todo/tasks.json")
    # Cooperative lock prevents overlapping helper mutations; still use one writer
    # because browser/native agent edits do not universally honour this lock.
    lock = safe_path(root, "personal/todo/.write.lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError("Task write already in progress; inspect stale lock before retrying") from None
    try:
        os.close(fd)
        raw, current = read_tasks(source)
        if edit["baseRevision"] != current["revision"] or edit["baseHash"] != digest(raw):
            raise ValueError("Stale export: source changed. Reconcile by task id; do not overwrite.")
        proposed = {"schemaVersion":1,"revision":current["revision"]+1,"updatedAt":stamp(),"tasks":edit["tasks"]}
        validate_tasks(proposed)
        # The board does not delete tasks; imports cannot silently remove any.
        if not {t["id"] for t in current["tasks"]} <= {t["id"] for t in proposed["tasks"]}:
            raise ValueError("Import would remove tasks; explicit reconciliation required")
        backup = safe_path(root, "personal/todo/history/revision-" + str(current["revision"]) + "-" + digest(raw)[:12] + ".json")
        atomic_write(backup, raw, create_only=True)
        atomic_write(source, json_bytes(proposed), expected=raw)
        render_board(root)
        return proposed["revision"]
    finally:
        lock.unlink()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    todo = sub.add_parser("todo").add_subparsers(dest="action", required=True)
    todo.add_parser("render")
    todo.add_parser("validate")
    imp = todo.add_parser("import")
    imp.add_argument("export", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "init":
            print(init())
        elif args.action == "render":
            print(render_board())
        elif args.action == "validate":
            _, doc = read_tasks(safe_path(ROOT,"personal/todo/tasks.json"))
            print("Valid: revision", doc["revision"], "tasks", len(doc["tasks"]))
        else:
            print("Imported and verified revision", import_tasks(args.export))
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, "Not completed: " + str(error) + "\n")

if __name__ == "__main__":
    main()
