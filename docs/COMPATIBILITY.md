# Compatibility and scope

V1.0.0 is a stable release of the portable folder kit. The app provides tools, permissions and connectors; the kit cannot grant them. App availability varies by OS, version, plan and company policy.

| App profile | Reported evidence for v1.0 | Limits |
|---|---|---|
| Codex desktop on Windows | Local context retrieval, Outlook email summary, saved briefing/journal and read-back; no mailbox mutation reported | Tests encountered a Windows sandbox login issue and used an environment-specific workaround. Normal protected setup is not universally verified; see troubleshooting. Calendar/Teams were not tested. |
| Claude Code | Cold-start setup offer, assistant rename saved in the profile, honest missing-connector handling | Microsoft 365 sign-in was blocked by enterprise-app assignment; live retrieval was not tested. |
| ChatGPT Work Local | Folder adapter and shared skill index provided | No signed-in acceptance result supplied. |
| Claude Cowork | Connected-folder adapter and shared skill index provided | No signed-in acceptance result supplied. |
| Other capable local-file agents | Explicit instruction and skill-index fallback | Check local persistence and each integration before relying on it. |

These are user-reported tests on the beta.3 core carried into v1.0 without helper or board behaviour changes. Exact app build numbers were not supplied. This is not universal app certification or proof of sandbox enforcement. OpenAI approval-mode guidance and basic Microsoft 365 checks are in [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

The kit has .agents/skills and .claude/skills discovery wrappers plus a shared index. AGENTS.md and CLAUDE.md load the same shared instructions. When an app does not auto-load them, use the starter prompt or the relevant adapters/<app>.md. Ordinary hosted chats need explicit file import/export; they do not automatically share your local vault.

## Check before relying on a new app

1. Open the kit as the primary local folder and send the starter prompt.
2. Have the agent identify the shared instructions and daily-brief skill.
3. Save a harmless note and task under personal/ and read both back.
4. Start a new conversation, retrieve the saved files and update the task.
5. Check each connector separately and confirm missing sources are labelled.

Use one writer at a time. Do not use a Git worktree for live personal memory: ignored files may be absent and parallel copies can diverge. Native app prerequisites belong to the vendor, not this ZIP. Keep the app's sandbox and approval controls enabled.

Vendor references: [OpenAI projects](https://learn.chatgpt.com/docs/projects), [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [Work Local](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-local-security), [Claude Desktop](https://code.claude.com/docs/en/desktop), [Claude skills](https://code.claude.com/docs/en/skills), [Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), [Agent Skills](https://agentskills.io/specification). Product labels and prerequisites can change.
