# V1.0 release decision

Decision date: 2026-09-10. The maintainer explicitly authorised v1.0.0 after supplying user test reports. The release scope is the portable core kit with conditional app/connector integrations. Remaining checks below are accepted limitations, not claimed passes.

## Evidence used

- Automated setup, persistence, task-board, import-conflict, public-package and site tests, including the safe-update regression.
- Published beta.2 to beta.3 synthetic upgrade rehearsal: all authoritative personal state preserved, original folder unchanged and recovery copy matched. Repeated against the final v1.0 package before publication.
- User-reported Codex/Windows local context retrieval, read-only Outlook email summary and briefing/journal save/read-back. A Windows sandbox login issue affected the test environment; protected default setup remains environment-dependent.
- User-reported Claude Code cold start, profile customisation and honest fallback when Microsoft 365 access was blocked by application assignment.

See [TESTING.md](TESTING.md) for actual results and provenance and [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for public guidance. Reports are deliberately summarised without personal content, account names or application identifiers.

## Accepted limitations and follow-up checks

- No separate timed nontechnical-colleague pilot result was supplied.
- No fresh-conversation cross-app round trip, native browser OS picker exercise or personal-skill end-to-end result was supplied. Browser application code and the fallback were tested automatically; this does not establish native permission-UI behaviour.
- Calendar, Teams, attachments, full multi-source briefing and connector writes were not tested. The briefing workflow is read-only; connector writes are outside its scope.
- No claim of comprehensive model prompt-injection resistance, sandbox enforcement or independent security certification.
- The reported Windows sandbox-account issue remains unresolved. Trying manual approvals is not a verified repair. The kit does not recommend removing isolation or administrative account/configuration changes.

These remain visible in the compatibility and test documentation. They do not become passed tests by changing the release number. Future reports can expand verified support and inform v1.0.x fixes or v1.1.0 improvements. Known kit data-loss or unsafe-action defects require correction; app access failures should be clearly diagnosed and routed to app/IT support.

## Publication checks

Before publishing: run final Windows/Linux CI and browser tests, render and inspect the revised guide/PDF, verify the reviewed public allowlist and final upgrade rehearsal, merge through protected main and publish the versioned ZIP/PDF/checksums/manifest as a stable GitHub Release. Read back public assets and verify hashes after publication. Preserve old releases and the stable Releases-page link.
