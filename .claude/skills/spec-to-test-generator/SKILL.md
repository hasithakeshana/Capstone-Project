---
name: spec-to-test-generator
description: Use when turning acceptance criteria or Given/When/Then scenarios from a spec into tests, before writing production code for an AC (the TDD red step). Produces AC-tagged tests at the right level.
---

# Spec to Test Generator

## Purpose

Turn each Given/When/Then scenario into one AC-tagged test that fails first. Covers all ACs and their rejection scenarios.

## Guide

1. Take one scenario from the feature spec. Write one test for it.
2. Name and tag the test:
   - pytest: `test_acNN_<behaviour>` + `@pytest.mark.ac("AC-NN")` + docstring `AC-NN (E1-S1-ACn): …`.
   - NFR tests: `test_nfrNN_<behaviour>`, docstring starts `NFR-NN:`.
   - Vitest and Playwright: title starts `AC-NN (E1-S1-ACn): …`.
   - Add the harness story id in brackets only when one exists (process rule PR-learnlab-03).
3. Follow the shape in `specs/test_artefacts/at-template.md`: Given/When/Then comments, a fake in-memory adapter, ids not emails.
4. Pick the level:
   - domain rule → `tests/domain/`
   - service use case → `tests/services/`
   - API route → `tests/controllers/`
   - repository → `tests/repositories/`
   - browser user flow → `e2e/` (Playwright). End the spec with `await expect(page).toHaveScreenshot();`.
   - architecture rule → use the archtest-author skill instead.
5. Write the test first. Run it. Confirm it fails for the right reason: the behaviour is missing, not a typo or an import error.
6. Commit the red step as `test(AC-NN): <behaviour>` (process rule PR-learnlab-01).
7. Cover the rejection scenario, not only the happy path. Every "Then the request is rejected" line in the spec needs its own test.
8. One behaviour per test.

## Check for

- Tests without an AC, NFR or architecture id.
- Skipped, deleted or weakened tests (`skip`, `xfail`, removed asserts).
- Assertions that only repeat the code under test.
- Tests that pass before the code exists.
- Missing rejection tests.
- ACs in the sprint with no test that carries their id.

## Tests to write

- One test per scenario in the feature spec, at the right level.
- The AC coverage check: every AC in the sprint has at least one test with its id (`docs/tdd.md`).

## References

- `docs/tdd.md`.
- `specs/test_artefacts/at-template.md`.
- The feature specs in `specs/`.
- `tests/CLAUDE.md`.
