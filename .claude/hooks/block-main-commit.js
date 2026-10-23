#!/usr/bin/env node
'use strict';

// PreToolUse(Bash) — PR-Only Merge rule (CLAUDE.md → Git & PR workflow).
// Blocks git commit / git push while on main or master, and any push to them.
// When the branch cannot be read, it is treated as main (fail closed).

const fs = require('fs');
const { execSync } = require('child_process');

const COMMIT_OR_PUSH = /(^|[\s;&|(])git\s+(commit|push)(\s|$)/;
const PUSH_TO_MAIN = /(^|[\s;&|(])git\s+push\b[^;&|\n]*\b(main|master)\b/;
const MESSAGE = 'Blocked: no direct commits/pushes to main. Use a branch + PR.';

function currentBranch() {
  try {
    return execSync('git rev-parse --abbrev-ref HEAD', {
      cwd: process.env.CLAUDE_PROJECT_DIR || process.cwd(),
      stdio: ['ignore', 'pipe', 'ignore'],
      timeout: 3000,
    }).toString().trim();
  } catch {
    return null;
  }
}

function onProtectedBranch() {
  const branch = currentBranch();
  return branch === null || branch === 'HEAD' || branch === 'main' || branch === 'master';
}

function parseCommand(raw) {
  try {
    return { ok: true, text: String(JSON.parse(raw).tool_input?.command ?? '') };
  } catch {
    return { ok: false, text: raw };
  }
}

function main() {
  const raw = fs.readFileSync(0, 'utf8');
  const { ok, text } = parseCommand(raw);
  if (!ok) fs.writeSync(2, 'block-main-commit: warning: could not parse hook input.\n');
  if (!COMMIT_OR_PUSH.test(text)) return 0;
  if (PUSH_TO_MAIN.test(text) || onProtectedBranch()) {
    fs.writeSync(2, MESSAGE + '\n');
    return 2;
  }
  return 0;
}

process.exitCode = main();
