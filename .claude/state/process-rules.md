# Process Rules

Monotonic **workflow** constraints for agents (distinct from `learned-rules.md` code patterns).
When the same agent-behaviour failure class appears 2+ times, append a rule here and keep it forever.
Inject into orchestrator, `/implement`, `/auto` teammates, and `/change` before edits.

### PR-default-01 — no destructive git during parallel implement
- **Rule:** never run `git stash`, `git reset --hard`, `git clean -fd`, or `git push --force` while parallel implement is active (`parallel-implement.lock` or `HARNESS_PARALLEL_AGENTS=1`)
- **Enforcement:** pre-bash-gate (`hooks/lib/git-safety.js`) + SECTION 4 teammate prompt
- **Added:** 2026-07-12 (Bun adversarial Phase A)

### PR-default-02 — no stub-to-green
- **Rule:** do not clear compile/lint by shipping stub markers on production paths; implement real behaviour or use an explicit `harness:stub-ok story=…` deferral
- **Enforcement:** code-gen + code-reviewer Iron Laws + `stub-smell-gate` (standard+)
- **Added:** 2026-07-12 (Bun adversarial Phase A)

### PR-default-03 — diagnostics queue: no full-suite mid-shard
- **Rule:** when `fix-from-diagnostics` is active with ≥15 errors, do not run the full monorepo test suite between shards; re-check scoped diagnostics only until the queue is empty
- **Enforcement:** fix-from-diagnostics skill + /auto SECTION 6 self-heal routing
- **Added:** 2026-07-12 (Bun Phase B)

### PR-default-04 — canary before large mechanical / multi-story fan-out
- **Rule:** canary 3 files or one story before applying a mechanical pattern or epic fan-out across more than ~10 files / remaining groups
- **Enforcement:** implement Step 0.5, feature canary story, refactor --mechanical + G32
- **Added:** 2026-07-12 (Bun Phase B)

### PR-default-05 — edit the workflow when agents misbehave
- **Rule:** after repeated workflow failures (stash races, stub-to-green, suite thrash), update process-rules and/or `.claude/workflows/fix-diagnostics.js` / skills — do not only patch product code
- **Enforcement:** workflows/README.md + fix-diagnostics Process learn phase
- **Added:** 2026-07-12 (Bun Phase C)

### PR-learnlab-01 — commits per AC, red then green then refactor
- **Rule:** commit each AC separately in conventional form with a short description:
  `test(AC-NN): <behaviour>` (failing test, red) → `feat(AC-NN): <change>` (green) →
  `refactor(AC-NN): <change>` (optional; source only — never touches tests or snapshots, the
  harness refactor-purity gate blocks that). Never combine steps. If a harness gate (e.g. the
  coverage ratchet early in sprint 1) blocks a test-only commit, commit test + code together as
  `feat(AC-NN): …` and note "red step blocked by <gate>" in the commit body. Every commit
  message ends with `Co-Authored-By: Claude <noreply@anthropic.com>`.
  Example: `test(AC-01): learner cannot enroll twice` → `feat(AC-01): reject duplicate
  enrollment` → `refactor(AC-01): extract enrollment policy`.
- **Enforcement:** `.claude/program.md` → LearnLab quality rules + harness refactor-purity gate
- **Added:** 2026-10-23

### PR-learnlab-02 — no direct commits to main
- **Rule:** never commit or push to `main` or `master`. Work on the sprint branch and open the
  PR with `gh` (GitHub); merge on GitHub with "Create a merge commit".
- **Enforcement:** block-main-commit hook + PR-Only Merge Rule in `specs/app_spec.md`
- **Added:** 2026-10-23

### PR-learnlab-03 — every test carries its AC id
- **Rule:** every test carries the literal capstone id `AC-NN` (the grader searches for it).
  pytest: function name `test_acNN_<behaviour>` + marker `@pytest.mark.ac("AC-NN")` + docstring
  starting `AC-NN: …`. Vitest and Playwright: test titles start with `AC-NN …`.
  Where a harness story AC id exists (e.g. `E1-S1-AC2`), add it in brackets right after the
  AC-NN id: title `AC-01 (E1-S1-AC2): …`, docstring `AC-01 (E1-S1-AC2): …`.
  NFR and architecture tests: `test_nfrNN_<behaviour>` / `test_arch_<behaviour>` with
  `NFR-NN:` / `Architecture:` at the start of the docstring.
  Example (pytest):
    @pytest.mark.ac("AC-01")
    def test_ac01_learner_cannot_enroll_twice():
        """AC-01 (E1-S1-AC2): Given a learner already enrolled, When they enroll again, Then it is rejected."""
  Example (Playwright): test('AC-01 (E1-S1-AC2): learner cannot enroll twice', …)
- **Enforcement:** ac-tag-check hook + `docs/tdd.md` → Test Naming
- **Added:** 2026-10-23

### PR-learnlab-04 — read the story-area skill before coding
- **Rule:** implementers read the skill for their story area (see `.claude/program.md` →
  LearnLab) before writing code.
- **Enforcement:** implementer prompt in `.claude/program.md`
- **Added:** 2026-10-23

### PR-learnlab-05 — E2E specs end with a screenshot assertion
- **Rule:** every Playwright spec ends with a screenshot assertion; snapshot folders are
  committed.
- **Enforcement:** harness /test Playwright patterns + `docs/tdd.md` → Test Levels
- **Added:** 2026-10-23

### PR-learnlab-06 — coverage reports go to reports/
- **Rule:** coverage reports are written to `reports/` (`reports/coverage.xml`,
  `reports/lcov.info`), never only to `coverage/` or `htmlcov/`.
- **Enforcement:** pytest-cov and Vitest config (created in sprint 1) + `docs/tdd.md` → Coverage
- **Added:** 2026-10-23
