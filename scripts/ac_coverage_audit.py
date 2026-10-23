#!/usr/bin/env python3
"""Semantic AC coverage: do the tests tagged with an AC cover its spec scenarios?

Uses the Claude Agent SDK (claude-agent-sdk). Claude may use only Read, Grep and Glob.
The SDK is imported only when a judgement is requested, so the pure functions and the
tests run without it.

Usage:
    python scripts/ac_coverage_audit.py                       # every AC in specs/app_spec.md
    python scripts/ac_coverage_audit.py --ac AC-01 --ac AC-02 # repeatable
    python scripts/ac_coverage_audit.py --model claude-haiku-5-5

Writes reports/ac-semantic-coverage.md.
Exit codes: 0 = no MISSING scenario, 1 = at least one MISSING, 2 = setup error.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import NoReturn

ROOT = Path(__file__).resolve().parent.parent
APP_SPEC = ROOT / "specs" / "app_spec.md"
REPORT = ROOT / "reports" / "ac-semantic-coverage.md"
TEST_DIRS = ("tests", "frontend/src", "e2e")
SUFFIXES = {".py", ".ts", ".tsx"}
STATUSES = ("COVERED", "PARTIAL", "MISSING")
DEFAULT_MODEL = "claude-haiku-5-5"
SYSTEM_PROMPT = "You are a strict test reviewer. Judge only against the spec scenarios."
READ_ONLY_TOOLS = ["Read", "Grep", "Glob"]
MAX_TURNS = 5
MAX_BUDGET_USD = 0.50


@dataclass
class Row:
    ac: str
    scenario: str
    status: str
    evidence: str
    gap: str


def ac_index(spec_text: str) -> dict[str, Path]:
    """Map each AC id to its feature spec, from the 'Detail: specs/...md' part of its line."""
    found: dict[str, Path] = {}
    for line in spec_text.splitlines():
        ac = re.match(r"- \*\*(AC-\d{2}):\*\*", line)
        detail = re.search(r"Detail: (specs/\S+?\.md)", line)
        if ac and detail:
            found[ac.group(1)] = ROOT / detail.group(1)
    return found


def scenarios(spec_path: Path, ac: str) -> list[str]:
    """Return the Given lines under the '### AC-NN' heading of a feature spec."""
    out: list[str] = []
    inside = False
    for line in spec_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            inside = line.startswith(f"### {ac} ")
        elif inside and line.startswith("- Given"):
            out.append(line[2:])
    return out


def tagged_snippets(ac: str) -> list[str]:
    """Files and matching lines that carry the literal AC id as a whole word."""
    pattern = re.compile(rf"(?<![\w-]){re.escape(ac)}(?![\w-])")
    blocks: list[str] = []
    for folder in TEST_DIRS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix not in SUFFIXES or "node_modules" in path.parts:
                continue
            lines = path.read_text(encoding="utf-8").splitlines()
            hits = [line.strip()[:160] for line in lines if pattern.search(line)]
            if hits:
                blocks.append(f"{path.relative_to(ROOT).as_posix()}:\n  " + "\n  ".join(hits[:10]))
    return blocks


def build_prompt(ac: str, items: list[str], snippets: list[str]) -> str:
    """Build the judging prompt: numbered scenarios, tagged tests, and the answer format."""
    numbered = "\n".join(f"S{i}: {text}" for i, text in enumerate(items, 1))
    return (
        f"AC: {ac}\n\nSpec scenarios:\n{numbered}\n\n"
        "Tests tagged with this AC id (file and matching lines):\n"
        + "\n".join(snippets)
        + "\n\nFor each scenario, answer COVERED (a tagged test asserts this behaviour), "
        "PARTIAL (some of it is asserted), or MISSING (no test asserts it). "
        "Use Read, Grep or Glob on the files above if you need detail. "
        "Answer with only a JSON array: "
        '[{"scenario": "S1", "status": "COVERED|PARTIAL|MISSING", "evidence": "test name or file", "gap": "one line"}]'
    )


def parse_rows(answer: str) -> dict[str, dict[str, object]]:
    """Return the judged rows keyed by scenario id (S1, S2, ...). Empty if no valid array."""
    match = re.search(r"\[.*\]", answer, re.DOTALL)
    if not match:
        return {}
    try:
        rows = json.loads(match.group(0))
    except json.JSONDecodeError:
        return {}
    return {str(r.get("scenario")): r for r in rows if isinstance(r, dict)}


def to_status(value: object) -> str:
    """Return COVERED, PARTIAL or MISSING. Any other value counts as MISSING."""
    text = str(value).upper()
    return text if text in STATUSES else "MISSING"


def exit_code(rows: list[Row]) -> int:
    """Return 1 if any scenario is MISSING, otherwise 0."""
    return 1 if any(r.status == "MISSING" for r in rows) else 0


def cell(text: str) -> str:
    """Escape a pipe so it does not break the markdown table."""
    return text.replace("|", "\\|")


def write_report(rows: list[Row]) -> None:
    counts = {status: sum(1 for r in rows if r.status == status) for status in STATUSES}
    lines = [
        "# AC semantic coverage (Claude Agent SDK)",
        "",
        "| AC | scenario | status | evidence | gap |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| {r.ac} | {cell(r.scenario)} | {r.status} | {cell(r.evidence)} | {cell(r.gap)} |" for r in rows]
    lines += ["", "## Summary", ""] + [f"- {status}: {counts[status]}" for status in STATUSES]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fail_setup(message: str) -> NoReturn:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def import_sdk() -> ModuleType:
    """Import the SDK on first use. A missing SDK is a setup error (exit 2)."""
    try:
        import claude_agent_sdk
    except ImportError:
        fail_setup("claude-agent-sdk is not installed. Run: pip install -r scripts/requirements.txt")
    return claude_agent_sdk


def make_options(sdk: ModuleType, model: str) -> object:
    return sdk.ClaudeAgentOptions(
        tools=READ_ONLY_TOOLS,
        allowed_tools=READ_ONLY_TOOLS,
        max_turns=MAX_TURNS,
        model=model,
        cwd=str(ROOT),
        system_prompt=SYSTEM_PROMPT,
        max_budget_usd=MAX_BUDGET_USD,
    )


async def collect_text(sdk: ModuleType, prompt: str, options: object) -> str:
    text: list[str] = []
    async for message in sdk.query(prompt=prompt, options=options):
        if isinstance(message, sdk.AssistantMessage):
            text.extend(block.text for block in message.content if isinstance(block, sdk.TextBlock))
    return "\n".join(text)


async def judge(prompt: str, model: str) -> str:
    """Ask Claude to judge one AC with read-only tools. Setup and API errors exit with code 2."""
    sdk = import_sdk()
    options = make_options(sdk, model)
    try:
        return await collect_text(sdk, prompt, options)
    except sdk.CLINotFoundError:
        fail_setup("the Claude Code CLI was not found. Install Claude Code, then run again.")
    except Exception as exc:  # noqa: BLE001 - any SDK error (credentials, network, budget) is a setup error
        fail_setup(f"could not get a judgement from Claude ({exc}). "
                   "Set ANTHROPIC_API_KEY or log in with Claude Code, then run again.")


async def audit_ac(ac: str, spec_path: Path, model: str) -> list[Row]:
    items = scenarios(spec_path, ac)
    if not items:
        return [Row(ac, "-", "MISSING", "-", "no scenarios found in the feature spec")]
    snippets = tagged_snippets(ac)
    if not snippets:
        return [Row(ac, text, "MISSING", "-", "no test carries the AC id") for text in items]
    judged = parse_rows(await judge(build_prompt(ac, items, snippets), model))
    rows: list[Row] = []
    for i, text in enumerate(items, 1):
        r = judged.get(f"S{i}", {})
        rows.append(Row(
            ac,
            text,
            to_status(r.get("status", "MISSING")),
            str(r.get("evidence", "-")),
            str(r.get("gap", "no judgement returned")),
        ))
    return rows


async def audit(acs: list[str], index: dict[str, Path], model: str) -> list[Row]:
    rows: list[Row] = []
    for ac in acs:
        if ac not in index:
            fail_setup(f"{ac} is not listed in specs/app_spec.md")
        rows.extend(await audit_ac(ac, index[ac], model))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Semantic AC coverage with the Claude Agent SDK.")
    parser.add_argument("--ac", action="append", help="AC id, repeatable (default: every AC in app_spec.md)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"model id (default: {DEFAULT_MODEL})")
    args = parser.parse_args()
    index = ac_index(APP_SPEC.read_text(encoding="utf-8"))
    acs = args.ac or list(index)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("note: ANTHROPIC_API_KEY is not set; the run needs a Claude Code login.", file=sys.stderr)
    rows = asyncio.run(audit(acs, index, args.model))
    write_report(rows)
    missing = sum(1 for r in rows if r.status == "MISSING")
    print(f"wrote {REPORT.relative_to(ROOT).as_posix()}: {len(rows)} scenarios, {missing} MISSING")
    return exit_code(rows)


if __name__ == "__main__":
    sys.exit(main())
