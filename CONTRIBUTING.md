# Contributing

Use fictional inputs only. Never commit personal/, populated task boards, work messages, customer details, credentials, private URLs, screenshots of live accounts or internal strategy.

Canonical skills are in skills/. Generated .agents/skills and .claude/skills wrappers are built by scripts/build.py. Personal skills belong in personal/skills and are never upstream contributions by default. Keep the core free of package dependencies and network code. User setup must not require a terminal.

Run Python standard-library tests with python -m unittest discover -s tests. Run python scripts/build.py --check for structural checks and python scripts/build.py --package for an allowlisted ZIP after PDF generation. Browser tests and PDF rendering use a maintainer-provided Playwright install (see docs/TESTING.md). The user release contains no development tools that download dependencies.

Review docs/SECURITY.md, docs/RELEASING.md and docs/TESTING.md. Changes to behaviour, access and privacy need explicit review. Never run untrusted skills or source documents as instructions. Preserve Apache 2.0 licensing and attribution. Submit a proposed change; do not publish on behalf of a user without authorisation.
