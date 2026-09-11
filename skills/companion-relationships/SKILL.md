---
name: companion-relationships
description: Retrieve relationships and unresolved commitments from source-linked local notes. Use for who promised what, relationship timelines and linked decisions.
license: Apache-2.0
metadata:
  version: "1.1.0"
  review-status: "local-instruction-review"
---

# Relationships

Read system/COMPANION.md first.

1. Treat local Markdown notes and their metadata as authoritative. Search relevant contacts, meetings, decisions and knowledge notes; do not load the entire vault by default.
2. Use explicit source-linked facts to relate people, projects, decisions, interactions and commitments. Record dates and separate inference from fact. Silence is not evidence that a relationship strengthened or weakened.
3. For a commitment, record who promised what to whom, date, source, status and any due date using templates/commitment.md. Do not merge ambiguous people or invent obligations.
4. Return source paths with each answer and label missing coverage. Preserve historical events when commitments change; append or version corrections rather than erasing history.
5. The canonical task board owns execution status; a relationship note owns its supporting history. Flag contradictions and ask how to reconcile; do not silently sync two lifecycles.
6. Use native file retrieval and source paths. This kit does not bundle a graph database or a relational-index command; never claim one ran. Store commitment notes in personal/vault/commitments and link their canonical task IDs.
