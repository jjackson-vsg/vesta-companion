---
name: companion-care
description: Help with backup, recovery, safe updates, connection checks and optional schedules. Use when the user asks to back up, move apps, upgrade or schedule briefings.
license: Apache-2.0
metadata:
  version: "1.1.0"
  review-status: "local-technical-review"
---

# companion care

1. Identify the specific operation and read personal profile, handover and schedule registry first. No automatic background installation or unsolicited remote copying.
2. Backup: explain what to protect (personal/), ask for an organisation-approved private destination, and get approval for the exact copy. No secrets in archives. Use a new timestamped archive; never overwrite an existing backup. Verify its contents and rehearse restore to a new empty test folder when authorised.
3. Restore: keep the original intact. Extract into a new empty folder, reject archive traversal/symlinks, verify notes/tasks, then ask before switching. Never bulk replace the live folder.
4. Upgrade: download only a reviewed official release after user request, verify published checksum, extract alongside the current folder and compare system changes. Preserve personal/ and user skills. Do not execute new scripts until reviewed. Migrations need a preview, backup and explicit approval.
5. Schedule: confirm time, timezone, recurrence, source scope, output path, app owner, notification preference and unattended limits. Register with only the current app's callable approved scheduler. Never use a shell scheduler workaround.
6. Store non-secret schedule intent, owner, stable scheduler id and last verified status under personal/automations/. Inspect existing jobs before creating one. When moving apps, disable the old job with approval before activating the replacement. A registry file alone is not evidence a schedule exists.
7. State whether the task needs an awake device, connected folder and valid connections. Use actual app evidence. Unattended briefings remain Microsoft 365 read-only, with local output only; queue actions requiring user approval.
8. Connection health: check only tool availability/least-privilege reads the user requested. Record capability status, never connector configuration. Missing permissions route to the organisation's administrator.
9. Backup reminders: read the Backup care fields in personal/HANDOVER.md at setup and weekly review. If no backup is confirmed or its agreed interval has elapsed, offer one brief optional reminder. Honour a snooze or disabled reminders; record the date offered so it is not repeated on every chat. Keep working if the user declines. Record backup/restore dates only after evidence or explicit user confirmation, labelled accordingly.
10. Save a journal and handover update. Do not claim backup, restoration, schedule or connection success without verification.

Success: a verified, reversible action with its exact scope and remaining limitations recorded.
