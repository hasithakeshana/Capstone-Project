# Acceptance Test Template

Use this shape for every acceptance test. Write it in plain business language.

**Test name:** `test_acNN_<behaviour>` (for example `test_ac01_learner_cannot_enroll_twice`)
**Tag:** `@pytest.mark.ac("AC-NN")`
**Docstring:** starts with `AC-NN:`

## Example: AC-01

- **Given** Ada is a registered learner
  and the course "Intro to Python" is PUBLISHED
- **When** Ada enrolls in "Intro to Python" for the first time
  and then enrolls in it again
- **Then** the second request is rejected
  and Ada has exactly 1 enrollment for "Intro to Python"

## Rules

- Use concrete dummy data only (synthetic names, `@example.com` emails).
- One behaviour per test.
- Name the business outcome in Then, not the code path.
