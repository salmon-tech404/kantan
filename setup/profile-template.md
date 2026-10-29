---
project: <Project Name>
kantanda: 3.0.0
updated: <YYYY-MM-DD>
---

# Profile — <Project Name>

> Place this file **in your project's repository**, not in Kantanda.
> It is the source of truth for your project's specifics. Kantanda holds the common parts.

## 1. Stack

| | |
|---|---|
| Frontend | |
| Backend | |
| Database | |
| AI / LLM | |
| Verify Command | `npm run verify` |

Record actual versions from `package.json`, not from memory.

## 2. Kantanda Modules

| Module | Enabled | Why |
|---|---|---|
| base (default) | ✅ required | |
| `rag-pgvector` | ☐ | |
| `python-ml` | ☐ | |

Disabled modules mean agents **won't read** the corresponding files.

## 3. Architecture

Declare the style per package. Architecture rules (`ARCH-*`, `FE-ARCH-*`) apply only when their `applies_to` matches (`any` always applies). See `rules/architecture/styles.md` for values and the rule-to-style map.

| Package / path | Partitioning | Dependency style | Other (`domain-model`, `feature-slice`, `stack:...`) |
|---|---|---|---|
| | | | |

If a layered package uses an open layer (callers may skip it for simple reads, see `ARCH-LAY-001`), name it here: `layered (open: query service)`.

Choosing or changing a style is an ADR (`{{adr_path}}`), not a profile edit made in passing.

## 4. Parameters

| Parameter | Value | Notes |
|---|---|---|
| `{{ownership_key}}` | | ownership column name in schema |
| `{{max_fn_lines}}` | | |
| `{{max_depth}}` | | |
| `{{touch_target}}` | | |
| `{{max_upload}}` | | |
| `{{access_ttl}}` | | |
| `{{refresh_ttl}}` | | |
| `{{adr_path}}` | | must be a path **not** in .gitignore |

If you enable `rag-pgvector`, also declare: `{{embedding_dims}}`, `{{chunk_words}}`, `{{chunk_overlap}}`, `{{async_size}}`, `{{async_pages}}`.

> `{{embedding_dims}}` must match the model in use. Using multiple models? State each one — different dimension counts between models cause silent search failures.

## 5. Overrides

Each row must have every column. No reason means it's not an override, it's deviation from standard.

| Rule ID | Change | Why | Expires (YYYY-MM-DD) | Approved by |
|---|---|---|---|---|
| | | | | |

An override past its expiry date no longer counts and the rule applies again. Renew it deliberately or remove the row. Permanent differences belong in Section 6 (Extensions) or in the Architecture section, not here.

You cannot override rules in the "Non-Negotiable" section of `AGENTS.md`.

**Row count in this table is a health indicator.** Many overrides mean either the common rule is wrong, or your project is out of standard. Review when exceeding 5 rows.

## 6. Extensions

Rules that exist only in this project. Use your own ID prefix (e.g. `VX-*`) to avoid conflicts with Kantanda IDs.

| ID | Tier | Description |
|---|---|---|
| | | |

## 7. Design Token Sources

| Type | Source of Truth |
|---|---|
| Colors, fonts, spacing, radius, shadow, motion | |
| Tiers per scale | |

Rules point to the source. Don't copy values into rules — copies drift out of sync.

## 8. Enforcement

| Tier | Tool | Command |
|---|---|---|
| T1 Block | | |
| Presubmit | | |
| Agent Hook | | |

## 9. Domain Invariants

Things you cannot break in this project, with reasons.

-
