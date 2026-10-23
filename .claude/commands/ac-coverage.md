---
description: Prove every acceptance criterion has at least one AC-tagged test. Writes reports/ac-coverage.md. No AI.
argument-hint: [AC-NN, optional: show only that AC]
---

# AC coverage

Filter: $ARGUMENTS (empty means all ACs).

## Steps

1. Run `bash scripts/sprint_close.sh --ac-only`. It writes `reports/ac-coverage.md` as a table: AC | test files | count | status. It does not use AI.
2. Show the table. If a filter was given, show only that AC's row.
3. If any row is MISSING, list those ACs. Then ask: "Run the tester agent for these ACs?"
4. Run the tester agent only after the user agrees. Use `/implement-ac AC-NN` for a single AC, or ask the tester agent for all missing ACs in one step.

## Expected output

- The coverage table, or the filtered row.
- The count of MISSING ACs.
