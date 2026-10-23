#!/usr/bin/env node
'use strict';

// PreToolUse(Write|Edit|MultiEdit) — course status changes only through the state machine (AC-08, NFR-08).
// Checks src/** except src/domain/ (the state machine lives there, so it is exempt).
// Blocks direct assignments such as "course.status = ..." or "course.state = ...",
// including seed code.

const fs = require('fs');
const path = require('path');

const SCOPE = /^src\//;
const DOMAIN = /^src\/domain\//;
const DIRECT_ASSIGN = /\b\w*course\w*\.(status|state)\s*=(?!=)/i;

function projectDir() {
  return process.env.CLAUDE_PROJECT_DIR || process.cwd();
}

function writtenText(input) {
  if (typeof input.content === 'string') return input.content;
  if (typeof input.new_string === 'string') return input.new_string;
  if (Array.isArray(input.edits)) return input.edits.map((e) => e.new_string || '').join('\n');
  return '';
}

function main() {
  const raw = fs.readFileSync(0, 'utf8');
  let input;
  try {
    input = JSON.parse(raw).tool_input || {};
  } catch {
    process.stderr.write('course-publish-gate: warning: could not parse hook input.\n');
    return 0;
  }
  if (!input.file_path) return 0;
  const rel = path.relative(projectDir(), input.file_path).split(path.sep).join('/');
  if (!SCOPE.test(rel) || DOMAIN.test(rel)) return 0;
  if (!DIRECT_ASSIGN.test(writtenText(input))) return 0;
  process.stderr.write(`course-publish-gate: course status/state changed outside the state machine in ${rel}.\n`);
  process.stderr.write('Use the course state machine in src/domain/.\n');
  return 2;
}

process.exitCode = main();
