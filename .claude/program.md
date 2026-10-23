# Program

## Instructions

<!-- BRD INSTRUCTIONS PLACEHOLDER -->
<!-- Replace this block with the Business Requirements Document (BRD) instructions for the current project. -->
<!-- These instructions drive the autonomous /auto loop — be specific about features, acceptance criteria, and constraints. -->

### LearnLab

- **Requirements:** `specs/app_spec.md`, the feature specs in `specs/`, and the current sprint PRD in `specs/sprints/`.
- **Spec-Is-Truth:** if a spec and the code disagree, stop and ask for the spec to be updated first.
- **Skill per story area:** implementers must read the skill for their area before coding.
  - course lifecycle → `.claude/skills/course-state-validator/SKILL.md`
  - enrollment → `.claude/skills/enrollment-deduper/SKILL.md`
  - progress → `.claude/skills/progress-aggregator/SKILL.md`
  - quiz → `.claude/skills/quiz-grader/SKILL.md`
  - writing tests → `.claude/skills/spec-to-test-generator/SKILL.md`
  - architecture rules → `.claude/skills/archtest-author/SKILL.md`
- **Domain review step:** after a group's implementers finish and before the evaluator runs, spawn the matching LearnLab agent to review the group's diff against its feature spec:
  - course → `course-publisher-agent`
  - enrollment → `enrollment-manager-agent`
  - progress → `progress-tracker-agent`
  - quiz → `quiz-grader-agent`
  - any state change → `state-machine-validator-agent`
  - architecture stories → `archtest-author-agent`

  Save findings to `specs/reviews/domain-review-{group}-{agent-name}.md` (for example `domain-review-group-A-enrollment-manager-agent.md`). Fix blocking findings first.
- **Evaluator browser checks:** use the Playwright MCP server from `.mcp.json` (`mcp__playwright__browser_*` tools) for Layer 2 UI verification. Save at least one screenshot per group to `specs/reviews/screenshots/<group>/` and list the browser steps taken in the group's evaluator report in `specs/reviews/`.
- **Quality rules (every group; the orchestrator re-reads these each iteration):**
  - **Commit cadence:** same format as process rule PR-learnlab-01: `test(AC-NN): <behaviour>` (failing test, red), then `feat(AC-NN): <change>` (green), then `refactor(AC-NN): <change>` (optional; source only, never tests or snapshots). If a harness gate blocks a test-only commit, commit test + code together as `feat(AC-NN): …` and note "red step blocked by <gate>" in the commit body. The end-of-group commit only collects leftovers. Every commit ends with `Co-Authored-By: Claude <noreply@anthropic.com>`.
  - **Test ids:** every acceptance criterion in the sprint has at least one test with the literal id `AC-NN`. pytest: name `test_acNN_<behaviour>`, marker `@pytest.mark.ac("AC-NN")`, docstring starting `AC-NN: …`. Vitest and Playwright titles start with `AC-NN …`. Where a harness story AC id exists (e.g. `E1-S1-AC2`), put it in brackets after AC-NN in the title and docstring: `AC-01 (E1-S1-AC2): …`. NFR and architecture tests: `test_nfrNN_<behaviour>` / `test_arch_<behaviour>` with `NFR-NN:` / `Architecture:` at the start of the docstring. When `pyproject.toml` is created (sprint 1), register the marker: `[tool.pytest.ini_options]` `markers = ["ac(id): acceptance criterion id"]`.
  - **Coverage:** coverage runs write `reports/coverage.xml` (backend) and `reports/lcov.info` (frontend).
  - **E2E:** Playwright specs (Phase 9) end with a screenshot assertion; snapshot folders are committed.
  - **Architecture:** rules live in `pyproject.toml` `[tool.importlinter]` and `tests/architecture/`. Run `lint-imports` as part of the test gate.
  - **Tooling config (sprint 1):** `pyproject.toml` sets pytest `testpaths = ["tests"]` and measures coverage with `--cov=src` only. `scripts/` is tooling, not app code.

## Constraints

- **Layered architecture:** All code must respect the layer hierarchy defined in `architecture.md`. No cross-layer imports in forbidden directions.
- **Review gate:** Every sprint/iteration must pass the review gate before advancing to the next phase.
- **Max retries:** No more than 3 consecutive auto-fix attempts per error category before escalating to a human.
- **No new dependencies without noting:** Any new package or library added must be logged in the current iteration's status block.
- **Self-heal before revert:** Always attempt automated self-healing (see Self-Healing Policy) before reverting to a prior commit.
- **Never delete learned rules:** Rules discovered during a session (error patterns, project-specific fixes) must be preserved in memory and never removed.
- **TDD mandatory:** Write failing tests FIRST, then implement code to make them pass. Never write implementation before tests. Tests define the contract; code fulfills it.
- **100% meaningful coverage:** Every line of generated code must be covered by tests. Coverage is not about bug prevention — it's about guaranteeing the agent has double-checked the behavior of every line it wrote (ref: "AI is forcing us to write good code" by Steve Krenzel). At 100%, any uncovered line is an immediate, unambiguous signal of missing verification.
- **Coverage floor: 80%.** The ratchet gate BLOCKS any commit that drops coverage below 80%. Target is 100% — 80% is the absolute minimum, not the goal.
- **Model tiering:** Use Opus for orchestration/evaluation (judgment tasks), Sonnet for implementation teammates (execution tasks). Configure via project-manifest.json.

## Stopping Criteria

The autonomous `/auto` loop terminates when any of the following conditions are met:

| Condition | Description |
|-----------|-------------|
| All features pass | Every story in the current sprint has passing tests and a green review gate |
| 3 consecutive failures | The same error category fails 3 times in a row without progress |
| Architecture violation | A layer dependency violation is detected and cannot be auto-fixed |
| Coverage below threshold | Test coverage drops below the project baseline and cannot be recovered in one iteration |
| Max iterations | The configured maximum iteration count is reached (default: 50, configured in project-manifest.json) |

## Self-Healing Policy

When an automated check fails, apply the fix strategy from the table below before re-running. If the fix strategy fails after the max retry count, stop and report.

| Category | Signal | Auto-fix |
|----------|--------|----------|
| Lint/format | ruff/eslint fails | `ruff check --fix && ruff format` |
| Type error | mypy/tsc reports type errors | Fix annotation or cast at the error site |
| Test failure | pytest/vitest fails | Fix code under test; never modify the test to make it pass |
| Import error | `ImportError` / `ModuleNotFoundError` at runtime | Fix layer placement or missing `__init__` |
| Coverage drop | Coverage falls below baseline | Add targeted tests for uncovered lines |
| API check fail | Evaluator returns 500/404 or wrong response schema | Read error message, fix service logic or router handler |
| Playwright fail | Element not found / wrong state in browser test | Read selector, fix component rendering or interaction |
| Design score low | Critic scores UI below threshold | Apply critique feedback, regenerate affected component |
| Docker fail | Container fails to start or health check fails | Read container logs, fix config or dependency issue |
| Architecture drift | Response shape does not match declared schema | Read schema definition, fix response serialization |

## Pipeline Status

Phase order is owned by `/build` (`.claude/skills/build/SKILL.md`): Brownfield discovery (existing codebases) → BRD → Spec → Design + Test-planning (parallel) → state init → deploy artifacts (docker mode) → autonomous execution via `/auto` (ratchet loop) → E2E test generation → README. Do not sequence phases from this file.

| Phase | Status | Notes |
|-------|--------|-------|
| Brownfield discovery | pending | existing codebases only |
| BRD | pending | Business requirements not yet loaded |
| Spec | pending | |
| Design + Test-plan | pending | run in parallel |
| Deploy artifacts | pending | docker mode |
| Autonomous execution (/auto) | pending | |
| E2E test generation | pending | |
| README | pending | |

## Current Focus

```
iteration : 0
status    : idle
story     : (none)
phase     : (none)
coverage  : (none)
```
