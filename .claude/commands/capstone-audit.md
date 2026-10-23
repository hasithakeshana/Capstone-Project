---
description: Check the repo against the capstone marking checklist. Read-only except docs/capstone-audit.md.
argument-hint: [optional sprint number]
---

# Capstone audit

Scope: $ARGUMENTS (empty means the whole repo).

## Steps

1. Read `scripts/capstone_checklist.md`.
2. For each checklist line, check the repo for evidence. Do not change any repo file.
3. Write `docs/capstone-audit.md` as a table: Item | Evidence path | ✅ / ⚠️ / ❌ | Fix.
4. Show the counts of ✅, ⚠️ and ❌, and the top 5 fixes.

## Expected output

- The path of `docs/capstone-audit.md`.
- The counts of ✅, ⚠️ and ❌.
- The top 5 fixes.
