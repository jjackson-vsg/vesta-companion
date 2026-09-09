# Security model

Vesta Companion is an instruction and file kit, not a sandbox. The chosen app, OS and connected services enforce access. Keep approval controls enabled and grant only the required folders and read capabilities. Local files may be processed by cloud models under the selected service's terms.

Core runtime dependencies: none. The optional helper is Python standard library; HTML uses browser APIs only. No telemetry, remote scripts, external fonts, network requests or embedded model credentials. No third-party skill code is bundled. Agent Skills is a file-format convention, not a security certification.

All public examples are fictional. Personal state is ignored by Git, and packaging uses a committed explicit file allowlist. Ignore rules are not protection from manual uploads, tracked history, screenshots or unsafe third-party tools. Never upload your populated folder as a support attachment. Share a minimal fictional reproduction.

Skill vetting: read complete instructions and referenced scripts, inspect access and network behaviour, test successful and adversarial cases, record review date/version and rerun when changed. A locally modified or user-created skill is unreviewed until evaluated. AI review or a clean scanner result cannot guarantee harmlessness.

Task imports require matching base revision and exact source hash; conflicts require reconciliation. Browser-rendered text uses textContent, not executable HTML. The file picker only writes a file selected by the user and rechecks it before writing. One active writer remains required: OS/browser APIs do not offer a universal cross-app lock.

Report vulnerabilities privately using the repository owner's established private contact route. Do not put exploitable details, credentials or work data in public issues. Private GitHub vulnerability reporting may depend on repository settings; it is not claimed enabled here.
