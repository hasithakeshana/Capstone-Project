# Architecture Constitution

Cross-sprint invariants this system must never violate — the rules a design
amendment is checked against every sprint, not just the rules for right now.
Human-owned. Edit this file like code: a change to an invariant is itself an
architectural decision and should go through normal PR review.

First authored at sprint-1 design approval. Revisit at each sprint boundary —
`/design --delta`'s design-delta rubric checks every amendment against the
`## Invariants` list below as a hard criterion; violating one fails the
amendment regardless of its weighted score.

## Invariants

- INV-1 (AC-08, DR-1): A course changes state only through DRAFT → PUBLISHED → UNPUBLISHED → ARCHIVED; any other move raises InvalidCourseStateException.
- INV-2 (NFR-08): A PUBLISHED course cannot be changed unless it goes through an unpublish transition.
- INV-3 (AC-01, AC-04, DR-3): A learner can enroll only in a PUBLISHED course.
- INV-4 (AC-01, DR-4): A learner has at most one enrollment per course.
- INV-5 (NFR-01, DR-6): Quiz scores are integer percentages; no floating-point math.
- INV-6 (NFR-02, DR-9): Quiz attempts, lesson completions, and enrollments are never edited or deleted.
- INV-7 (AC-06, DR-8): The best quiz score is kept, and each attempt keeps its timestamp.
- INV-8 (NFR-03): Learner PII is never written to logs in plain text.
- INV-9 (NFR-08, DR-11): A learner cannot access another learner's progress; instructors see only aggregated band counts (AC-09); admins see enrollment analytics (AC-10).
- INV-10 (NFR-08, DR-12): An instructor cannot grade their own courses' learners.
- INV-11 (NFR-04, DR-10): Each role is checked at the controller layer.
- INV-12 (NFR-05): Database migrations are append-only.

## Amendment History

- Sprint 1: initial invariants from app_spec.md
