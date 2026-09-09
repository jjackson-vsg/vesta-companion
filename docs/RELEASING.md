# Release procedure

1. Work in this clean public project, never a populated personal assistant folder. Review git status and all proposed content, including binary metadata. Preserve the existing Apache 2.0 licence.
2. Run all structural, Python and browser tests. Generate START-HERE.html and docs/Quick-start.pdf from the same guide content. Render and visually inspect every PDF page. Record actual results and limitations in docs/TESTING.md.
3. Inspect PUBLIC-FILES.txt. Only exact listed files may enter the release or initial public commit. No globs, symlinks, traversal paths, private folders, caches or hidden authentication state. The packager fails on unlisted tracked files except the allowlist itself.
4. Review every listed file for personal, proprietary and confidential information; use secret scanning as an additional check. Scan the extracted ZIP and PDF text. Generic safety instructions and fictional tasks are permitted; internal work is not. Record hashes and provenance. Do not label this an independent security audit.
5. python scripts/build.py --package creates dist/vesta-companion.zip, its checksum and a file-hash manifest. The archive has one vesta-companion/ top folder and no Git history or personal data.
6. Obtain explicit authorisation for the exact public commit and release payload, then push only the reviewed files. Create the initial beta as a GitHub prerelease. Upload the exact reviewed ZIP, PDF, checksums and manifest. Never recreate a released version with different bytes.
7. Prerelease downloads use /releases/download/v0.1.0-beta.1/vesta-companion.zip; GitHub's /releases/latest/download route excludes prereleases. Change the README link deliberately for the stable release.
8. Verify download URLs and hashes after publication. Keep previous releases available. A newer ZIP is extracted alongside an existing installation, never over personal data.

No automatic public publishing is installed. User authorisation and exact-artifact review remain the final release step. Promotion to stable requires signed-in cross-app/M365 checks and a representative nontechnical pilot; do not manufacture these results.
