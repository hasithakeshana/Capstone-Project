#!/usr/bin/env node
'use strict';

// PreToolUse(Write|Edit|MultiEdit) — append-only records (NFR-02, DR-9).
// Checks src/repositories/ and migrations/ only. Blocks update or delete code for
// enrollments, lesson completions and quiz attempts: SQL UPDATE/DELETE on those tables,
// and ORM forms that name one of those models (session.delete, query(Model)...update/delete,
// update(Model), delete(Model)). A plain ".update(" with no model name is not blocked.

const fs = require('fs');
const path = require('path');

const SCOPE = /^(src\/repositories|migrations)\//;
const MODEL_NAMES = 'Enrollment|LessonCompletion|QuizAttempt';
const TABLES = 'enrollments|lesson_completions|quiz_attempts';
const MODEL = new RegExp(`\\b(${MODEL_NAMES})\\b`);
const SQL_CHECKS = [
  new RegExp(`\\bUPDATE\\s+["\`']?(${TABLES})\\b`, 'i'),
  new RegExp(`\\bDELETE\\s+FROM\\s+["\`']?(${TABLES})\\b`, 'i'),
];
const ORM_CHECKS = [
  new RegExp(`\\bquery\\(\\s*(${MODEL_NAMES})\\s*\\)[\\s\\S]{0,200}?\\.(update|delete)\\(`),
  new RegExp(`\\b(update|delete)\\(\\s*(${MODEL_NAMES})\\b`),
  /\bsession\.delete\(/,
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

function existingText(input, file) {
  // Write replaces the whole file, so only Edit and MultiEdit keep the old content.
  if (input.content !== undefined || !fs.existsSync(file)) return '';
  return fs.readFileSync(file, 'utf8');
}

function mutatesRecords(text, context) {
  if (SQL_CHECKS.some((re) => re.test(text))) return true;
  if (!MODEL.test(context)) return false;
  return ORM_CHECKS.some((re) => re.test(text));
}

function main() {
  const raw = fs.readFileSync(0, 'utf8');
  let input;
  try {
    input = JSON.parse(raw).tool_input || {};
  } catch {
    process.stderr.write('attempt-immutability-check: warning: could not parse hook input.\n');
    return 0;
  }
  if (!input.file_path) return 0;
  const rel = path.relative(projectDir(), input.file_path).split(path.sep).join('/');
  if (!SCOPE.test(rel)) return 0;
  const text = writtenText(input);
  const context = `${existingText(input, input.file_path)}\n${text}`;
  if (!mutatesRecords(text, context)) return 0;
  process.stderr.write(`attempt-immutability-check: update/delete on enrollments, lesson completions or quiz attempts in ${rel}.\n`);
  process.stderr.write('These records are append-only (NFR-02). Remove the update or delete.\n');
  return 2;
}

process.exitCode = main();
