# E2E (e2e/)

- Run: `npx playwright test`.
- Test titles start with `AC-NN`.
- Each spec ends with `await expect(page).toHaveScreenshot();`.
- Snapshot folders are committed.
- Log in with the seed accounts from [specs/app_spec.md](../specs/app_spec.md) §10. Use dummy data only.
