---
description: Collect sprint N evidence with mechanical steps, stop on blocking problems, update docs once with doc-writer, and list files to commit. Does not push.
argument-hint: sprint number N
---

# Sprint close

Sprint: $ARGUMENTS

## Steps

1. Run `bash scripts/sprint_close.sh $ARGUMENTS`. The mechanical steps use no AI.
2. Show `reports/sprint-$ARGUMENTS-summary.md`.
3. Stop and report if the summary shows any blocking problem:
   - a commit on `main`
   - a commit with no `Co-Authored-By` line
   - coverage below 80%
   - an AC with no test
4. Optional, only if credits allow: run `python scripts/ac_coverage_audit.py` for this sprint's ACs.
5. Call the `doc-writer` agent once for sprint $ARGUMENTS. It updates `docs/harness-integration.md` (the sprint row) and, when needed, `docs/architecture.md` and `docs/knowledge-deposits.md`.
6. List the files to commit with `git status --short`. Do not commit. Do not push.

## Expected output

- The summary path.
- Blocking problems: none, or the list.
- The docs the doc-writer changed.
- The files to commit.
