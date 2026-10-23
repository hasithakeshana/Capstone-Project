"""Tooling: tests for the pure functions in scripts/ac_coverage_audit.py.

No network and no SDK calls. Run from the repo root:
    uv run --with pytest python -m pytest scripts/test_ac_coverage_audit.py -q
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import ac_coverage_audit as aca

ROOT = Path(__file__).resolve().parent.parent

SPEC = """# Spec

### AC-01 Learner can register
- Given a visitor, When they register, Then an account exists.
- Given a registered learner, When they enroll, Then one enrollment exists.

### AC-02 Instructor can create a course
- Given an instructor, When they create a course, Then it is DRAFT.
"""


def test_tool_ac_index_maps_each_ac_to_its_feature_spec():
    """Tooling: every AC line in specs/app_spec.md maps to the feature spec in its Detail part."""
    index = aca.ac_index((ROOT / "specs" / "app_spec.md").read_text(encoding="utf-8"))
    assert len(index) == 10
    assert index["AC-05"] == ROOT / "specs" / "quiz-engine_spec.md"
    assert index["AC-10"] == ROOT / "specs" / "admin-console_spec.md"


def test_tool_ac_index_skips_ac_lines_without_a_detail_part():
    """Tooling: an AC line with no Detail part is not indexed."""
    assert aca.ac_index("- **AC-09:** an instructor can view progress.") == {}


def test_tool_scenarios_returns_the_given_lines_under_the_ac_heading(tmp_path: Path):
    """Tooling: only the Given lines under the matching ### AC heading are returned."""
    spec = tmp_path / "spec.md"
    spec.write_text(SPEC, encoding="utf-8")
    assert aca.scenarios(spec, "AC-01") == [
        "Given a visitor, When they register, Then an account exists.",
        "Given a registered learner, When they enroll, Then one enrollment exists.",
    ]


def test_tool_scenarios_stops_at_the_next_heading(tmp_path: Path):
    """Tooling: lines under a later AC heading are not returned for an earlier AC."""
    spec = tmp_path / "spec.md"
    spec.write_text(SPEC, encoding="utf-8")
    assert aca.scenarios(spec, "AC-02") == ["Given an instructor, When they create a course, Then it is DRAFT."]


def test_tool_parse_rows_reads_the_json_array_inside_prose():
    """Tooling: the judgement JSON array is found even when Claude wraps it in text."""
    answer = 'Result: [{"scenario": "S1", "status": "COVERED", "evidence": "test_ac01_x", "gap": "none"}] end'
    assert aca.parse_rows(answer)["S1"]["status"] == "COVERED"


def test_tool_parse_rows_returns_empty_for_unusable_answers():
    """Tooling: an answer with no valid JSON array gives no judgements."""
    assert aca.parse_rows("[not json") == {}
    assert aca.parse_rows("no array here") == {}


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("covered", "COVERED"), ("PARTIAL", "PARTIAL"), ("missing", "MISSING"), ("maybe", "MISSING"), (None, "MISSING")],
)
def test_tool_to_status_accepts_only_the_three_statuses(raw: object, expected: str):
    """Tooling: a judgement is COVERED, PARTIAL or MISSING; anything else counts as MISSING."""
    assert aca.to_status(raw) == expected


def test_tool_exit_code_is_1_only_when_a_scenario_is_missing():
    """Tooling: exit code 1 when any scenario is MISSING; PARTIAL alone is not a failure."""
    covered = aca.Row("AC-01", "s", "COVERED", "t", "-")
    partial = aca.Row("AC-02", "s", "PARTIAL", "t", "gap")
    missing = aca.Row("AC-03", "s", "MISSING", "-", "gap")
    assert aca.exit_code([covered]) == 0
    assert aca.exit_code([covered, partial]) == 0
    assert aca.exit_code([covered, missing]) == 1


def test_tool_build_prompt_numbers_each_scenario():
    """Tooling: the prompt lists each scenario as S1, S2, ... so the answer can refer to it."""
    prompt = aca.build_prompt("AC-01", ["first", "second"], ["tests/x.py:\n  AC-01"])
    assert "S1: first" in prompt
    assert "S2: second" in prompt


def test_tool_tagged_snippets_ignores_name_only_tags(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Tooling: a name like test_ac01_ does not count; the literal AC-01 in a docstring does."""
    tests = tmp_path / "tests"
    tests.mkdir()
    (tests / "test_name_only.py").write_text("def test_ac01_enroll():\n    assert True\n", encoding="utf-8")
    (tests / "test_literal.py").write_text('def test_enroll():\n    """AC-01 (E1-S1-AC2): x."""\n', encoding="utf-8")
    monkeypatch.setattr(aca, "ROOT", tmp_path)
    snippets = aca.tagged_snippets("AC-01")
    assert len(snippets) == 1
    assert "test_literal.py" in snippets[0]


def test_tool_cell_escapes_pipes_for_the_markdown_table():
    """Tooling: a pipe inside a cell does not break the markdown table."""
    assert aca.cell("a|b") == "a\\|b"
