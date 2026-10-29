---
area: architecture
path: rules/architecture/adr.md
rules: 1
---
### ARCH-ADR-001 · `must` · T2 needs review
> applies_to: `any`
**Mandatory Architectural Decision Records (ADR) for Structural Decisions**

Any structural architectural decision that introduces new database engines, external protocols, communication patterns, or alters boundary contracts must be documented in a committed Architectural Decision Record (ADR).

How to: Record decisions under {{adr_path}}/NNNN-title.md containing: Title, Status, Context, Decision, and Consequences (positive and negative trade-offs).

✗ Switching from REST to WebSockets or adopting Redis without a documented ADR discussing connection scale and infrastructure costs.
✓ docs/adr/0004-use-pgvector-for-rag-embeddings.md documenting why pgvector was selected over standalone vector DBs.

**Why:** Architectural intent and trade-off rationales fade from team memory over time. Undocumented decisions lead to repeated debates and accidental architectural regression.

**Parameter:** `{{adr_path}}/NNNN-title.md`

