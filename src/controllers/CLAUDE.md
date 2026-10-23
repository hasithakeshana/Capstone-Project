# Controllers (src/controllers/)

- Keep routes thin: check the caller's role, call a service, return the result. No business logic.
- Every route calls `require_role(...)`, except `/health`, register and login (NFR-04).
- Never import repositories directly. Architecture tests enforce this.
- Every protected route has a role-boundary test in `tests/controllers/` (wrong role → 403, no token → 401).
