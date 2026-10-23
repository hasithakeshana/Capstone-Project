---
name: course-state-validator
description: Use when writing or reviewing code that creates a course, changes its state (publish, unpublish, archive), or edits a course's content. Keeps the course lifecycle correct (AC-02, AC-04, AC-08, NFR-08).
---

# Course State Validator

## Purpose

Keep the course lifecycle correct. Covers AC-02, AC-04, AC-08 and NFR-08.

## Guide

1. Read the transition table in `specs/app_spec.md` → Course Lifecycle. It is the only source of allowed moves.
2. Allowed moves: DRAFT → PUBLISHED, PUBLISHED → UNPUBLISHED, UNPUBLISHED → ARCHIVED. No other move exists.
3. Change a course's status only through the state machine in `src/domain/`. Services and controllers call it. They never assign the status field directly.
4. Any other move raises `InvalidCourseStateException`. The stored state stays unchanged.
5. Only an Admin may publish, unpublish or archive. Check the role at the controller layer.
6. A new course starts in DRAFT. Store the creating instructor as its owner.
7. A PUBLISHED course cannot be changed (title, description, category, difficulty, modules, lessons) until it is UNPUBLISHED (NFR-08). Reject the edit and leave the course unchanged.
8. Do not add states. ARCHIVED has no allowed exit.

## Check for

- Status assigned outside `src/domain/`.
- Wrong exception name. It must be `InvalidCourseStateException`.
- Missing role check on publish, unpublish or archive.
- Edits to a PUBLISHED course that are not rejected.

## Tests to write

- One test per allowed transition (3): `test_ac08_…`.
- At least 3 forbidden moves from AC-08: UNPUBLISHED → PUBLISHED, DRAFT → ARCHIVED, PUBLISHED → ARCHIVED. Also ARCHIVED → any state.
- Publish, unpublish and archive rejected for instructor and learner: `test_ac04_…`.
- New course starts in DRAFT with the owner stored: `test_ac02_…`.
- Edit to a PUBLISHED course rejected: `test_nfr08_…`.

Tag every test as described in `tests/CLAUDE.md`.

## References

- `specs/app_spec.md` → Course Lifecycle (section 4); Invariants INV-1 and INV-2.
- `specs/catalog_spec.md`, `specs/course-authoring_spec.md`.
- Test naming: process rule PR-learnlab-03.
