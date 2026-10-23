---
description: Spec-Is-Truth flow. Propose a spec edit as a diff, wait for approval, update the specs and traceability, then list what must be regenerated.
argument-hint: short description of the change
---

# Spec change

Change: $ARGUMENTS

Never edit code or tests in this command.

## Steps

1. Find the affected specs. Search `specs/app_spec.md` and `specs/*_spec.md` for the terms in the change. List each file and section.
2. Propose the spec edit as a diff. Show the diff, then stop and wait for approval.
3. After approval, edit the spec. Also update the affected sprint PRD in `specs/sprints/` and `specs/requirements-traceability.md`.
4. List the code and tests that must be regenerated. For each one, name the AC or NFR it covers.
5. Suggest the next step: `/implement-ac AC-NN` for a single AC, or the harness `/change` command for a story.

Do not commit unless the user asks.

## Expected output

- The affected spec files and sections.
- The approved diff.
- The list of files to regenerate, with their AC or NFR ids.
