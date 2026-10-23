# Services (src/services/)

- Services run use cases: call domain rules, then repositories.
- No FastAPI or HTTP objects here. Controllers handle requests.
- One service per feature area.
- Business rules stay in `src/domain/`.
