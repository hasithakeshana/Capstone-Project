# LearnLab — Test-Driven Development

*Version 1.*

## 1. Approach

We build each feature with red → green → refactor:

- **Red:** write a test for one acceptance criterion. It fails, because the behaviour does not exist yet.
- **Green:** write the simplest code that makes the test pass.
- **Refactor:** tidy the code, with the tests still passing.

Every acceptance criterion (AC) needs at least one test that references its AC-NN id (capstone doc, Section 5.1). Agents write the tests and the code. We review the result.

## 2. Commit Convention

Each step is a separate commit, made by an agent:

- `test(AC-NN)`: the failing test (red).
- `feat(AC-NN)`: the code that makes it pass (green).
- `refactor(AC-NN)`: cleanup with no change in behaviour.

The commit history is the evidence of red → green → refactor (capstone doc, Section 7.3).

## 3. Test Naming

Every test name contains its AC id. Unit and API tests use the form `test_ac05_...`. End-to-end test titles use the form "AC-05 ...". The names are examples here; the real names are set when the tests are written.

## 4. Test Levels

| Level | Tool | Folder |
|---|---|---|
| Domain unit | pytest | tests/domain |
| API | pytest | tests/controllers |
| Architecture | import-linter + pytest | tests/architecture |
| UI unit | Vitest | frontend/ |
| End-to-end (UI) | Playwright | e2e/, with screenshot snapshots |

## 5. Coverage

- Backend coverage uses pytest-cov. Frontend coverage uses Vitest coverage.
- Reports are committed in reports/.
- Minimum coverage: 80%. This number is proposed here. The capstone doc does not set a coverage percentage, so it is an Open Question.
- The capstone doc requires at least 20 unit tests with a coverage artefact (Section 7.4).

## 6. Worked Example: AC-05 Quiz Auto-Grading

**Acceptance criterion:** Quiz supports MCQ (single correct) and TRUE / FALSE question types; quizzes are auto-graded by a deterministic rule.

**Failing test (red).** A test named in the form `test_ac05_...` describes one scenario from the quiz engine spec. For example: Given a quiz with 4 questions and 3 answered correctly, When the attempt is submitted, Then the score is 75%. The test fails, because no grading rule exists yet.

**Making it pass (green).** The simplest change is a grading rule in the domain layer. It counts correct answers and turns the count into an integer percentage. It does not use floating-point math (NFR-01). The test passes.

**Refactor.** The rule is moved to its own domain file, the quiz grading rule in Section 5 of the architecture doc. The MCQ and TRUE / FALSE checks are kept in one place, so the same answers always give the same score (DR-7). The tests still pass.

**Commit hashes.** To be completed with real commit hashes after sprint 3.
