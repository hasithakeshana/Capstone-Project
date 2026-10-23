# Setup problems and the first failing CI run

- **Date:** 2026-10-23
- **Sprint:** 0 (setup)
- **Symptom:** Claude could not run pytest, because the token governor blocked the command. Then PR #1 had failing checks: the tooling job (ruff EXE001), the backend job (a mutmut-only `pyproject.toml` treated as a backend), and the sast job (`semgrep ci --error` is not a valid option).

## Environment checks (in order)

- **Versions:** npm failed with "Cannot find module '@npmcli/config'". After Node and npm were reinstalled, npm 10.9.9 worked. Python on the default PATH was 3.8.5 (Anaconda), which is too old for the SDK. uv 0.13.5 is installed, and it uses CPython 3.12 for the project.
- **Dependencies:** `uv` was not installed. Installing it fixed the Python 3.12 runs. `uv run --with ruff` and `uv run --with pytest` then worked.
- **Environment variables:** no key values were printed. The governor's hook refused commands by their text, not by environment.
- **Ports:** not relevant (no app server ran).
- **Database and migrations:** not relevant (no database yet).
- **Browsers:** not relevant to these failures.
- **CI image:** the CI runner is ubuntu-latest, and the local machine is Windows. The two differ on the executable bit. Semgrep could not be run locally: `uv` installed it, but it had no runnable executable on Windows, so the scan ran only in CI.

## Root cause

- The token governor was set to "enforced", and the helper it pointed to (`.claude/scripts/run-compact.js`) was not installed by the lean scaffold. Test and lint commands were blocked. See KD-01.
- Windows has no executable bit, so the shebang scripts passed locally and failed on Linux CI. See KD-02.
- The sast step used `semgrep ci --error`, which is not a valid option. See KD-03.
- The sast scan covered harness machinery under `.claude/` and produced hundreds of findings. See KD-04.
- The backend check treated the scaffold's `pyproject.toml` (which only has `[tool.mutmut]`) as a backend.

## Fix

- Commit `0695365`: token governor set to "advisory".
- Commit `0253a20`: scripts marked executable in git; the backend check now requires a `[project]` table; the semgrep step changed to `semgrep scan`.
- Commit `75fbb76`: semgrep limited to python and typescript rules, excluding `.claude`.

## Prevention

- KD-01 to KD-04 in `docs/knowledge-deposits.md`.
- The backend check in `.github/workflows/ci.yml` now requires a `[project]` table.

## Lesson

Check the environment first (versions, tools on PATH, operating system differences), and only then change the configuration.

## Links

- Fix loop: [docs/fix-loops/2026-10-23-pr1-ci-checks.md](../fix-loops/2026-10-23-pr1-ci-checks.md)
- PR: https://github.com/hasithakeshana/Capstone-Project/pull/1
