# Connections and local access

The kit stores your assistant's files and instructions. Your chosen app supplies local-file tools, Microsoft 365 connections and permission controls. You can start with local notes and tasks before connecting work services.

## Check Microsoft 365 in the app you will use

1. Open the app's approved Apps, Connectors or Integrations settings and use your approved work account.
2. Check Outlook email, Outlook calendar and Teams separately. A connection in another app, or another mode of the same product, does not prove this app has access.
3. Ask: “Check which Outlook email, calendar and Teams read tools you can use. Do not change anything. Run a small check and clearly list unavailable sources.”
4. If sign-in says administrator approval, user assignment or consent is required, ask IT to check access to the specific enterprise application used by that connector. An error such as AADSTS50105 can indicate an assignment block. Do not create your own app registration or bypass company policy.
5. Continue with a labelled partial or local-only briefing while access is resolved. Missing access is not evidence that there are no messages or meetings. Never paste passwords, tokens or connection configuration into chat or public support issues.

Calendar and Teams live retrieval have not yet been verified for this release. Reported Outlook email and local-save results are described in [TESTING.md](TESTING.md); they do not establish that every company's connections will work.

## Codex: try manual approvals if automatic review fails

If **Approve for me** is failing, use the permissions control in the app to try **Ask for approval** (manual approvals), if your organisation allows it. Review requests as they appear and keep the normal sandbox and managed controls enabled. Labels may vary by app version. [Official OpenAI permission guidance](https://learn.chatgpt.com/docs/permission-modes) explains the modes.

Manual approval changes who reviews a request; it does not repair a Windows sandbox login problem. It is a troubleshooting option, not a tested fix for error 1907.

If commands cannot start, including a `CreateProcessWithLogonW failed: 1907` error:

- Check that the correct local folder is open and connected. Ask for a harmless read/save/read-back check; do not start collecting personal setup details until it succeeds.
- Update and restart the app if permitted. If the error remains, contact IT or app support with the app version and error code through an approved private support route.
- You may use another organisation-approved app with working local-folder access. Finish or stop the previous session and allow only one app to write to the folder.

Do not select Full Access, disable the sandbox, change Windows accounts, run administrative repair commands or edit sandbox configuration to get this kit working. The kit does not require those changes. A reported Windows sandbox-account problem is unresolved; no vendor fix date is confirmed.

## Preserve work when switching or updating

Check your profile, handover and task file from disk in the new app. Permissions, connectors and schedules need checking again; memory files do not grant access. For new releases, follow [UPDATING.md](UPDATING.md) and keep your previous folder intact.
