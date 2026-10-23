# Repositories (src/repositories/)

- Enrollments, lesson completions and quiz attempts are insert-only. Do not add update or delete methods for them (NFR-02, DR-9).
- Access the database through SQLAlchemy only.
- Repositories do not apply business rules. Those live in `src/domain/`.
