# Architecture

The chosen agent app supplies model inference, tool execution, authentication, sandboxing and optional scheduling. The kit supplies shared instructions, local file conventions, nine skills, a guide and an offline task board.

- AGENTS.md / CLAUDE.md: short discovery entry points.
- system/COMPANION.md: common behaviour and persistence contract.
- skills/: canonical Agent Skills-format sources.
- .agents/skills/ and .claude/skills/: generated native wrappers with relative links.
- adapters/: pasteable folder/project instructions for other modes.
- templates/: empty data and reusable file formats; board template contains no user data.
- personal/: ignored and created only on user setup; the sole home for real context.
- examples/: explicitly fictional data and an interactive board demo.
- START-HERE.html and docs/Quick-start.pdf: matching user guide.
- scripts/: optional standard-library helper and maintainer release/guide tools.

No background process, model API, vector store, telemetry or network dependency is required by the core. The browser board can save only to a user-selected handle, otherwise it downloads an edit envelope for explicit import. Task files are revisioned and hashed; stale imports cannot silently replace current tasks. This is optimistic conflict detection, not universal locking; one active writer is required.

Public packaging is allowlist based. User files are never package inputs. .work and dist are ignored build outputs; the initial Git history remains separate from any live assistant.
