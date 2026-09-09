# File operations without Python

The agent uses its own file tools; the user does not edit code or run commands.

Setup: create personal/profile.md from templates/profile.md; create personal/HANDOVER.md from templates/handover.md; copy templates/tasks.json to personal/todo/tasks.json only if it does not exist. Create personal/vault/HOME.md linking notes as they appear. To render the board, read templates/board.html and replace the single @@TASK_DATA@@ marker with a JSON object containing document (the parsed tasks.json) and sourceHash (SHA-256 of the exact tasks.json UTF-8 file bytes), escaping the serialised JSON text with one-backslash JSON escapes: < as \u003c, > as \u003e and & as \u0026. Write personal/todo/board.html. Read back every output. Never place raw JSON containing a closing script tag into HTML.

For changes, re-read tasks.json first. Validate schemaVersion=1, nonnegative integer revision, unique task ids, statuses todo/doing/waiting/done, priorities high/normal/low, title length 1..240 and dates YYYY-MM-DD or empty. Preserve unknown user prose in note files. Increment revision exactly once per task-file change. Update updatedAt as ISO UTC. Read back after writing.

For a browser export: accept only format=companion-task-edit, schemaVersion=1, baseRevision matching the current tasks.json revision, and baseHash matching SHA-256 of the exact UTF-8 source file bytes. Validate every task. If hashes cannot be checked with available tools, do not blindly import; show the task changes and reconcile against current state with the user's confirmation. On conflict, retain both files and compare task ids individually. Never copy a stale full snapshot over current tasks.

Skills: create personal/skills/<name>/SKILL.md with Agent Skills name/description metadata, then add it to personal/skills/INDEX.md. After approval, optionally create native discovery wrappers with a unique personal- prefix. Wrapper relative paths must resolve to the personal skill from their own folder. The index is the universal fallback if native discovery needs an app restart.
