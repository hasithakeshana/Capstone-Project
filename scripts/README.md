# scripts/

Helper scripts for sprint close and capstone evidence. Nothing here edits app code.

| File | What it does | AI? |
|---|---|---|
| `sprint_close.sh` | Mechanical sprint evidence: AC tag table, coverage, metrics, branch and commit checks, PR body, docs reminders | No |
| `ac_coverage_audit.py` | Claude judges whether each AC's tests cover its spec scenarios (Claude Agent SDK) | Yes |
| `test_ac_coverage_audit.py` | Tests for the pure functions of `ac_coverage_audit.py`. No network, no SDK calls | No |
| `capstone_checklist.md` | Marking checklist used by `/capstone-audit` | No |
| `requirements.txt` | Python dependency for `ac_coverage_audit.py` (`claude-agent-sdk==0.2.173`) | No |

## Install

Python 3.12 is needed for the SDK script. Bash (Git Bash on Windows) is needed for `sprint_close.sh`.

```bash
pip install -r scripts/requirements.txt
```

The SDK script needs one of these:
- `ANTHROPIC_API_KEY` set in the environment, or
- a Claude Code login.

The key is read from the environment only. Never write it to a file.

## Run

```bash
uv run --with pytest python -m pytest scripts/test_ac_coverage_audit.py -q   # tests, no SDK needed
bash scripts/sprint_close.sh --ac-only                    # AC tag table only
bash scripts/sprint_close.sh 1                            # full close for sprint 1
python scripts/ac_coverage_audit.py                       # semantic coverage, all ACs
python scripts/ac_coverage_audit.py --ac AC-01 --ac AC-02 # repeatable --ac
python scripts/ac_coverage_audit.py --model claude-haiku-5-5  # --model overrides the default
```

`/sprint-close` runs `sprint_close.sh N`. `/ac-coverage` runs `sprint_close.sh --ac-only`.

## The SDK script

- Imports `claude_agent_sdk` only when it asks Claude for a judgement. The tests and CI run without the SDK.
- Claude may use only `Read`, `Grep` and `Glob`, with at most 5 turns and a budget of 0.50 USD per AC.
- Default model: `claude-haiku-5-5`. `--model` overrides it.
- For each AC it sends the Given/When/Then scenarios from its feature spec and the test lines that carry the literal AC id. A name like `test_ac01_` alone does not count.
- Each scenario gets COVERED, PARTIAL or MISSING, with the test as evidence and one line on the gap.

## Outputs (all under `reports/`)

| File | Written by |
|---|---|
| `ac-coverage.md` | `sprint_close.sh` (AC table: literal `AC-NN` match) |
| `sprint-N-summary.md` | `sprint_close.sh N` (BLOCKING, REMINDERS, metrics, commits) |
| `mr-sprint-N.md` | `sprint_close.sh N` (PR body, if the gate is ready) |
| `coverage.xml`, `lcov.info` | test runs (backend and frontend) |
| `ac-semantic-coverage.md` | `ac_coverage_audit.py` |

`sprint_close.sh N` also copies `specs/reviews/*.md` and `*.json` into `specs/reviews/sprint-N/`.

## Exit codes

| Script | 0 | 1 | 2 |
|---|---|---|---|
| `sprint_close.sh --ac-only` | always, on success | not used | not used |
| `sprint_close.sh N` | no BLOCKING item | at least one BLOCKING item | bad argument |
| `ac_coverage_audit.py` | no MISSING scenario | at least one MISSING scenario | setup error: SDK not installed, Claude CLI not found, or no credentials / API error |

Missing ACs in `--ac-only` are shown in the table, not treated as a failure.

## Blocking checks (`sprint_close.sh N`)

- The current branch is `main` or `master`, or local `main` has commits not on `origin/main`.
- A commit in the branch range has no `Co-Authored-By: Claude` line.
- Backend or frontend line coverage is below 80% (when the report exists).
- A test run fails.
- An AC for sprint N has no test with its literal id. Sprint ACs come from `specs/app_spec.md` → Sprint Plan.

## Reminders (never block)

- `docs/post-mortems/` or `docs/fix-loops/` has only `README.md`, or is empty.
- `docs/knowledge-deposits.md` has no rows.
- Coverage was skipped because the project part does not exist yet.
- The PR body gate is not ready.
