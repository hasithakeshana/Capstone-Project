# Fix loops

A fix loop is one run where an agent or gate finds a failure, reproduces it, fixes it, checks the fix, and opens a PR. Record each loop in its own file, named `YYYY-MM-DD-short-title.md`.

## Template

```markdown
# <Title>

- **Failure detected:** which agent or gate found it, and the signal (for example, the sast job or the evaluator).
- **Reproduced:** the failing test or command, with its output line.
- **Fixed:** the commit hash and subject.
- **Validated:** the passing run (test command and result, or CI run link).
- **PR link:** the pull request URL.
- **Trace excerpt:** the short log lines that show the loop, with the secrets and PII removed.
```
