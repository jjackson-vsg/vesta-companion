# Update your Companion safely

You do not need to reinstall your AI app or start your assistant's memory again.

1. Ask your current assistant to save progress and update its handover. Finish any task-board edits and use only one active writer.
2. Open the [Releases page](https://github.com/Vesta-Software-Group/vesta-companion/releases). Find the newest release at the top, scroll to its **Assets** section, expand it if needed, and download **vesta-companion.zip**. The Source code files are not the prepared user download.
3. Extract the ZIP into a **separate new folder**. Never extract over your existing Companion folder. Keep the old folder intact.
4. In your current assistant, give it the new folder's location and paste:

> Help me update to this new Companion version. Keep my current folder intact, copy my personal files into the new folder, and check my profile, notes, tasks and custom skills before I switch. Review any other customisations with me first.

5. Let it compare the versions and explain the proposed copy. It should verify the published checksum, review changed instructions and helper code, and copy the complete **personal/** folder only into a new installation with no existing personal data. If the destination is already populated, stop and select another fresh folder; do not merge blindly. It must compare copied files with their originals before adding missing starter files and rebuilding the board. Your saved task data remains authoritative.
6. Open the new folder as a local project in your agent. Start a fresh conversation and ask it to recall one saved preference and one note, show your current tasks, and use one personal skill. Check the saved files and task statuses. App permissions and connectors may need checking for the new folder.
7. Work from the new folder once those checks pass. Keep the old folder as a recovery copy until you are satisfied; do not edit both copies. If a check fails, stop and resume from the untouched old folder while the problem is investigated.

Personal skills and their index are copied with personal/. If you customised files elsewhere, including native discovery wrappers or local app settings, ask the assistant to compare them and propose what should be carried forward. Do not blindly copy old built-in instructions over the new kit, activate schedules twice, weaken managed permissions or copy authentication configuration. Custom skills remain available through personal/skills/INDEX.md even if a native wrapper needs to be recreated after review.

If your agent cannot access both folders, add the new folder using its normal approved folder controls or ask for guided manual copy steps. Do not switch to a bypass mode. A retained old folder is a recovery copy on the same device; it does not replace your normal approved backup.

## V1.0.0 to v1.1.0

The personal/ layout and task JSON schema are unchanged. Copy the complete personal/ folder using the steps above. No data-format conversion or new dependencies are required. New report, persona and commitment folders are created only when you choose to use those workflows. Existing user notes and vault conventions are preserved; the assistant can consult the new shipped templates without overwriting your conventions.

## What has been verified

A rehearsal using the published beta.2 and beta.3 ZIPs passed on Windows with fictional profile, handover, notes, tasks, custom skills, legacy journals and Obsidian preferences. Every pre-existing authoritative personal file retained identical bytes, the original folder was unchanged, the new board showed the existing task/status, and a recovery copy matched. This establishes the file-copy route; it does not claim that every agent app has been tested.

V1.1 verification also used the published v1.0.0 ZIP with fictional data: existing personal files and original folder retained identical bytes; task revision/status and custom skills were preserved. No format conversion was required.
