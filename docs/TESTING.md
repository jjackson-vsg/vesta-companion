# Test evidence

Version: 0.1.0-beta.2
Checked: 2026-09-09
Status: local technical checks passed; signed-in app and Microsoft 365 pilot pending.

## Executed checks

| Check | Actual result |
|---|---|
| Python standard-library suite | 17 tests passed: additive setup, persistent imports, revision/hash conflicts, removal refusal, malformed data, locking, traversal, HTML escaping and release isolation. |
| Offline task board in headless Microsoft Edge | Passed adding, editing, filtering, completion, export format, unsaved warnings, responsive layout and script-tag display as plain text. No HTTP requests observed. |
| Selected-file saving | Save/read-back, rejection of changed source files, locking of editing during a save, exact-byte BOM hashing, strict document fields and oversized-save refusal passed. The OS picker and file handle were mocked; the board's real application code ran. |
| User guide | 12 A4 PDF pages generated from the shipped HTML. All pages rendered and visually reviewed; layout checks found no content/footer overlap. Mobile HTML checked for horizontal overflow. |
| Public packaging | Explicit reviewed allowlist. Tests confirm private sentinel files never enter the ZIP, unsafe paths are rejected and unchanged inputs produce identical archive bytes. Release build verifies every archive entry against the SHA-256 manifest. |
| Extracted release smoke check | The actual ZIP was extracted into a fresh temporary folder. Setup created empty personal state and rendered the board successfully. |
| Dependency review | Original core instructions and code; no third-party skill code, runtime bundle, installer, telemetry or remote asset dependencies. Maintainer PDF/browser checks use an already installed Playwright and Edge. |

These results are local technical evidence, not an independent security audit or proof of model compliance. The browser OS permission prompt was not exercised, and no live Microsoft 365 messages were read for these checks.

## Pilot gates before stable release

- Signed-in Codex, ChatGPT Work Local, Claude Code Desktop and Cowork: setup, local write/read-back, fresh task retrieval and cross-app handover on target devices. Record exact app/OS versions.
- Outlook email/calendar and Teams: successful read-only briefing, missing permissions, pagination, timezone differences, source citations, partial failures and prompt-injection attempts.
- Native browser file selection and saving on supported target browsers; export/import fallback on a browser without direct file access.
- Representative nontechnical setup, a useful first workflow, personal skill creation, backup and restore rehearsal.

The expected behaviour and outstanding agent scenarios are in [SKILL-REVIEW.md](SKILL-REVIEW.md). Do not describe these pilot gates as passed until evidence is recorded.

## Reproduce the technical checks

Maintainers can run:

```text
python -m unittest discover -s tests -v
python scripts/build.py --assets
node tests/browser.cjs
node scripts/render-guide.cjs
python scripts/build.py --check --package
```

Python 3.10+ suffices for the helper and release tests. The browser and PDF scripts require an already installed Playwright module and Microsoft Edge, and do not download dependencies. Set NODE_PATH to that module's parent folder if needed. These are maintainer commands; ordinary users start by chatting with their approved agent.

## Guide-only revision: beta.2

Added the repository address and a direct ZIP download link to the Get started page in both HTML and PDF. Runtime code and skills are unchanged from beta.1; their earlier test evidence still applies. The revised guide passed layout and clickable PDF-link checks. Pages 1–2 were visually inspected; rendered pages 3–12 match the previously reviewed pages byte-for-byte. All 17 Python tests and the browser checks were rerun and passed.
