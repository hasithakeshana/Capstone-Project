---
name: enrollment-deduper
description: Use when writing or reviewing code that enrolls a learner in a course, handles enrollment retries or double submits, or touches enrollment records. Enforces one enrollment per learner and course (AC-01, AC-04, NFR-02).
---

# Enrollment Deduper

## Purpose

Allow one enrollment per learner per PUBLISHED course, and keep it correct when a request is retried. Covers AC-01, AC-04 and NFR-02.

## Guide

1. Enrollment is allowed only when the course is PUBLISHED. Reject DRAFT, UNPUBLISHED and ARCHIVED courses, and save no enrollment. Course state rules live in the course-state-validator skill; here only check the state.
2. Only learners enroll. Reject instructors, admins and anonymous users at the controller layer (NFR-04).
3. Enforce uniqueness in two places:
   - a domain check in `src/domain/` before saving;
   - a database unique constraint on (learner, course), in the enrollment migration (a new migration file, NFR-05).
   The domain check gives the clear error. The constraint stops two requests that race past the check.
4. Retries and double submits: the second request is rejected and exactly one enrollment exists (enrollment_spec.md, AC-01). The spec does not say how a retry is detected. Do not add a request-id scheme without a spec change.
5. Enrollment records are append-only. Do not add update or delete methods, routes or repository calls (NFR-02, DR-9).
6. Never log the learner's email (NFR-03).

## Check for

- No unique constraint on (learner, course).
- Any update or delete on enrollments.
- Enrollment saved for a course that is not PUBLISHED.
- Duplicate error raised but a second row still written.
- Check-then-insert with no constraint behind it.
- Missing role check.

## Tests to write

- First enrollment in a PUBLISHED course succeeds: `test_ac01_…`.
- Second enrollment in the same course is rejected and the count stays 1: `test_ac01_…`.
- Repeated request (retry) leaves exactly one enrollment: `test_ac01_…`.
- DRAFT, UNPUBLISHED and ARCHIVED courses reject enrollment: `test_ac04_…`.
- Instructor and admin enrollment rejected: `test_nfr04_…`.
- Edit or delete of an enrollment rejected: `test_nfr02_…`.

Tag every test as described in `tests/CLAUDE.md`.

## References

- `specs/enrollment_spec.md` (AC-01 scenarios).
- `specs/catalog_spec.md` (AC-04 scenarios).
- Invariants INV-3, INV-4 and INV-6 in `specs/app_spec.md`.
