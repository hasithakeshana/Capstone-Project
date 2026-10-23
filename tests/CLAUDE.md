# Backend tests (tests/)

- Folders mirror `src/`: `domain/`, `services/`, `controllers/`, `repositories/`, `architecture/`.
- Names: `test_acNN_<behaviour>` for ACs, `test_nfrNN_<behaviour>` for NFRs, `test_arch_<behaviour>` for architecture rules.
- Each test has `@pytest.mark.ac("AC-NN")` (or the NFR/architecture id) and a docstring that starts with the id.
- Red first: write the failing test before the code it tests.
- Never delete, skip or weaken a test to make it pass. Fix the code under test.
