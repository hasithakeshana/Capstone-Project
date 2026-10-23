# E2E (e2e/)

- Run: `npx playwright test`.
- Test titles start with `AC-NN (E1-S1-ACn): …`.
- Each spec ends with `await expect(page).toHaveScreenshot();`.
- Snapshot folders are committed.
- `playwright.config.ts` lives at the repo root (`testDir ./e2e`). Its `webServer` must start the local dev servers: backend uvicorn on :8000 and the Vite dev server on :5173. Never `docker compose`.
- If the harness copies `.github/workflows/e2e.yml`, adapt it to start the local dev servers too.
- Log in with the seed accounts from [specs/app_spec.md](../specs/app_spec.md) → Seed Data. Use dummy data only.
