---
name: companion-memory
description: Remember and recall preferences, decisions, knowledge and progress from local files. Use when the user asks to remember, retrieve context, resume work or switch apps.
license: Apache-2.0
metadata:
  version: "1.0.0"
  review-status: "local-technical-review"
---

# companion memory

1. Read personal/vault/vault-conventions.md, the profile and handover, then search personal/vault by HOME.md, filenames, metadata and content. Follow direct source links as needed. Distinguish actual evidence from inference; do not invent missing notes.
2. Save new durable knowledge in a clearly named Markdown file under personal/vault. Use the matching note/contact/meeting/decision template and its small frontmatter standard. Replace {{date}} with the actual date, preserve created on updates, and keep source, confidence and status accurate. Never save credentials, token-bearing links or one-time codes.
3. For corrections, retain relevant history and mark which statement supersedes which. Preserve user-authored material; propose substantial replacement before writing.
4. Keep contacts in personal/vault/contacts, decisions in personal/vault/decisions, meetings in personal/vault/meetings and reference knowledge in personal/vault/knowledge. Use inbox for unfiled captures and personal/vault/journal for dated progress. Existing journals in other personal folders remain in place. Link the note from HOME.md. Tasks belong in personal/todo/tasks.json, not duplicate tick lists.
5. Re-read before replacing and confirm the write afterward. Save milestone progress to personal/HANDOVER.md during long tasks. Include output paths, accepted decisions, current status, next step and access gaps; not hidden reasoning or credentials.
6. When changing apps, finish pending writes, refresh handover and ask the new app to read system/COMPANION.md plus the same personal files. Permissions, connectors and schedules must be checked independently in the new app.
7. If saving is unavailable, explicitly label the response UNSAVED and provide an export the user can save. Never claim a downloaded file is already in their chosen folder.

Success: a new chat can retrieve the fact from a cited local file without the prior conversation.
