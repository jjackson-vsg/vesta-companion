# Optional Claude approval settings

The default kit uses your app's existing permission controls. For colleagues who prefer an explicit approval for each shell command and file edit, templates/claude-settings.example.json is an optional starting point.

Ask your assistant: "Show me the optional Claude approval settings and how they would change my current setup."

The template keeps default permission mode, adds ask rules for Bash, Edit and Write, and denies direct access to common environment/secret paths. It contains no allow rules, hooks, credentials or connector setup. It is not loaded automatically.

After you approve the precise change, your assistant can merge the selected rules into .claude/settings.local.json in your own folder. Preserve existing and managed settings; do not replace a configuration wholesale. Reload Claude and verify the settings loaded using the controls available in that app/version. Expect more prompts; other agents do not use this file.

These rules are a convenience layer, not a comprehensive secret filter or deletion sandbox. Read rules do not cover every route by which code or connectors can access data. A list of rm/del command spellings is not reliable protection. Keep the OS/app sandbox and existing organisation controls enabled. Do not weaken managed policy to activate this template.

Sources checked 2026-09-10: [Claude settings](https://code.claude.com/docs/en/settings), [permission rules](https://code.claude.com/docs/en/permissions). Signed-in testing of this optional profile remains part of the pilot.
