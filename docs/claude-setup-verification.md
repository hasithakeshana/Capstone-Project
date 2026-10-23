# Claude setup verification (S12, updated in S13)

- **Date:** 2026-10-23
- **Branch:** `chore/foundation`, PR #1 (draft): https://github.com/hasithakeshana/Capstone-Project/pull/1
- **Scope:** read-only checks at S12. Updated in S13 with decisions and manual-check results.

Legend: ✅ done · ⚠️ done with a gap · ⏳ planned, needs app code, a sprint run, or a merge

## PART A — Repo tree

Compared against the expected layout in S12.

| Area | Result |
|---|---|
| Root files (CLAUDE.md, AGENTS.md, README.md, plugin.json, .mcp.json, project-manifest.json, pyproject.toml, .gitignore, REVIEW.md) | ✅ all present. `pyproject.toml` holds only the scaffold's `[tool.mutmut]` block, as expected. |
| `.github/workflows/` (ci.yml, claude-review.yml, security.yml, deploy.yml) | ✅ all present. `deploy.yml` is the unused harness file. |
| `.claude/` (settings.json, program.md, architecture.md, process-rules.md) | ✅ all present. `program.md` has the `### LearnLab` block. `architecture.md` has the LearnLab layers. |
| `.claude/agents/` | ✅ 16 files: 8 harness and our 8 (course-publisher, enrollment-manager, progress-tracker, quiz-grader, state-machine-validator, archtest-author, tester, doc-writer). |
| `.claude/skills/` | ✅ our 6 present: course-state-validator, enrollment-deduper, progress-aggregator, quiz-grader, spec-to-test-generator, archtest-author. |
| `.claude/commands/` | ✅ our 5: implement-ac, ac-coverage, spec-change, sprint-close, capstone-audit. |
| `.claude/hooks/` | ✅ our 5 `.js` files and `learnlab-hooks.json`, plus the harness hooks. |
| `scripts/` | ✅ ac_coverage_audit.py, test_ac_coverage_audit.py, sprint_close.sh, capstone_checklist.md, requirements.txt, README.md. |
| CLAUDE.md files | ✅ in src/, src/domain/, src/services/, src/controllers/, src/repositories/, tests/, migrations/, frontend/, e2e/. |
| docs/ | ✅ business-case.md, architecture.md, tdd.md, harness-integration.md, knowledge-deposits.md (KD-01 to KD-04), post-mortems/README.md and the 2026-10-23 post-mortem, fix-loops/README.md and the 2026-10-23 fix loop. |
| specs/ | ✅ app_spec.md, the 7 feature specs, requirements-traceability.md, design/constitution.md, design/CONTEXT.md, test_artefacts/at-template.md, sprints/sprint-1 to sprint-3 PRDs. |
| Unexpected production code, tests or migrations | ✅ none. The only tracked files under src/, tests/, frontend/, e2e/ and migrations/ are CLAUDE.md files. |
| Wrong names | ✅ none found. |
| Untracked files | ⚠️ `uv.lock` is untracked. Decision: leave it untracked; sprint 1 creates the real one. `reports/` is untracked on purpose. |

## PART B — Capstone Section 7.1

| Item | Evidence path | Count | Status |
|---|---|---|---|
| 7.1.1 Specs with AC sections | `specs/app_spec.md`, `specs/*_spec.md` | 8 files | ✅ |
| 7.1.2 Layered CLAUDE.md | `CLAUDE.md` and 9 folder CLAUDE.md files | 10 | ✅ |
| 7.1.3 AGENTS.md as table of contents | `AGENTS.md` | 1 | ✅ |
| 7.1.4 Project skills (≥2) | `.claude/skills/*/SKILL.md` | 6 | ✅ |
| 7.1.5 Project commands (≥2) | `.claude/commands/*.md` | 5 | ✅ |
| 7.1.6 Project hooks (≥2) | `.claude/hooks/*.js` registered in `settings.json` | 5 | ✅ |
| 7.1.7 Project agents (≥2) | `.claude/agents/*` | 8 | ✅ |
| 7.1.8 Agent SDK in scripts | `scripts/ac_coverage_audit.py` | 1 (not run yet) | ✅ |
| 7.1.9 Own plugin.json | `plugin.json` and `.claude-plugin/plugin.json` (identical) | 2 | ✅ |
| 7.1.10 Debugging log / post-mortem | `docs/post-mortems/2026-10-23-setup-and-first-ci-run.md` | 1 | ✅ |
| 7.1.11 Playwright MCP in .mcp.json, used by evaluator | `.mcp.json` (1 server); `evaluator.md` (10 tools) | 1 + 10 | ⏳ config done; evaluator browser use is planned for sprint 1 |

## PART C — Items this step prepares

| Item | Evidence | Status |
|---|---|---|
| 3.4 No-hand-coding, Spec-is-truth, PR-only merge, Synthetic data | `CLAUDE.md` → Project rules | ✅ |
| 3.4 Process rules | `.claude/state/process-rules.md` (PR-learnlab-01 to 06) | ✅ |
| 3.4 PR-only enforcement | `block-main-commit.js` registered; self-tested; manual main-commit block passed | ✅ |
| 7.3 TDD document | `docs/tdd.md` | ⚠️ worked-example commit hashes are a placeholder. Planned: fill after sprint 3. |
| 7.3 Architecture rule author | archtest-author skill and agent | ✅ |
| 7.3 Architecture tests and import-linter config | `tests/architecture/` and `[tool.importlinter]` do not exist yet | ⏳ planned: sprint 1 |
| 7.4 AC-tag rule and hook | PR-learnlab-03; `ac-tag-check.js` (self-tested) | ✅ |
| 7.4 Snapshot rule | program.md and PR-learnlab-05 | ✅ |
| 7.4 Snapshot folder exists | no `e2e/**/*-snapshots/` yet | ⏳ planned: sprint 1 |
| 7.4 Coverage written to reports/ | rule in PR-learnlab-06 and program.md | ✅ |
| 7.4 Coverage artefacts exist | no coverage run yet | ⏳ planned: sprint 1 |
| 7.4 .gitignore does not hide reports/ or snapshots | `git check-ignore` returned no match | ✅ |
| 7.5 CI on PR #1 | Last run: tooling, backend, frontend, gitleaks, sast, review all pass | ✅ |
| 7.5 Claude Code Action with key guard | `claude-review.yml`; the key guard works and skips the review when no key is set | ⚠️ no key set. Planned: the repo owner adds a key secret. |
| 8.1.4 Layered CLAUDE.md and AGENTS.md | see 7.1.2 and 7.1.3 | ✅ |
| 8.1.5 Project agent substrate | see 7.1.4 to 7.1.7 | ✅ |
| 8.1.7 plugin.json and .mcp.json | see 7.1.9 and 7.1.11 | ✅ |
| 8.1.9 CI pipeline | Green on PR #1; not yet green on main | ⏳ planned: after PR #1 is merged |
| 8.2.11 Architecture diagram | `docs/architecture.md` (flowchart and sequence) | ✅ |
| 8.2.11 TDD worked example | `docs/tdd.md` placeholder | ⚠️ planned: sprint 3 |
| 8.2.12 Fix-loop evidence | `docs/fix-loops/2026-10-23-pr1-ci-checks.md` | ✅ |
| 8.2.13 Knowledge deposits | `docs/knowledge-deposits.md` (KD-01 to KD-04) | ✅ |
| 8.2.15 Bonus agents | doc-writer and tester | ✅ |

## PART D — Wiring

| Check | Result |
|---|---|
| Names match across AGENTS.md, plugin.json, learnlab-hooks.json, settings.json and program.md | ✅ every agent, skill, command and hook name in AGENTS.md is found. The five hooks match in settings.json and the plugin hooks file, with the same events and matchers. |
| program.md maps every story area to a skill | ✅ six areas map to six skills. |
| program.md maps every story area to a review agent | ✅ six areas map to six review agents. Writing tests has no review agent by design. |
| evaluator.md lists Playwright MCP tools | ✅ 10 `mcp__playwright__*` entries and 10 `mcp__plugin_playwright_playwright__*` entries in the frontmatter. One more mention is in the harness body text. |
| Both plugin.json files identical and valid | ✅ |
| No CLAUDE.md references the capstone PDF | ✅ |
| Harness layer names in other `.claude/architecture.md` sections | ⏳ planned: no change now. The Cross-Cutting, Bounded Contexts and Customization sections still use harness names such as `src/lib`. |

## PART E — Manual checks

| Check | Result |
|---|---|
| `/agents` shows our 8 LearnLab agents | ✅ passed |
| `/hooks` shows our 5 hooks | ✅ passed |
| `/mcp` shows `playwright` connected | ✅ passed |
| A commit on `main` is blocked by `block-main-commit` | ✅ passed |

## Summary

| Part | ✅ | ⚠️ | ❌ | ⏳ |
|---|---|---|---|---|
| A — tree | 1 | 1 | 0 | 0 |
| B — Section 7.1 | 10 | 0 | 0 | 1 |
| C — prepared items | 15 | 3 | 0 | 4 |
| D — wiring | 5 | 0 | 0 | 1 |
| E — manual | 4 | 0 | 0 | 0 |

No ❌ items. The ⏳ items are planned for later steps, as listed in the decisions below.

## Decisions (S13)

- **uv.lock:** left untracked. Sprint 1 creates the real lock file. No `.gitignore` change.
- **Claude review key:** no change now. Planned: the repo owner adds `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` as a secret.
- **TDD worked-example hashes:** no change now. Planned: fill after sprint 3.
- **Sprint 1 items** (`tests/architecture/`, `[tool.importlinter]`, snapshot folders, coverage artefacts): planned for sprint 1.
- **CI on main:** planned: confirm after PR #1 is merged.
- **Harness layer names** in the other `.claude/architecture.md` sections: no change now. Planned: update with the sprint 1 layers.
- **Fix loop:** recorded as [docs/fix-loops/2026-10-23-pr1-ci-checks.md](fix-loops/2026-10-23-pr1-ci-checks.md). Item 8.2.12 is ✅.

## Manual checks

`/agents`, `/hooks`, `/mcp` and the blocked commit on `main` all passed.
