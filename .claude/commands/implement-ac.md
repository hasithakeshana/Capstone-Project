---
description: Build or fix one acceptance criterion (AC-NN) outside /auto, with a red test, the minimum code and a domain review.
argument-hint: AC-NN
---

# Implement one AC

Target: $ARGUMENTS (for example `AC-05`).

Never run this command on `main`. Work on a `fix/<name>` branch or the sprint branch.

## Steps

1. Check the branch with `git branch --show-current`. If it is `main`, stop and ask for a branch.
2. Find the AC in its feature spec. `specs/app_spec.md` → Acceptance Criteria lists the file for each AC. Read its Given/When/Then scenarios.
3. Ask the `tester` agent to write the failing test for each scenario, following the `spec-to-test-generator` skill. Each test carries the AC id (PR-learnlab-03).
4. Run the new tests. Confirm they fail for the right reason: the behaviour is missing.
5. Commit: `test($ARGUMENTS): <behaviour>`.
6. Implement the minimum change in the layer the test names. Read the area skill first. The mapping is in `.claude/program.md` → LearnLab → Skill per story area.
7. Run the test suite until the new tests and the existing tests pass. Backend: `uv run pytest -x -q`. Frontend: `npm test`.
8. Commit: `feat($ARGUMENTS): <change>`.
9. Optional: refactor without changing behaviour. Commit `refactor($ARGUMENTS): <change>`, source files only.
10. Ask the matching domain agent to review the change. The mapping is in `.claude/program.md` → Domain review step. Its findings go to `specs/reviews/`.

## Expected output

- The branch name.
- The list of commits: test, feat, and refactor if made.
- Test results: pass and fail counts.
- The path of the review file.

Do not push or merge.
