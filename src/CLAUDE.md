# Backend (src/)

Run from the repo root: `uv run pytest -x -q`, `uv run ruff check --fix .`, `uv run mypy src/`, `uv run lint-imports`.

- Layers: controllers → services → repositories → domain; `core/` for config and logging. Imports flow one way only. See [docs/architecture.md](../docs/architecture.md).
- Logs are structured JSON. Every line for one request carries the same correlation id (NFR-06).
- Never log learner PII (email, phone, performance data) in plain text (NFR-03).
- `GET /health` returns 200 within 1 second of startup (NFR-07).
- Declare `pytest-cov` and `import-linter` as dev dependencies in `pyproject.toml`.
- Schema changes go through a new migration only (see [migrations/CLAUDE.md](../migrations/CLAUDE.md)).
- Seed data creates course states through the domain state machine, never by assigning status directly (course-publish-gate).
