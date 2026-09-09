# Compatibility and honest limits

Beta target profiles: Codex desktop local folder; ChatGPT Work Local with local file tools; Claude Code Desktop local folder; Claude Cowork with connected folder access. Ordinary browser chat and hosted tasks need explicit file import/export; they do not automatically share your local vault.

The kit has native .agents/skills and .claude/skills discovery wrappers plus an explicit skill index fallback. AGENTS.md and CLAUDE.md load the same shared instructions. For Cowork and ChatGPT modes that do not auto-load those files, use the starter prompt or paste adapters/<app>.md into the app's project/folder instructions. No adapter grants tools or permissions.

A successful release test of files and wrappers is not an end-to-end test in every app. The v0.1 beta has automated file/schema/board tests; actual signed-in cross-harness and Microsoft 365 testing plus nontechnical pilot evidence must be recorded in docs/TESTING.md before claiming full compatibility. App labels and availability can vary by OS, version, plan and organisational policy.

## Startup check for each app
1. Open this folder locally and send the starter prompt.
2. Have the agent identify the shared instructions and find the daily-brief skill.
3. Create a fictional note and a task under personal/; reopen both from disk.
4. Start a new task, retrieve that note, and update the task.
5. Switch to another supported app and retrieve the same files.
6. Test missing connectors, failed writes and a denied destructive request.

Do not use a Git worktree for the user's live memory: ignored personal files may be missing and parallel copies diverge. Use a local folder; only one agent writes at a time. Claude Code's Windows installation currently documents Git for Windows. Other app prerequisites belong to the vendor, not this ZIP.

Sources checked 2026-09-09: [OpenAI projects](https://learn.chatgpt.com/docs/projects), [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [Work Local](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-local-security), [Claude Desktop](https://code.claude.com/docs/en/desktop), [Claude skills](https://code.claude.com/docs/en/skills), [Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), [Agent Skills](https://agentskills.io/specification).
