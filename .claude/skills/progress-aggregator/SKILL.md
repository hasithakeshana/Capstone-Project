---
name: progress-aggregator
description: Use when writing or reviewing lesson completion, course progress percentages, or instructor progress bands. Keeps progress integer-only, never double-counted, and private per learner (AC-07, AC-09, NFR-01, NFR-08).
---

# Progress Aggregator

## Purpose

Compute correct progress percentages and instructor band counts. Covers AC-07, AC-09, NFR-01 and NFR-08.

## Guide

1. A learner can mark a lesson complete only in a course they are enrolled in (AC-07, AC-01).
2. Store one completion per learner and lesson. Marking the same lesson twice must not add a second record or change progress.
3. Completions are append-only. Do not add update or delete methods (NFR-02, DR-9).
4. Progress % = completed lessons ÷ total lessons, as an integer percentage. Use integer arithmetic only. Never use float (NFR-01, DR-6).
5. Percentages round down: percent = completed * 100 // total (integer division). Project decision; see `specs/app_spec.md` → Project Decisions.
6. A course with no lessons shows 0% progress. This is a project decision in `specs/progress-tracker_spec.md` → Business Rules. Do not divide by zero.
7. Bands for instructors: 0–25%, 25–50%, 50–75%, 75–100% (AC-09). Each learner counts in one band.
8. Bands: 0 ≤ p < 25, 25 ≤ p < 50, 50 ≤ p < 75, 75 ≤ p ≤ 100. Project decision; see `specs/app_spec.md` → Project Decisions.
9. Instructors receive band counts only, never learner identities or individual progress (AC-09, DR-11). Learners and anonymous users are rejected (NFR-04).
10. A learner sees only their own progress. A request for another learner's progress is rejected (NFR-08).

## Check for

- Float use, including any division that returns a float.
- Boundary values 0 and 100 handled wrongly.
- Any path where one learner can read another learner's progress.
- Double counting when a lesson is marked twice.
- Band responses that include learner ids.
- Completions that can be edited or deleted.

## Tests to write

- 1 of 4 lessons → 25%; 0 of 4 → 0%; 4 of 4 → 100%: `test_ac07_…`.
- Marking the same lesson twice counts once: `test_ac07_…`.
- Completion rejected when not enrolled: `test_ac07_…`.
- Band counts for 10% and 60% learners (AC-09 example): `test_ac09_…`.
- Learner request for band counts rejected: `test_ac09_…`.
- Learner cannot read another learner's progress: `test_nfr08_…`.
- Progress returns an integer type: `test_nfr01_…`.
- Course with 0 lessons → 0%: `test_ac07_…` (scenario added to AC-07).
- 1 of 3 lessons → 33%: `test_ac07_…`.
- Band boundaries: 0 → band 1, 25 → band 2, 50 → band 3, 75 → band 4, 100 → band 4: `test_ac09_…`.

Tag every test as described in `tests/CLAUDE.md`.

## References

- `specs/progress-tracker_spec.md`.
- `specs/instructor-workbench_spec.md`.
- Invariants INV-8 and INV-9 in `specs/app_spec.md`.
