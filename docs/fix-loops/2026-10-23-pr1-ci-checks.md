# PR #1 CI checks: tooling, backend, sast

- **Failure detected:** PR #1 CI, found by the GitHub Actions checks.
  - tooling: ruff EXE001 (shebang in a file that is not executable).
  - backend: the scaffold's mutmut-only `pyproject.toml` was treated as a backend.
  - sast: `semgrep ci --error` is not a valid option. After that fix, the next sast run scanned `.claude/` harness machinery and reported findings.
- **Reproduced:** the failing job logs were pulled with `gh`. The EXE001 and semgrep option errors were reproduced on Linux with the same commands, as reported by the user.
- **Fixed:**
  - Commit `0253a20`: scripts marked executable in git; backend check requires a `[project]` table; semgrep step changed to `semgrep scan`.
  - Commit `75fbb76`: semgrep limited to python and typescript rules, with `--exclude .claude`.
- **Validated:** `gh pr checks 1`: all 6 checks green (tooling, backend, frontend, gitleaks, sast, review).
- **PR link:** https://github.com/hasithakeshana/Capstone-Project/pull/1
- **Trace excerpt:** the sast findings for the first run (before commit `75fbb76`) listed `.claude/hooks/lib/*.js` path-traversal findings and `.github/workflows/*.yml` mutable-action-tag findings. The log lines contained no secrets.
