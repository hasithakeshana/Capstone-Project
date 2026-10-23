# Controllers (src/controllers/)

- Keep routes thin: check the caller's role, call a service, return the result. No business logic.
- Every route calls `require_role(...)`, except `/health`, register and login (NFR-04).
- Never import repositories directly. Architecture tests enforce this.
