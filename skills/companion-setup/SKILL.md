---
name: companion-setup
description: Guide first-time setup and customise the assistant name, profile, language and preferences. Use on first use or when the user asks to set up or personalise Companion.
license: Apache-2.0
metadata:
  version: "1.0.0"
  review-status: "local-technical-review"
---

# companion setup

1. Read system/COMPANION.md. Check personal/profile.md and personal/HANDOVER.md before asking repeated questions. Explain that the assistant name can differ from Vesta Companion.
2. Verify this exact local folder can persist files: with the user's setup request, create personal/setup-check.md containing a harmless test sentence and read it back. If saving fails, stop collecting profile information and explain the available local/manual route.
3. Ask small groups of questions: preferred name and language; assistant name; role and two useful outcomes; timezone and working week; desired tone and level of detail. Optional questions can be skipped. Never ask for passwords, API keys or tenant configuration.
4. Record confirmed answers in personal/profile.md after each step, including setup progress. Keep unanswered values explicitly unset. A user can start useful work before completing the interview.
5. Use scripts/companion.py init if Python is already available; it is additive and preserves existing files. Otherwise use templates/FILE-OPERATIONS.md. It now adds a vault HOME, conventions, starter folders and minimal Obsidian settings without replacing existing notes or settings. Do not require a user terminal or silently install software.
6. Show the person their personal folder and explain local memory, the app's cloud processing, approved-account use and the need for a private location. Offer Obsidian as an optional way to browse personal/vault. No community plugins are installed. Show HOME.md and where a saved note lives. Offer a backup plan through companion-care; record reminder preferences in the handover.
7. Offer a first task: add one real priority, remember a preference, or draft a local daily brief. Explain that Outlook and Teams require separately approved connections and that the core can work without them.
8. Save personal/HANDOVER.md and a journal entry. Mark setup complete only after the profile and first output are read back. End with three natural-language starter prompts and a link to the HTML guide.
9. On later customisation requests, edit personal/profile.md and personal skills only. Preview changes affecting access, safety or schedules before activation.

Success: a saved profile, one useful saved output and a retrieval from a fresh task. No personal content outside personal/.
