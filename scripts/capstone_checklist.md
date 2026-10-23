# Capstone checklist (marking)

Used by `/capstone-audit`. Source: `docs/reference/AI Native Engineer Capstone - BC-011 LearnLab.md`, Sections 7.1–7.5 and 8.1–8.2. Check each line against the repo. The evidence path is what to look for.

## Section 7.1 — Claude Code specs (40 marks)

- [ ] 7.1.1 `specs/app_spec.md` and `specs/<feature>_spec.md`, each with AC sections — evidence: `specs/app_spec.md`, `specs/*_spec.md` with `### AC-NN` headings
- [ ] 7.1.2 Layered CLAUDE.md: root, per-module and per-folder — evidence: `CLAUDE.md`, `src/CLAUDE.md`, `frontend/CLAUDE.md`, `e2e/CLAUDE.md`, `src/domain/CLAUDE.md`, `src/controllers/CLAUDE.md`, `src/repositories/CLAUDE.md`, `migrations/CLAUDE.md`, `tests/CLAUDE.md`
- [ ] 7.1.3 AGENTS.md as a table of contents only — evidence: `AGENTS.md`
- [ ] 7.1.4 At least 2 project skills in `.claude/skills/` — evidence: `.claude/skills/<name>/SKILL.md` (LearnLab skills)
- [ ] 7.1.5 At least 2 project commands in `.claude/commands/` — evidence: `.claude/commands/*.md`
- [ ] 7.1.6 At least 2 project hooks in `.claude/hooks/` — evidence: `.claude/hooks/*.js` registered in `.claude/settings.json`
- [ ] 7.1.7 At least 2 project agents in `.claude/agents/` — evidence: `.claude/agents/*-agent.md`, `tester.md`, `doc-writer.md`
- [ ] 7.1.8 Claude Agent SDK used in a script — evidence: `scripts/ac_coverage_audit.py` imports `claude_agent_sdk`
- [ ] 7.1.9 Own `plugin.json` packaging the project substrate — evidence: `plugin.json` (repo root), `.claude-plugin/plugin.json`
- [ ] 7.1.10 Debugging log or post-mortem under `docs/` (environment first) — evidence: `docs/post-mortems/*.md`
- [ ] 7.1.11 Playwright MCP in `.mcp.json` and used by the evaluator — evidence: `.mcp.json` (`playwright`), `.claude/agents/evaluator.md` (`mcp__playwright__*` tools), `specs/reviews/screenshots/`

## Section 7.2 — Business understanding (20 marks)

- [ ] 7.2.1 `docs/business-case.md` covers problem, target users, success metrics, domain rules and value proposition — evidence: `docs/business-case.md` headings
- [ ] 7.2.2 At least 4 rule, policy or validator files under `src/domain/` — evidence: `src/domain/*.py` (4 or more)
- [ ] 7.2.3 Frontend (React, Angular or Vue) with at least one responsive layout — evidence: `frontend/package.json`, responsive Playwright snapshots in `e2e/`
- [ ] 7.2.4 Acceptance criteria in testable form (Given-When-Then or AC-NN) for at least 4 specs — evidence: `specs/*_spec.md` with `### AC-NN` and `- Given` lines

## Section 7.3 — Architectural discipline (8 marks)

- [ ] 7.3.1 Architecture test directory with at least 3 structural tests — evidence: `tests/architecture/` (3 or more `test_arch_` functions)
- [ ] 7.3.2 ArchUnit, dependency-cruiser or import-linter enforces the layers — evidence: `pyproject.toml` `[tool.importlinter]`
- [ ] 7.3.3 `docs/tdd.md`, and at least 10 test files committed across history with red → green → refactor — evidence: `docs/tdd.md`; `git log` shows `test(AC-NN)` before `feat(AC-NN)` commits

## Section 7.4 — Technical implementation (26 marks)

- [ ] 7.4.1 `docs/architecture.md` with at least one diagram and explicit layers (controllers, services, repositories, domain) — evidence: `docs/architecture.md` (Mermaid blocks)
- [ ] 7.4.2 At least 3000 lines of meaningful generated code — evidence: `reports/sprint-N-summary.md` (source lines)
- [ ] 7.4.3 Playwright UI validation with at least one snapshot directory — evidence: `e2e/**/*-snapshots/`
- [ ] 7.4.4 Tests tagged with AC IDs, and every spec AC has at least one test — evidence: `reports/ac-coverage.md` (all rows COVERED)
- [ ] 7.4.5 At least 20 unit tests with a coverage artefact and the coverage tool declared — evidence: `reports/coverage.xml` or `reports/lcov.info`; `pytest-cov` in `pyproject.toml`; `@vitest/coverage-v8` in `frontend/package.json`

## Section 7.5 — CI/CD (6 marks)

- [ ] 7.5.1 CI pipeline with build and test — evidence: `.github/workflows/*.yml`
- [ ] 7.5.2 Claude Code Action (or equivalent) wired into CI — evidence: `.github/workflows/*.yml` uses `anthropics/claude-code-action`
- [ ] 7.5.3 At least 3 PR-driven merges (`--no-ff`); zero direct commits to main — evidence: `git log --merges main` (3 or more); no non-merge commits made directly on main

## Section 8.1 — Mandatory (items 1–10)

- [ ] 8.1.1 Working application runs locally with one command, seed data and a README quick-start — evidence: `README.md` quick-start, the run command from the sprint 1 design, seed data code
- [ ] 8.1.2 `docs/business-case.md` — evidence: `docs/business-case.md`
- [ ] 8.1.3 `specs/app_spec.md` and per-feature specs (course-authoring, catalog, enrollment, quiz-engine, progress-tracker, instructor-workbench, admin-console) with AC sections — evidence: `specs/*_spec.md`
- [ ] 8.1.4 Layered CLAUDE.md hierarchy; AGENTS.md as table of contents — evidence: `CLAUDE.md` tree, `AGENTS.md`
- [ ] 8.1.5 Project agent substrate: `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, `.claude/hooks/`, including the 7.1 additions — evidence: the four folders
- [ ] 8.1.6 Harness plugin installed; project scaffolded; at least one full sprint cycle (Generator → Evaluator → ratcheting → PR); sprint contracts and evaluator outputs committed — evidence: `sprint-contracts/`, `specs/reviews/`, PR history
- [ ] 8.1.7 `plugin.json` at the repo root; `.mcp.json` with Playwright MCP active — evidence: `plugin.json`, `.mcp.json`
- [ ] 8.1.8 Test suite: unit (quiz grading, progress aggregation, role boundaries, state transitions), architecture, AC-tagged, Playwright UI, coverage report — evidence: `tests/`, `e2e/`, `reports/coverage.xml`
- [ ] 8.1.9 CI pipeline with Claude Code Action; passing build on main — evidence: `.github/workflows/`, GitHub Actions run status on main
- [ ] 8.1.10 PR-driven git history: at least 3 PR-driven merges; zero direct pushes to main — evidence: `git log --merges main`

## Section 8.2 — Good to have (items 11–15)

- [ ] 8.2.11 Architecture and TDD docs: a diagram (C4 context or sequence), and `docs/tdd.md` with one worked example (AC-05) — evidence: `docs/architecture.md`, `docs/tdd.md`
- [ ] 8.2.12 Autonomous fix-loop evidence: a recorded failure → reproduce → fix → validate → PR loop — evidence: `docs/fix-loops/*.md`
- [ ] 8.2.13 Knowledge deposit log: recurring mistakes encoded as rules, hooks or skills — evidence: `docs/knowledge-deposits.md` (rows)
- [ ] 8.2.14 Multiple sprint cycles covering catalog and enrollment, then lessons and progress, then quiz engine and instructor workbench — evidence: `specs/sprints/sprint-*_prd.md`, `specs/reviews/sprint-N/`, `reports/sprint-N-summary.md`
- [ ] 8.2.15 Bonus agents beyond the required additions — evidence: `.claude/agents/doc-writer.md`, `.claude/agents/tester.md`, other agents beyond the required set
