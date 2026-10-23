# LearnLab

LearnLab is a lightweight learning management system for an internal team. Learners browse and enroll in published courses, work through lessons, and take auto-graded quizzes. Instructors author courses and see learner progress. Admins publish courses and monitor enrollment.

Roles: **learner**, **instructor**, **admin**.

- Business case: [docs/business-case.md](docs/business-case.md)
- Application spec: [specs/app_spec.md](specs/app_spec.md)
- Architecture: [docs/architecture.md](docs/architecture.md)
- Agents, skills, commands and hooks: [AGENTS.md](AGENTS.md)

## Quick start

Prerequisites:
- uv, with Python 3.12
- Node 22

The single run command and seed accounts are added in sprint 1 (FR-31).

## Tests

```bash
uv run pytest          # backend
npm test               # frontend (run from frontend/)
npx playwright test    # end-to-end (run locally; snapshots are generated on the developer's OS)
```

## Project workflow

- Work is built with the Claude Harness Engine: `/build` for sprint 1, then `/sprint` for sprints 2 and 3.
- No direct commits to `main`. Every change goes through a pull request.
- Every pull request gets a Claude review in CI (`.github/workflows/claude-review.yml`).
