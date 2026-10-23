# Backend tests (tests/)

- Folders mirror `src/`: `domain/`, `services/`, `controllers/`, `repositories/`, `architecture/`.
- Names: `test_acNN_<behaviour>` for ACs, `test_nfrNN_<behaviour>` for NFRs, `test_arch_<behaviour>` for architecture rules.
- Each test has `@pytest.mark.ac("AC-NN")` (or the NFR/architecture id). Its docstring starts with `AC-NN (E1-S1-ACn): …`.
- Red first: write the failing test before the code it tests.
- Never delete, skip or weaken a test to make it pass. Fix the code under test.

## Required unit test areas (capstone test suite)

- Quiz auto-grading — `tests/domain/` (AC-05, AC-06)
- Progress aggregation — `tests/domain/` (AC-07, AC-09)
- Role-boundary checks — `tests/controllers/`: for each protected route, the wrong role gets 403 and no token gets 401 (NFR-04, `test_nfr04_…`)
- Course state transitions — `tests/domain/` (AC-08): every allowed move + at least 3 forbidden

At least 20 unit tests in total across sprints.
