#!/usr/bin/env bash
# sprint_close.sh — mechanical sprint evidence for LearnLab. No AI.
#   scripts/sprint_close.sh N          full close: reports/sprint-N-summary.md (exit 1 on BLOCKING)
#   scripts/sprint_close.sh --ac-only  AC tag table only: reports/ac-coverage.md (exit 0)
# Writes only under reports/ and specs/reviews/sprint-N/. Does not edit code, commit or push.
set -o pipefail

cd "$(dirname "$0")/.." || exit 2

ACS=(AC-01 AC-02 AC-03 AC-04 AC-05 AC-06 AC-07 AC-08 AC-09 AC-10)
TABLE="reports/ac-coverage.md"
BLOCKING=()
REMINDERS=()
MISSING_ACS=""
MISSING_COMMITS=()
COV_BACKEND="n/a"
COV_FRONTEND="n/a"
TEST_FILES=0
TEST_FUNCS=0
SRC_LINES=0
TOTAL_COMMITS=0
T_TEST=0
T_FEAT=0
T_REF=0

print_list() {
  if [ "$#" -eq 0 ]; then echo "- none"; return; fi
  for item in "$@"; do echo "- $item"; done
}

# Sprint N's ACs from specs/app_spec.md → Sprint Plan (S1, S2, S3). Other N: all ACs.
sprint_acs() {
  case "$1" in
    1) echo "AC-01 AC-02 AC-04 AC-08" ;;
    2) echo "AC-03 AC-07 AC-10" ;;
    3) echo "AC-05 AC-06 AC-09" ;;
    *) echo "${ACS[*]}" ;;
  esac
}

# Literal AC-NN as a whole word in test folders. A name like test_ac01_ alone does not count.
build_ac_table() {
  {
    echo "# AC coverage: literal AC-NN id"
    echo
    echo "Match: the literal AC-NN as a whole word in tests/, frontend/src/ or e2e/."
    echo
    echo "| AC | test files | count | status |"
    echo "|---|---|---|---|"
  } > "$TABLE"
  MISSING_ACS=""
  for ac in "${ACS[@]}"; do
    files=$(grep -rlw -- "$ac" tests frontend/src e2e 2>/dev/null | wc -l)
    lines=$(grep -rw -- "$ac" tests frontend/src e2e 2>/dev/null | wc -l)
    if [ "$lines" -gt 0 ]; then
      status="COVERED"
    else
      status="MISSING"
      MISSING_ACS="$MISSING_ACS $ac"
    fi
    echo "| $ac | $files | $lines | $status |" >> "$TABLE"
  done
}

block_missing_sprint_acs() {
  for ac in $(sprint_acs "$1"); do
    case " $MISSING_ACS " in
      *" $ac "*) BLOCKING+=("$ac has no test with the literal id") ;;
    esac
  done
}

copy_reviews() {
  mkdir -p "specs/reviews/sprint-$1"
  cp specs/reviews/*.md specs/reviews/*.json "specs/reviews/sprint-$1/" 2>/dev/null
}

run_coverage() {
  if [ -f pyproject.toml ] && [ -d tests ]; then
    uv run pytest --cov=src --cov-report=xml:reports/coverage.xml -q || BLOCKING+=("backend test run failed")
  else
    REMINDERS+=("backend coverage skipped: pyproject.toml or tests/ not present yet")
  fi
  if [ -f frontend/package.json ]; then
    (cd frontend && npm test -- --coverage) || BLOCKING+=("frontend test run failed")
  else
    REMINDERS+=("frontend coverage skipped: frontend/package.json not present yet")
  fi
}

check_backend_floor() {
  [ -f reports/coverage.xml ] || return
  rate=$(grep -o 'line-rate="[0-9.]*"' reports/coverage.xml | head -1 | grep -o '[0-9.]*')
  COV_BACKEND=$(awk -v r="${rate:-0}" 'BEGIN { printf "%.1f", r * 100 }')
  awk -v p="$COV_BACKEND" 'BEGIN { exit !(p < 80) }' && BLOCKING+=("backend line coverage ${COV_BACKEND}% is below 80%")
}

check_frontend_floor() {
  [ -f reports/lcov.info ] || return
  COV_FRONTEND=$(awk -F: '/^LF:/{f+=$2} /^LH:/{h+=$2} END { if (f > 0) printf "%.1f", h * 100 / f; else print "0.0" }' reports/lcov.info)
  awk -v p="$COV_FRONTEND" 'BEGIN { exit !(p < 80) }' && BLOCKING+=("frontend line coverage ${COV_FRONTEND}% is below 80%")
}

count_metrics() {
  TEST_FILES=$(find tests frontend/src e2e -type f \( -name 'test_*.py' -o -name '*.test.ts' -o -name '*.test.tsx' -o -name '*.spec.ts' -o -name '*.spec.tsx' \) 2>/dev/null | wc -l)
  TEST_FUNCS=$(grep -rhoE 'def test_|\b(test|it)\(' tests frontend/src e2e 2>/dev/null | wc -l)
  SRC_LINES=$(find src frontend/src -type f \( -name '*.py' -o -name '*.ts' -o -name '*.tsx' \) -not -path '*/node_modules/*' -print0 2>/dev/null | xargs -0 -r cat | wc -l)
}

check_git() {
  local branch base range commit direct
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  case "$branch" in
    main|master) BLOCKING+=("current branch is $branch: work on a branch, not main") ;;
  esac
  base=""
  git rev-parse --verify -q origin/main >/dev/null && base="origin/main"
  if [ -n "$base" ]; then
    direct=$(git rev-list --count "origin/main..main" 2>/dev/null)
    [ "${direct:-0}" -gt 0 ] && BLOCKING+=("$direct commit(s) on local main that are not on origin/main")
  fi
  range="${base:+$base..}HEAD"
  TOTAL_COMMITS=$(git rev-list "$range" 2>/dev/null | wc -l)
  T_TEST=$(git log --format=%s "$range" 2>/dev/null | grep -cE '^test\(')
  T_FEAT=$(git log --format=%s "$range" 2>/dev/null | grep -cE '^feat\(')
  T_REF=$(git log --format=%s "$range" 2>/dev/null | grep -cE '^refactor\(')
  for commit in $(git rev-list "$range" 2>/dev/null); do
    if ! git show -s --format=%B "$commit" | grep -q 'Co-Authored-By: Claude'; then
      MISSING_COMMITS+=("$(git log -1 --format='%h %s' "$commit")")
    fi
  done
  [ "${#MISSING_COMMITS[@]}" -gt 0 ] && BLOCKING+=("${#MISSING_COMMITS[@]} commit(s) without 'Co-Authored-By: Claude' (see Commits)")
}

run_pr_body() {
  if node .claude/scripts/pr-body.js --require-gate > "reports/pr-sprint-$1.md" 2> reports/pr-body.err; then
    return
  fi
  rm -f "reports/pr-sprint-$1.md"
  REMINDERS+=("PR body not written: the gate is not ready (see reports/pr-body.err)")
}

check_docs() {
  local dir rows
  for dir in docs/post-mortems docs/fix-loops; do
    if [ ! -d "$dir" ] || ! ls -A "$dir" | grep -v '^README\.md$' | grep -q .; then
      REMINDERS+=("$dir has no entries yet (only README.md, or empty)")
    fi
  done
  rows=$(grep -cE '^\|' docs/knowledge-deposits.md 2>/dev/null)
  if [ "${rows:-0}" -le 2 ]; then
    REMINDERS+=("docs/knowledge-deposits.md has no rows yet")
  fi
}

write_summary() {
  local out="reports/sprint-$1-summary.md"
  {
    echo "# Sprint $1 summary"
    echo
    echo "Generated $(date -u +%Y-%m-%dT%H:%MZ) by scripts/sprint_close.sh (no AI)."
    echo
    echo "## BLOCKING"
    print_list "${BLOCKING[@]}"
    echo
    echo "## REMINDERS"
    print_list "${REMINDERS[@]}"
    echo
    echo "## Acceptance criteria (literal id)"
    echo
    sed -n '/^| AC/,$p' "$TABLE"
    echo
    echo "## Metrics"
    echo
    echo "- test files: $TEST_FILES"
    echo "- test functions: $TEST_FUNCS"
    echo "- source lines (src + frontend/src): $SRC_LINES"
    echo "- backend line coverage: ${COV_BACKEND}%"
    echo "- frontend line coverage: ${COV_FRONTEND}%"
    echo
    echo "## Commits"
    echo
    echo "- commits in range: $TOTAL_COMMITS"
    echo "- test(: $T_TEST · feat(: $T_FEAT · refactor(: $T_REF"
    echo "- without Co-Authored-By: Claude:"
    print_list "${MISSING_COMMITS[@]}"
  } > "$out"
}

main() {
  local n="${1:-}"
  mkdir -p reports
  if [ "$n" = "--ac-only" ]; then
    build_ac_table
    echo "wrote $TABLE"
    exit 0
  fi
  case "$n" in
    ''|*[!0-9]*) echo "usage: $0 N | --ac-only" >&2; exit 2 ;;
  esac
  build_ac_table
  copy_reviews "$n"
  run_coverage
  check_backend_floor
  check_frontend_floor
  count_metrics
  check_git
  block_missing_sprint_acs "$n"
  run_pr_body "$n"
  check_docs
  write_summary "$n"
  echo "wrote reports/sprint-$n-summary.md"
  if [ "${#BLOCKING[@]}" -gt 0 ]; then
    echo "BLOCKING problems: ${#BLOCKING[@]}" >&2
    exit 1
  fi
  exit 0
}

main "$@"
