# Domain (src/domain/)

- Pure Python: standard library only. No FastAPI, SQLAlchemy or imports from other layers.
- Integer maths only. Quiz scores and percentages never use floats (NFR-01).
- Planned rule files (see [docs/architecture.md](../../docs/architecture.md) §5): course state rule, enrollment policy, quiz grading rule, progress calculation rule, access policy.
- Course state changes go only through the course state machine. Any other move raises `InvalidCourseStateException` (AC-08).
- Every rule has an AC-tagged test in `tests/domain/`.
