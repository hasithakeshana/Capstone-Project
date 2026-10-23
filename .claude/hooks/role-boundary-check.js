#!/usr/bin/env node
'use strict';

// PostToolUse(Write|Edit|MultiEdit) — role check at the controller layer (NFR-04).
// Checks src/controllers/**/*.py. Every route decorator needs a require_role( dependency,
// except /health, register and login.
// Reads the file from disk when it exists; otherwise uses the text in the tool input.

const fs = require('fs');
const path = require('path');

const ROUTE = /@\w+\.(get|post|put|patch|delete)\(\s*(['"])([^'"]*)\2/g;
const SCOPE = /^src\/controllers\/(?:.*\/)?[^/]*\.py$/;
const EXEMPT_LAST = new Set(['register', 'login']);

function projectDir() {
  return process.env.CLAUDE_PROJECT_DIR || process.cwd();
}

function writtenText(input) {
  if (typeof input.content === 'string') return input.content;
  if (typeof input.new_string === 'string') return input.new_string;
  if (Array.isArray(input.edits)) return input.edits.map((e) => e.new_string || '').join('\n');
  return '';
}

function isExempt(route) {
  if (route === '/health') return true;
  const last = route.replace(/\/+$/, '').split('/').pop();
  return EXEMPT_LAST.has(last);
}

function signatureEnd(content, from) {
  const def = /def\s+\w+\s*\(/.exec(content.slice(from));
  if (!def) return content.length;
  const start = from + def.index;
  const close = /\)\s*(->[^:\n]*)?:/.exec(content.slice(start));
  return close ? start + close.index + close[0].length : content.length;
}

function untaggedRoutes(content) {
  const bad = [];
  for (const m of content.matchAll(ROUTE)) {
    if (isExempt(m[3])) continue;
    const region = content.slice(m.index, signatureEnd(content, m.index));
    if (!region.includes('require_role(')) {
      const line = content.slice(0, m.index).split('\n').length;
      bad.push({ line, method: m[1].toUpperCase(), route: m[3] });
    }
  }
  return bad;
}

function fail(rel, bad) {
  const rows = bad.map((b) => `  - line ${b.line}: ${b.method} ${b.route}`).join('\n');
  process.stderr.write(`role-boundary-check: route without require_role(...) in ${rel} (NFR-04):\n${rows}\n`);
  process.stderr.write('Add a require_role(...) dependency. Only /health, register and login are exempt.\n');
  return 2;
}

function checkTarget(input) {
  const file = input.file_path;
  const rel = path.relative(projectDir(), file).split(path.sep).join('/');
  if (!SCOPE.test(rel)) return 0;
  const content = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : writtenText(input);
  const bad = untaggedRoutes(content);
  return bad.length ? fail(rel, bad) : 0;
}

function main() {
  const raw = fs.readFileSync(0, 'utf8');
  try {
    const input = JSON.parse(raw).tool_input || {};
    return input.file_path ? checkTarget(input) : 0;
  } catch {
    process.stderr.write('role-boundary-check: warning: could not parse hook input.\n');
    return 0;
  }
}

process.exitCode = main();
