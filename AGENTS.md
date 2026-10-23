# AGENTS.md — Table of Contents

Index only. Rules live in `CLAUDE.md`, `.claude/program.md`, and the files linked below.

plugin.json (repo root) — capstone deliverable; .claude-plugin/plugin.json — same content, Claude Code plugin manifest.

## Harness agents

| Agent | Path |
|---|---|
| planner | `.claude/agents/planner.md` |
| generator | `.claude/agents/generator.md` |
| implementer | `.claude/agents/implementer.md` |
| evaluator | `.claude/agents/evaluator.md` |
| code-reviewer | `.claude/agents/code-reviewer.md` |
| security-reviewer | `.claude/agents/security-reviewer.md` |
| design-critic | `.claude/agents/design-critic.md` |
| advisor | `.claude/agents/advisor.md` |
| modularity-reviewer | plugin agent (not in `.claude/agents/`) |
| codebase-explorer | plugin agent (not in `.claude/agents/`) |

## LearnLab agents

| Agent | Path |
|---|---|
| course-publisher-agent | `.claude/agents/course-publisher-agent.md` |
| enrollment-manager-agent | `.claude/agents/enrollment-manager-agent.md` |
| progress-tracker-agent | `.claude/agents/progress-tracker-agent.md` |
| quiz-grader-agent | `.claude/agents/quiz-grader-agent.md` |
| state-machine-validator-agent | `.claude/agents/state-machine-validator-agent.md` |
| archtest-author-agent | `.claude/agents/archtest-author-agent.md` |
| tester | `.claude/agents/tester.md` |
| doc-writer | `.claude/agents/doc-writer.md` |

## LearnLab skills

| Skill | Path |
|---|---|
| course-state-validator | `.claude/skills/course-state-validator/SKILL.md` |
| enrollment-deduper | `.claude/skills/enrollment-deduper/SKILL.md` |
| progress-aggregator | `.claude/skills/progress-aggregator/SKILL.md` |
| quiz-grader | `.claude/skills/quiz-grader/SKILL.md` |
| spec-to-test-generator | `.claude/skills/spec-to-test-generator/SKILL.md` |
| archtest-author | `.claude/skills/archtest-author/SKILL.md` |

## LearnLab commands

| Command | Path |
|---|---|
| /implement-ac | `.claude/commands/implement-ac.md` |
| /ac-coverage | `.claude/commands/ac-coverage.md` |
| /spec-change | `.claude/commands/spec-change.md` |
| /sprint-close | `.claude/commands/sprint-close.md` |
| /capstone-audit | `.claude/commands/capstone-audit.md` |

## LearnLab hooks

| Hook | Path | Event |
|---|---|---|
| block-main-commit | `.claude/hooks/block-main-commit.js` | PreToolUse (Bash) |
| ac-tag-check | `.claude/hooks/ac-tag-check.js` | PostToolUse (Write, Edit, MultiEdit) |
| role-boundary-check | `.claude/hooks/role-boundary-check.js` | PostToolUse (Write, Edit, MultiEdit) |
| attempt-immutability-check | `.claude/hooks/attempt-immutability-check.js` | PreToolUse (Write, Edit, MultiEdit) |
| course-publish-gate | `.claude/hooks/course-publish-gate.js` | PreToolUse (Write, Edit, MultiEdit) |

## Role mapping

| Canonical role | Harness agents | Notes |
|---|---|---|
| implementer | generator + implementer | |
| reviewer | evaluator + code-reviewer + security-reviewer | |
| tester | tester | Harness v5 has no test-engineer. |

Harness names are kept because the pipeline dispatches by name.

## Changes to harness files

| File | Change |
|---|---|
| `.claude/agents/evaluator.md` | Tools list: Playwright MCP entries added. |
| `.claude/program.md` | `### LearnLab` block added. |
| `.claude/state/process-rules.md` | `PR-learnlab-01` to `06` appended. |
| `.claude/settings.json` | LearnLab hook entries appended. |
| agent model pins | implementer Haiku 5.5; generator, evaluator, code-reviewer, security-reviewer, advisor Sonnet 5.5; planner Opus — to fit the plan quota |
| `.claude/architecture.md` | Layer Hierarchy rewritten for LearnLab layers (core → domain → repositories → services → controllers); verification commands updated. |
| `REVIEW.md` | Encoded Policy: import hierarchy line changed to the LearnLab layers. |
| `.github/workflows/security.yml` | sast: `semgrep ci --error` → `semgrep scan --config p/python --config p/typescript --exclude .claude --error` (+ setuptools<81). Scans project code only; harness folder `.claude` is excluded. |
