# Architecture

## Layer Hierarchy

LearnLab uses these layers, lowest first: **core → domain → repositories → services → controllers**. The layer roots are `src/`. The order is set in `project-manifest.json` → `architecture.layers`.

Full design: [docs/architecture.md](../docs/architecture.md). Cross-sprint invariants: [specs/design/constitution.md](../specs/design/constitution.md).

| Layer | Folder | Responsibility | May import from |
|-------|--------|----------------|-----------------|
| core | `src/core/` | Configuration and logging | Standard library and installed packages only. No other layer. |
| domain | `src/domain/` | Business rules: course states, enrollment, quiz grading, progress, access | Standard library only. No other layer, not even core. |
| repositories | `src/repositories/` | Reads and writes records in SQLite | domain, core |
| services | `src/services/` | Use cases: enroll, complete a lesson, submit a quiz | repositories, domain, core |
| controllers | `src/controllers/` | HTTP routes, role checks, request and response mapping | services, core. Never repositories. |

The manifest order is the harness gate's minimum (downward imports only). LearnLab is stricter: domain imports only the Python standard library — enforced by an import-linter forbidden contract (domain ↛ core, fastapi, sqlalchemy).

## One-Way Dependency Rule

Imports flow one way: controllers → services → repositories → domain. Core is used by controllers, services and repositories.

Violations:
- `domain` importing from core, repositories, services or controllers — FORBIDDEN
- `repositories` importing from services or controllers — FORBIDDEN
- `services` importing from controllers — FORBIDDEN
- `controllers` importing from repositories — FORBIDDEN (routes go through services)
- `core` importing from any other layer — FORBIDDEN

The manifest order (core, domain, repositories, services, controllers) would allow domain to import core. This file is stricter: domain imports nothing from other layers.

The `verify-on-save` hook enforces this rule on every file save; the git `pre-commit` gate re-checks staged files. If the layer gate matches no staged source file (the project doesn't follow a `<root>/<layer>/` layout), `pre-commit` warns loudly instead of silently passing — configure or disable the check via `project-manifest.json` (see Customization).

The import-linter contracts that enforce this rule are written in sprint 1 from `docs/architecture.md`. Until they run in the test gate, this section is a rule to follow, not a check.

## Verification Commands

Run from the repo root. These are quick local checks. The gate is `uv run lint-imports`.

```bash
# domain: standard library only
grep -rnE "^(from|import) (fastapi|sqlalchemy|core|repositories|services|controllers)" src/domain/
# repositories: no services or controllers
grep -rnE "^(from|import) (services|controllers)" src/repositories/
# services: no controllers
grep -rnE "^(from|import) controllers" src/services/
# controllers: no repositories
grep -rnE "^(from|import) repositories" src/controllers/
# core: no other layer
grep -rnE "^(from|import) (domain|repositories|services|controllers)" src/core/
```

## Cross-Cutting Concerns

The following concerns span all layers and are handled via shared utilities, not inline in each layer:

| Concern | Implementation |
|---------|---------------|
| **Logging** | Centralized logger (e.g., `src/lib/logger`) — all layers import from `lib`, not from each other |
| **Authentication** | Auth context passed via dependency injection or middleware; never hardcoded per-layer |
| **Telemetry** | Instrumentation via a shared `src/lib/telemetry` module with span/trace helpers |
| **Error Handling** | Typed error classes in `Types`; caught and mapped at `API` boundary; never swallowed silently |

## Bounded Contexts (Vertical Boundaries)

The layer check is horizontal; bounded contexts are its vertical complement. Two contexts (e.g., `src/billing`, `src/user`) may not reach into each other's internals — a cross-context import is allowed only via the target's public surface (its root, `index`, `public`, or `__init__`) or an explicit allow-edge.

This check is **opt-in**: it runs only when `project-manifest.json` declares `architecture.contexts` (see Customization). Both `verify-on-save` and the git `pre-commit` gate enforce it, after the layer check.

## Customization

Layer names, source roots, and bounded contexts are configured via the `architecture` block of `project-manifest.json` in the project root. Without a manifest (or without an `architecture` block), the defaults above apply: layers `types → config → repository → service → api → ui` under `src/`.

```json
{
  "architecture": {
    "layers": ["domain", "application", "infrastructure", "presentation"],
    "layer_roots": ["src", "backend/src"],
    "contexts": {
      "roots": ["src/billing", "src/user"],
      "allow": [["billing", "user"]],
      "public": ["index", "public", "__init__"]
    }
  }
}
```

- `layers` — layer names in order, **lowest to highest**; a layer may import only from layers earlier in the list.
- `layer_roots` — directories scanned for `<root>/<layer>/` paths (default `["src"]`).
- `contexts` — optional bounded-context rules: `roots` name the context directories, `allow` lists permitted cross-context edges (`["billing", "user"]` = billing may import user's internals), `public` overrides the default public-surface names.

To **disable** the layer check entirely — the right default for libraries, CLIs, data pipelines, and ML projects that don't follow a layered hierarchy — set `"architecture": { "enabled": false }` (or `"layers": []`). `/scaffold` sets this automatically for those project shapes.
