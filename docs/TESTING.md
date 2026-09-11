# Test evidence

Version: 1.1.0
Checked: 2026-09-11
Status: additive workflow release; prior scoped app evidence is retained and limitations remain explicit.

## Executed checks

| Check | Actual result |
|---|---|
| Python standard-library suite | 28 tests passed (27-test full run plus the new site-link test and repeated site checks): safe upgrade preservation, additive vault setup, metadata/date substitution, existing notes/config preservation, idempotent setup, persistent imports, revision/hash conflicts, removal refusal, malformed data, locking, traversal, HTML escaping, optional settings and release/site isolation. |
| Offline task board in headless Microsoft Edge | Passed adding, editing, filtering, completion, export format, unsaved warnings, responsive layout and script-tag display as plain text. No HTTP requests observed. |
| Selected-file saving | Save/read-back, rejection of changed source files, locking of editing during a save, exact-byte BOM hashing, strict document fields and oversized-save refusal passed. The OS picker and file handle were mocked; the board's real application code ran. |
| User guide | 13 A4 PDF pages generated from the shipped HTML. All pages rendered and visually reviewed; layout checks found no content/footer overlap. Mobile HTML checked for horizontal overflow. |
| Public packaging | Explicit reviewed allowlist. Tests confirm private sentinel files never enter the ZIP, unsafe paths are rejected and unchanged inputs produce identical archive bytes. Release build verifies every archive entry against the SHA-256 manifest. |
| Extracted release smoke check | The actual ZIP was extracted into a fresh temporary folder. Setup created empty personal state and rendered the board successfully. |
| Dependency review | Original core instructions and code; no third-party skill code, runtime bundle, installer, telemetry or remote asset dependencies. Maintainer PDF/browser checks use an already installed Playwright and Edge. |

These results are local technical evidence, not an independent security audit or proof of model compliance. The browser OS permission prompt was not exercised. Automated checks used fictional inputs; the separate user-reported Outlook check below used a live connection.

## User-reported acceptance results

Reported 2026-09-10 against beta.3. The v1.0 core helper and board behaviour are unchanged. Reports are supplied by the maintainer; the release agent did not independently observe the signed-in sessions. App build numbers were not supplied.

| Reported check | Result and scope |
|---|---|
| Codex desktop / Windows local start | Initial command launch failed with Windows error 1907; update/restart did not resolve it. An environment-specific workaround allowed local context retrieval. This does not verify normal protected setup or establish a kit fix. |
| Codex Outlook email summary | Relevant messages and later corrections were incorporated; answered items were distinguished. This was an email-only check, not a complete calendar/Teams briefing. |
| Codex local persistence | Briefing and journal were saved and read back successfully. |
| Codex mailbox boundary | No sending, moving, deletion or marking read was reported. |
| Claude Code cold start and customisation | Missing profile triggered guided setup; assistant-name change was saved to the personal profile without fabricated fields. |
| Claude Code unavailable Microsoft 365 | Enterprise application assignment blocked sign-in. The assistant correctly stated no reachable email/calendar/Teams tools and did not fabricate a summary. |

Calendar, live Teams, attachments, connector writes, broad sandbox enforcement, adversarial app behaviour, a fresh-chat cross-app round trip, native browser permission UI, a personal-skill end-to-end run and a separate timed nontechnical pilot remain unverified. Connector writes are not part of the read-only briefing workflow. The maintainer accepted these limits for stable-core promotion; [V1-ACCEPTANCE.md](V1-ACCEPTANCE.md) records the decision.

An oversized retrieval response was truncated in the reported email session; compact inspection of the retained response recovered coverage. No universal retrieval-efficiency claim is made. A local Windows account/policy issue remains unresolved. No repair commands or reduced-isolation settings are shipped or recommended; [TROUBLESHOOTING.md](TROUBLESHOOTING.md) provides bounded guidance.

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

The published beta.2 and beta.3 ZIPs passed a local Windows upgrade rehearsal with fictional personal state. The original folder and all pre-existing authoritative personal files retained identical bytes; new starter files were added, the task/status survived board regeneration and a recovery copy matched. A new regression test covers the same preservation boundary. This is a file-level check, not signed-in app or human-pilot evidence. All 25 tests passed locally after adding this regression. The previous beta.3 release remains available unchanged; its immutable assets are retained.

## V1.0 final technical checks

All 25 local tests and the browser suite passed on the v1.0 candidate. All twelve PDF pages were rendered: changed pages 1, 3, 6, 11 and 12 were visually checked; pages 2, 4, 5, 7, 8, 9 and 10 matched the previously reviewed PDF renders. Layout, public-content and document-link checks passed. The release remains limited to reviewed public files and contains no account details or raw user test content.

## V1.1 workflow expansion and upgrade check

Twelve instruction workflows and five templates were added without changing the core task helper, board source, personal/ layout or JSON schema. All 21 skills passed metadata validation; tests verify index/native discovery and referenced local documents. A small fictional reasoning walkthrough covers corrected/capped inbox evidence, approved-only report candidates and missing persona assumptions; see WORKFLOW-CHECKS.md. These are release-assistant walkthroughs, not independent or live app evaluations.

The actual published v1.0.0 ZIP was verified against its manifest, extracted and populated with fictional profile, knowledge, custom-skill and task state. After copying personal/ to a clean v1.1 candidate and running additive setup, every authoritative personal file retained identical bytes, the original folder was unchanged and the waiting task/revision survived board regeneration. Existing vault conventions were preserved.

All thirteen guide pages were rendered and visually reviewed. Browser checks passed; hosted Markdown documentation links are rewritten to the public repository and covered by a regression test. No new runtime, legacy workspace, framework, private context or connector configuration is included. Live connector and native OS-picker limits above remain unchanged.
