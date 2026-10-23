# Post-mortems

A post-mortem records one real problem: what happened, why, what changed, and how we stop it from coming back.

## Rule: check the environment first

Before you touch code, check the environment in this order. Most "code" failures are environment failures.

1. Versions: Python, Node, uv, npm, and the tool that failed.
2. Dependencies: lock files present and in sync (`uv.lock`, `frontend/package-lock.json`).
3. Environment variables: names set, values not printed.
4. Ports: 8000 (API) and 5173 (Vite) free or in use by the right process.
5. Database and migrations: SQLite file present, migrations applied in order.
6. Browsers: Playwright browsers installed for the version pinned.
7. CI image: the runner OS and tool versions match what the job expects.

Write down each check and its result, even when it passes.

## Template

Copy this block into a new file named `YYYY-MM-DD-short-title.md`.

```markdown
# <Title>

- **Date:** YYYY-MM-DD
- **Sprint:** N
- **Symptom:** What was seen, in one or two lines. Include the exact error text.

## Environment checks (in order)

- Versions:
- Dependencies:
- Environment variables:
- Ports:
- Database and migrations:
- Browsers:
- CI image:

## Root cause

What was actually wrong, and how it was confirmed.

## Fix

The commit or PR that fixed it.

## Prevention

The rule, hook or skill added so this does not come back. Name the file.

## Lesson

One sentence the next person can use.
```
