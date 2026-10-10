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

## 3. Parameters

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

## 4. Overrides

Each row must have all three columns. No reason means it's not an override, it's deviation from standard.

| Rule ID | Change | Why |
|---|---|---|
| | | |

You cannot override rules in the "Non-Negotiable" section of `AGENTS.md`.

**Row count in this table is a health indicator.** Many overrides mean either the common rule is wrong, or your project is out of standard. Review when exceeding 5 rows.

## 5. Extensions

Rules that exist only in this project. Use your own ID prefix (e.g. `VX-*`) to avoid conflicts with Kantanda IDs.

| ID | Tier | Description |
|---|---|---|
| | | |

## 6. Design Token Sources

| Type | Source of Truth |
|---|---|
| Colors, fonts, spacing, radius, shadow, motion | |
| Tiers per scale | |

Rules point to the source. Don't copy values into rules — copies drift out of sync.

## 7. Enforcement

| Tier | Tool | Command |
|---|---|---|
| T1 Block | | |
| Presubmit | | |
| Agent Hook | | |

## 8. Domain Invariants

Things you cannot break in this project, with reasons.

-
