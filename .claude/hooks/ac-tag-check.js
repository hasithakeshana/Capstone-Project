#!/usr/bin/env node
'use strict';

// PostToolUse(Write|Edit|MultiEdit) — every test carries a literal AC-NN or NFR-NN id (PR-learnlab-03).
// Checks tests/**/test_*.py, frontend/**/*.test.ts(x) and e2e/**/*.spec.ts(x).
// Skips tests/architecture/fixtures/ (fixtures, not tests).
// Reads the file from disk when it exists; otherwise uses the text in the tool input.

const fs = require('fs');
const path = require('path');

const ID = /(AC|NFR)-\d{2}/;
const JS_TEST = /\b(?:test|it)(?:\.(?:only|skip|fails|todo))?\(\s*(['"`])(.*?)\1/g;
const FIXTURES = /^tests\/architecture\/fixtures\//;
const SCOPES = [
  { re: /^tests\/(?:.*\/)?test_[^/]*\.py$/, kind: 'py' },
  { re: /^frontend\/(?:.*\/)?[^/]*\.test\.tsx?$/, kind: 'js' },
  { re: /^e2e\/(?:.*\/)?[^/]*\.spec\.tsx?$/, kind: 'js' },
];

function projectDir() {
  return process.env.CLAUDE_PROJECT_DIR || process.cwd();
}

function writtenText(input) {
  if (typeof input.content === 'string') return input.content;
  if (typeof input.new_string === 'string') return input.new_string;
  if (Array.isArray(input.edits)) return input.edits.map((e) => e.new_string || '').join('\n');
  return '';
}

function lineOf(text, index) {
  return text.slice(0, index).split('\n').length;
}

function pyTagged(lines, def, prevDefLine) {
  const decorators = lines.slice(prevDefLine + 1, def.i).filter((l) => l.trim().startsWith('@'));
  const doc = lines.slice(def.i + 1, def.i + 4).join('\n');
  if (ID.test(decorators.join('\n')) || ID.test(doc)) return true;
  return def.name.startsWith('test_arch_') && /Architecture:/.test(doc);
}

function pyUntagged(content) {
  const lines = content.split('\n');
  const defs = [];
  lines.forEach((line, i) => {
    const m = /^\s*(?:async\s+)?def\s+(test_\w+)/.exec(line);
    if (m) defs.push({ i, name: m[1] });
  });
  return defs
    .map((def, k) => ({ def, prev: k === 0 ? -1 : defs[k - 1].i }))
    .filter(({ def, prev }) => !pyTagged(lines, def, prev))
    .map(({ def }) => ({ line: def.i + 1, name: def.name }));
}

function jsUntagged(content) {
  return [...content.matchAll(JS_TEST)]
    .filter((m) => !ID.test(m[2]))
    .map((m) => ({ line: lineOf(content, m.index), name: m[2] }));
}

function fail(rel, untagged) {
  const rows = untagged.map((u) => `  - line ${u.line}: ${u.name}`).join('\n');
  fs.writeSync(2, `ac-tag-check: untagged tests in ${rel}:\n${rows}\n`);
  fs.writeSync(2, 'Add the literal AC-NN (or NFR-NN) id to the marker, docstring or title (PR-learnlab-03).\n');
  return 2;
}

function checkTarget(input) {
  const file = input.file_path;
  const rel = path.relative(projectDir(), file).split(path.sep).join('/');
  if (FIXTURES.test(rel)) return 0;
  const scope = SCOPES.find((s) => s.re.test(rel));
  if (!scope) return 0;
  const content = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : writtenText(input);
  const untagged = scope.kind === 'py' ? pyUntagged(content) : jsUntagged(content);
  return untagged.length ? fail(rel, untagged) : 0;
}

function main() {
  const raw = fs.readFileSync(0, 'utf8');
  try {
    const input = JSON.parse(raw).tool_input || {};
    return input.file_path ? checkTarget(input) : 0;
  } catch {
    fs.writeSync(2, 'ac-tag-check: warning: could not parse hook input.\n');
    return 0;
  }
}

process.exitCode = main();
