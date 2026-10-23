---
name: archtest-author
description: Use when setting up or changing layer rules (import-linter contracts in pyproject.toml), architecture tests in tests/architecture/, or the NFR-08 rule tests. Enforces layering, domain purity and the NFR-08 rules as tests.
---

# Architecture Test Author

## Purpose

Enforce the layer rules and the NFR-08 rules as tests that run in the test gate. Covers NFR-04, NFR-08 and the architecture rules in `specs/app_spec.md` → Technical Acceptance.

## Guide

1. Configure import-linter in `pyproject.toml` under `[tool.importlinter]`. Layer order, from `docs/architecture.md` → Layered Structure: controllers → services → repositories → domain. Core is used by controllers, services and repositories.
2. Add these contracts:
   - Layers contract: controllers → services → repositories → domain.
   - Forbidden: `domain` must not import `fastapi`, `sqlalchemy`, services, repositories, controllers or core. Domain uses only the standard library.
   - Forbidden: `controllers` must not import `repositories`.
   - Forbidden: `core` must not import controllers, services, repositories or domain.
3. Domain imports only the standard library. Core is used by controllers, services and repositories. Domain never imports core, and core never imports the other layers.
4. Write at least 3 structural tests in `tests/architecture/`:
   - `test_arch_layering`: runs import-linter and fails on any broken contract.
   - `test_arch_domain_purity`: domain imports only the standard library.
   - `test_arch_repositories_append_only`: no update or delete methods on enrollment, completion or attempt repositories (NFR-02).
   - `test_arch_controllers_require_role`: every route except `/health`, register and login calls `require_role(...)` (NFR-04).
   - `test_arch_no_float_in_scoring`: no float in the quiz and progress modules (NFR-01).
5. Write the NFR-08 rule tests:
   - `test_nfr08_learner_progress_isolation`
   - `test_nfr08_instructor_cannot_grade_own_learners`
   - `test_nfr08_published_course_immutable`
6. Each test docstring starts with `Architecture:` or `NFR-08:`.
7. Run `lint-imports` as part of the test gate. It must also run in CI (`.github/workflows/`, once CI exists).

## Check for

- Missing or incomplete contract in `pyproject.toml`.
- A test that cannot fail. Prove each contract can fail using a small test fixture package under `tests/architecture/fixtures/` that contains a forbidden import. The architecture test must fail on that fixture.
- Architecture rules that do not run in the test gate or CI.
- An NFR-08 rule with no test.

## Tests to write

- The tests listed in Guide step 4 and step 5.
- A test that proves each contract catches a violation, using the fixture package in `tests/architecture/fixtures/`.

## References

- `docs/architecture.md` → Layered Structure and Domain Rules.
- `specs/app_spec.md` → Non-Functional Requirements, Invariants (INV-10, INV-11, INV-12) and Technical Acceptance.
- Rules for test names: `tests/CLAUDE.md` and process rule PR-learnlab-03.
