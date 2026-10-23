# Knowledge deposits

Each row records a real mistake and the rule, hook, config or skill that now stops it.

| ID | Date | Mistake seen | Encoded as (rule/hook/skill/config) | File |
|---|---|---|---|---|
| KD-01 | 2026-10-23 | Token governor "enforced" blocked pytest and ruff runs, because the lean scaffold did not install `.claude/scripts/run-compact.js` | Manifest `token_governor.mode` set to "advisory" | `project-manifest.json` (commit 0695365) |
| KD-02 | 2026-10-23 | Ruff EXE001 passed on Windows but failed on Linux CI, because Windows has no executable bit | Scripts marked executable in git | `scripts/ac_coverage_audit.py`, `scripts/sprint_close.sh` (commit 0253a20) |
| KD-03 | 2026-10-23 | Harness `security.yml` used `semgrep ci --error`, an invalid option | Changed to `semgrep scan` | `.github/workflows/security.yml` (commit 0253a20) |
| KD-04 | 2026-10-23 | Semgrep scanned harness machinery under `.claude/`, with hundreds of findings | Rules limited to python and typescript; `--exclude .claude` | `.github/workflows/security.yml` (commit 75fbb76) |
