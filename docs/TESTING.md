# Test evidence

Version: 0.1.0-beta.3
Checked: 2026-09-10
Status: local technical checks passed; signed-in app and Microsoft 365 pilot pending.

## Executed checks

| Check | Actual result |
|---|---|
| Python standard-library suite | 24 tests passed: additive vault setup, metadata/date substitution, existing notes/config preservation, idempotent setup, persistent imports, revision/hash conflicts, removal refusal, malformed data, locking, traversal, HTML escaping, optional settings and release/site isolation. |
| Offline task board in headless Microsoft Edge | Passed adding, editing, filtering, completion, export format, unsaved warnings, responsive layout and script-tag display as plain text. No HTTP requests observed. |
| Selected-file saving | Save/read-back, rejection of changed source files, locking of editing during a save, exact-byte BOM hashing, strict document fields and oversized-save refusal passed. The OS picker and file handle were mocked; the board's real application code ran. |
| User guide | 12 A4 PDF pages generated from the shipped HTML. All pages rendered and visually reviewed; layout checks found no content/footer overlap. Mobile HTML checked for horizontal overflow. |
| Public packaging | Explicit reviewed allowlist. Tests confirm private sentinel files never enter the ZIP, unsafe paths are rejected and unchanged inputs produce identical archive bytes. Release build verifies every archive entry against the SHA-256 manifest. |
| Extracted release smoke check | The actual ZIP was extracted into a fresh temporary folder. Setup created empty personal state and rendered the board successfully. |
| Dependency review | Original core instructions and code; no third-party skill code, runtime bundle, installer, telemetry or remote asset dependencies. Maintainer PDF/browser checks use an already installed Playwright and Edge. |

These results are local technical evidence, not an independent security audit or proof of model compliance. The browser OS permission prompt was not exercised, and no live Microsoft 365 messages were read for these checks.

## Acceptance before v1.0

Use [V1-ACCEPTANCE.md](V1-ACCEPTANCE.md) for the bounded release gate: one actual app/colleague session, persistence and task-board save checks, basic boundaries and a safe upgrade. Declare exactly which apps and connectors were verified. Broader combinations can remain explicitly unverified and continue after v1.0; known data-loss or unsafe-action defects still block release.

The scenario expectations in [SKILL-REVIEW.md](SKILL-REVIEW.md) remain useful for broader coverage. Do not describe any app or connector check as passed without evidence.

## Reproduce the technical checks

Maintainers can run:

```text
python -m unittest discover -s tests -v
python scripts/build.py --assets
python scripts/build_site.py
node tests/browser.cjs
node scripts/render-guide.cjs
python scripts/build.py --check --package
```

Python 3.10+ suffices for the helper and release tests. The browser and PDF scripts require an already installed Playwright module and Microsoft Edge, and do not download dependencies. Set NODE_PATH to that module's parent folder if needed. These are maintainer commands; ordinary users start by chatting with their approved agent.

## Guide-only revision: beta.2

Added the repository address and a direct ZIP download link to the Get started page in both HTML and PDF. Runtime code and skills are unchanged from beta.1; their earlier test evidence still applies. The revised guide passed layout and clickable PDF-link checks. Pages 1–2 were visually inspected; rendered pages 3–12 match the previously reviewed pages byte-for-byte. All 17 Python tests and the browser checks were rerun and passed.

## Beta.3 scope and additional checks

- New vault starter folders, conventions and small frontmatter templates. Setup adds missing files and never replaces existing HOME notes, journal entries or Obsidian settings.
- Optional Claude approval template is valid JSON, has no auto-allow rules and is not activated by setup. Its signed-in behaviour remains a pilot check.
- Hosted guide/demo builds contain exactly four public files. Tests reject unexpected leftovers and show that a fictional private sentinel is not uploaded. The hosted demo hides local-file controls and uses temporary fictional tasks.
- The repository has pinned GitHub Actions workflows for Windows/Linux core checks on pull requests. Pages deployment is limited to reviewed public assets from main; there is no automated release publication.
- The guide and README link to the organisation Releases page, so they do not lock new readers to one beta.
- Full signed-in model behaviour, connector access and a timed nontechnical setup pilot remain outstanding.

Beta.3 guide verification: all twelve pages were rendered. Pages 1, 2, 8, 11 and 12 were visually inspected; the other seven rendered pages match beta.2. Browser checks also passed for the public landing page and interactive fictional demo, including hidden file controls and mobile layout.

## V1 preparation: update guidance and regression coverage

The published beta.2 and beta.3 ZIPs passed a local Windows upgrade rehearsal with fictional personal state. The original folder and all pre-existing authoritative personal files retained identical bytes; new starter files were added, the task/status survived board regeneration and a recovery copy matched. A new regression test covers the same preservation boundary. This is a file-level check, not signed-in app or human-pilot evidence. All 25 tests passed locally after adding this regression. The published beta.3 remains unchanged while acceptance proceeds.
