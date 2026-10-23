# Frontend (frontend/)

Run from `frontend/`: `npm test`, `npm run lint`, `npx tsc --noEmit`, `npm run build`.

- Responsive layout for mobile and desktop. No horizontal scroll at 375 px or 1280 px (sprint 1 PRD, NFR-11).
- Role-based views: learner, instructor and admin see only the screens for their role.
- All API calls go through one client module.
- Declare `@vitest/coverage-v8` as a dev dependency in `package.json`. Coverage goes to `reports/lcov.info`.
- Test titles start with `AC-NN …`.
