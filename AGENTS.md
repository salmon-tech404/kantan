# Kantanda — Unified Engineering Standards

A set of rules applying to every project. Each project declares its parameters and overrides in its own repository.

## How to Use (for AI Agents)

**Load only files for the area you're working on.** Don't read the entire tree. Don't read `_system/`.

| Task | Read File |
|---|---|
| Components, screens, styling, a11y | `frontend/ui.md` |
| Frontend structure, RSC, state, API calls | `frontend/architecture.md` |
| Frontend TypeScript types | `frontend/typescript.md` |
| Rendering AI/user-generated content | `frontend/security.md` |
| E2E tests, Playwright | `frontend/testing.md` |
| Endpoints, request validation, errors, responses | `backend/api.md` |
| Database queries, transactions, data access control | `backend/database.md` |
| Authentication, file upload, SSRF, rate limiting, logging, prompt injection | `backend/security.md` |
| Backend unit/integration tests | `backend/testing.md` |
| Module boundaries, layers, DDD, hexagonal | `architecture/boundaries.md` |
| Architectural decisions to document | `architecture/adr.md` |
| Naming, function length, formatting | `common/code-style.md` |
| Commits, CI gates, dependencies | `common/git.md` |
| Testing strategy, concurrent tests, idempotency | `common/testing.md` |
| Writing READMEs, technical guides, user documentation | `guide/writing.md` |

**Optional Modules** — read only when project profile enables:

| Module | File | Enable When |
|---|---|---|
| `rag-pgvector` | `backend/rag.md` | Project uses RAG, embeddings, vector search |
| `python-ml` | `backend/ml.md` | Project loads ML models or trains classifiers |

Files `*/guidance.md` are **recommendations, not rules**. Read only when considering design trade-offs, not as grounds for blocking.

## Priority Order for Conflicts

Two axes, evaluated in order:

**1. Scope — narrow wins over broad**
```
file conventions  >  project rules  >  optional modules  >  Kantanda
```

**2. Type — only when same scope**
```
Rank 1 Security & data integrity
Rank 2 Correctness & type safety
Rank 3 Maintainability
Rank 4 Performance (only if measured)
```

## Non-Negotiable Rules

Projects **cannot override** these rules, even if the profile declares an exception:

`BE-DB-001` `SEC-BOLA-002` `BE-VAL-001` `BE-VAL-002` `SEC-AUTH-003` `SEC-JWT-001`
`SEC-UPL-001` `SEC-SSRF-001` `SEC-RAT-001` `SEC-LOG-001` `BE-ERR-002` `SWE-DEP-001`

Overriding other rules must be explicitly declared in the project profile: **rule ID + what changed + why**. No declaration means the common rule still applies.

## Three Enforcement Tiers

Each rule carries a label:

| Label | Meaning | Tolerance |
|---|---|---|
| **T1 Automated Block** | Caught by lint/type/semgrep/tests | Near 0% — can block commits |
| **T2 Review Reminder** | Tooling catches partially, needs context | Under 10% — suggestion only |
| **T3 Guidance** | Not verifiable by tools | No blocking allowed |

T3 rules are **never** grounds to reject a change.

## Project Parameters to Declare

Rules containing `{{...}}` require projects to fill in values. See `_system/profile-template.md`.

| Parameter | Used By |
|---|---|
| `{{ownership_key}}` | BE-DB-001 — ownership column name (`userId` / `orgId` / `tenantId`) |
| `{{max_fn_lines}}` `{{max_depth}}` | CODE-FUN-002 |
| `{{touch_target}}` | UI-LAW-002 |
| `{{max_upload}}` | SEC-UPL-002 |
| `{{access_ttl}}` `{{refresh_ttl}}` | SEC-AUTH-001 |
| `{{adr_path}}` | ARCH-ADR-001 |
| `{{embedding_dims}}` `{{chunk_words}}` `{{chunk_overlap}}` `{{async_size}}` `{{async_pages}}` | module `rag-pgvector` |

## Design Tokens Not Defined Here

Kantanda requires **having** a finite, named scale for font sizes, colors, spacing, radius, shadow, motion — and forbids values outside the scale. Kantanda does **not** define what values that scale contains. That's each project's decision, declared in the profile and realized via design tokens.

## Before Finishing a Task

Run the verify command your project profile declares. Report the actual result, even if it fails.
