---
name: companion-development
description: Plan or implement a bounded software change in the selected project, with reviewable edits, appropriate tests and explicit release scope.
license: Apache-2.0
metadata:
  version: "1.1.0"
  review-status: "local-instruction-review"
---

# Development

Read system/COMPANION.md first.

1. Resolve the actual target project and requested outcome. Use companion-projects for ordinary project planning. Do not put application source code into the assistant kit or confuse this folder with the target repository.
2. Read that project's instructions and current state. Preserve uncommitted work. For a substantial change, agree acceptance criteria and a short plan; for a small authorised fix, proceed proportionately.
3. Use the project's existing tools and conventions. Make focused, reviewable edits within authorised scope. Do not install a framework or dependency, run a remote installer, or change permissions merely to get started.
4. Test the intended behaviour and important failure cases using available approved tools. Report actual results, environmental blockers and untested scenarios. A plan or code review is not an executed test.
5. Source code and project tests belong in the selected project. Keep assistant context and handover under personal/, never copy private memory into a public repository. Honour session-only requests.
6. Before a requested push, merge, deployment or release, review the exact destination and payload and confirm that the user's authorisation covers it. A coding request alone does not authorise publication. Stop on changed state or ambiguous outcomes.
7. Summarise the resulting behaviour, evidence, outstanding risks and recovery route. Use an existing approved development framework when the project already requires it; this skill does not bundle or require one.
