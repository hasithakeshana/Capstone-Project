# LearnLab — Test-Driven Development

*Version 1.*

## 1. Approach

We build each feature with red → green → refactor:

- **Red:** write a test for one acceptance criterion. It fails, because the behaviour does not exist yet.
- **Green:** write the simplest code that makes the test pass.
- **Refactor:** tidy the code, with the tests still passing.

Every acceptance criterion (AC) needs at least one test that references its AC-NN id (the capstone doc). Agents write the tests and the code. We review the result.

## 2. Commit Convention

Each step is a separate commit, made by an agent:

- `test(AC-NN)`: the failing test (red).
- `feat(AC-NN)`: the code that makes it pass (green).
- `refactor(AC-NN)`: cleanup with no change in behaviour.

The commit history is the evidence of red → green → refactor. At least 10 test files are committed across history, showing red → green → refactor (the capstone doc).

The harness also makes one group commit per completed story group (feat: implement group X); the test(AC-NN), feat(AC-NN) and refactor(AC-NN) commits come from the implementers inside that group.

## 3. Test Naming

Every test carries its exact AC id in the form "AC-NN" so it can be found by searching for the id:
- pytest: the function name starts with test_acNN_ (for example test_ac05_...), the test has an ac marker carrying the AC id, and the docstring starts with "AC-05:". The ac marker is registered in the project configuration file (pyproject.toml) with the description "acceptance criterion id".
- Vitest: the describe or test title starts with "AC-05 ...".
- Playwright: the test title starts with "AC-05 ...".

Tests for behaviour without an AC id use the user journey or NFR name in the same way (for example test_browse_... with "Browse:" in the docstring; test_nfr03_... with "NFR-03:" in the docstring; architecture tests test_arch_... with "Architecture:").

The names here are examples; the real names are set when the tests are written.

## 4. Test Levels

| Level | Tool | Folder |
|---|---|---|
| Domain unit | pytest | tests/domain |
| API | pytest | tests/controllers |
| Service unit | pytest | tests/services |
| Repository | pytest | tests/repositories |
| Architecture | import-linter + pytest | tests/architecture |
| UI unit | Vitest | frontend/ |
| End-to-end (UI) | Playwright | e2e/, with screenshot snapshots |

Test folders mirror src/ folders (the harness TDD gate expects a matching test for each source file).

## 5. Coverage

- Minimum 80%, enforced by the harness coverage ratchet.
- Artefacts: reports/coverage.xml (backend, pytest-cov) and reports/lcov.info (frontend, Vitest).
- The capstone doc requires at least 20 unit tests with a coverage artefact.

## 6. Worked Example: AC-05 Quiz Auto-Grading

**Acceptance criterion:** Quiz supports MCQ (single correct) and TRUE / FALSE question types; quizzes are auto-graded by a deterministic rule.

**Failing test (red).** A test named in the form test_ac05_..., with the ac marker set to AC-05 and a docstring starting "AC-05:", describes one scenario from the quiz engine spec. For example: Given a quiz with 4 questions and 3 answered correctly, When the attempt is submitted, Then the score is 75%. The test fails, because no grading rule exists yet.

**Making it pass (green).** The simplest change is a grading rule in the domain layer. It counts correct answers and turns the count into an integer percentage. It does not use floating-point math (NFR-01). The test passes.

**Refactor.** The rule is moved to its own domain file, the quiz grading rule in Section 5 of the architecture doc. The MCQ and TRUE / FALSE checks are kept in one place, so the same answers always give the same score (DR-7). The tests still pass.

**Commit hashes.** To be completed with real commit hashes after sprint 3.
