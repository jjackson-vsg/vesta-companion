---
name: companion-planning
description: Prioritise work, make plans and maintain the local to-do list and HTML board. Use when the user supplies tasks, asks what to do next, or wants to update their board.
license: Apache-2.0
metadata:
  version: "1.1.0"
  review-status: "local-technical-review"
---

# companion planning

1. Read personal/todo/tasks.json and current project context before editing. Capture raw tasks supplied by the user here rather than tracking them only in chat.
2. Identify the desired outcome and next concrete action. Ask only for material missing details; leave unconfirmed deadlines empty. Use priorities high/normal/low and statuses todo/doing/waiting/done. Retain stable ids.
3. For each item keep title, notes, project, owner, due, priority, status, source and updatedAt. Do not store secrets or link authentication URLs. Preserve completed items until the user requests archiving.
4. Use scripts/companion.py todo render after edits, or follow templates/FILE-OPERATIONS.md. The canonical source is tasks.json. Never treat browser storage or an old board as authoritative.
5. Browser editing: Open task file reads tasks.json. Save to selected file uses a user-granted browser handle where supported. Otherwise Download changes exports a versioned edit envelope that the agent imports. Explain that a download is not a completed save to the vault.
6. Import with scripts/companion.py todo import <export>. It rejects wrong revision/hash and malformed data. On conflict, compare by id and reconcile explicitly; never force overwrite or discard the newest version.
7. Prioritise by impact, deadline, dependency and effort. Suggest at most three focus tasks. Separate suggested actions from confirmed commitments. Briefing-derived ambiguous requests need confirmation.
8. Read back updated data, regenerate the board and handover, and link personal/todo/board.html. One active writer at a time. Do not modify a source in another system just because its local task is marked done.

Success: edits survive refresh/reopen, stale imports are rejected, and the board matches the canonical file.
