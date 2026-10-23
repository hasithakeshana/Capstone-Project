# Frontend (frontend/)

Run from `frontend/`: `npm test`, `npm run lint`, `npx tsc --noEmit`, `npm run build`.

- Simple UI only: plain layouts, standard form and table controls. No animations, no custom component libraries, no complex visualisations.
- Responsive layout for mobile and desktop. No horizontal scroll at 375 px or 1280 px (sprint 1 PRD, NFR-11).
- Role-based views: learner, instructor and admin see only the screens for their role.
- All API calls go through one client module.
- Declare `@vitest/coverage-v8` as a dev dependency in `package.json`.
- Vitest coverage: provider v8, reporter lcov, `reportsDirectory: '../reports'` → `reports/lcov.info` at the repo root.
- Test titles start with `AC-NN (E1-S1-ACn): …`.
