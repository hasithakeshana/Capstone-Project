---
name: quiz-grader
description: Use when writing or reviewing quiz questions, quiz grading, quiz attempts, or best-score logic. Keeps grading deterministic, integer-only and append-only (AC-05, AC-06, NFR-01, NFR-02).
---

# Quiz Grader

## Purpose

Grade quiz attempts deterministically and keep the attempt history. Covers AC-05, AC-06, NFR-01 and NFR-02.

## Guide

1. Question types are MCQ (exactly one correct option) and TRUE/FALSE only. Reject any other type. Reject an MCQ with zero or more than one correct option (AC-05).
2. Score = correct × 100 // total (integer division, rounds down). Use integer arithmetic only. AC-05 examples: 3 of 4 correct → 75%; 1 of 3 correct → 33%. Project decision; see `specs/app_spec.md` → Project Decisions.
3. Partial credit per question is an Open Question in `specs/quiz-engine_spec.md`. Do not decide it in code.
4. Same answers → same score every time (DR-7). Do not use randomness or time in grading.
5. Store every attempt with a timestamp (AC-06). Attempts are append-only: no update or delete (NFR-02, DR-9).
6. Best score = the highest score among the learner's attempts on that quiz. A lower later attempt does not lower it. The later attempt is still recorded (DR-8).
7. A learner attempts a quiz only when enrolled in its course. Not signed in → rejected.
8. A learner sees only their own attempts (NFR-08). No user can set or change a quiz score (NFR-08).
9. Instructors add questions only to a DRAFT course. Question changes on a PUBLISHED course are rejected (`specs/quiz-engine_spec.md`).

## Check for

- Float values or any division that returns a float.
- Attempts that can be updated or deleted.
- Non-deterministic grading (randomness, time, dict ordering).
- Best-score logic that keeps the latest attempt instead of the highest.
- Attempts saved without a timestamp.
- Question types other than MCQ and TRUE/FALSE accepted.

## Tests to write

- All correct → 100%: `test_ac05_…`.
- All wrong → 0%: `test_ac05_…`.
- 3 of 4 correct → 75%: `test_ac05_…`.
- 1 of 3 correct → 33%: `test_ac05_…`.
- TRUE/FALSE answered wrong → incorrect: `test_ac05_…`.
- MCQ wrong option → incorrect: `test_ac05_…`.
- Same answers in two attempts → same score: `test_ac05_…`.
- MCQ with two correct options rejected: `test_ac05_…`.
- Attempt 50% then 75% → best 75%, both kept: `test_ac06_…`.
- Attempt 75% then 50% → best stays 75%, new attempt recorded: `test_ac06_…`.
- Attempt carries a timestamp: `test_ac06_…`.
- Edit or delete of an attempt rejected: `test_nfr02_…`.
- Another learner's attempts rejected: `test_nfr08_…`.

Tag every test as described in `tests/CLAUDE.md`.

## References

- `specs/quiz-engine_spec.md` (AC-05 and AC-06).
- Invariants INV-5, INV-6 and INV-7 in `specs/app_spec.md`.
