---
area: common
path: rules/common/incidents.md
---

Real production incidents. Each entry is evidence for a rule — read to avoid repeating mistakes.

### INC-2026-001 · CRITICAL · 2026-08-15

- **Project:** RAG-Service
- **Symptom:** High-load document upload caused Redis workers to crash with Out-of-Memory (OOM) errors.
- **Root Cause:** Workers ingested 50MB PDFs directly into memory as whole buffers rather than stream chunking.
- **Rule That Would Have Prevented It:** `RAG-ING-002`

  RAG-ING-002 (Streaming / Bounded-Buffer Parsing for Large Document Ingestion) was added 2026-09-15 to close this exact gap: it requires page-by-page/row-by-row incremental parsing with a hard memory cap, independent of the file-size dispatch threshold (RAG-ASY-001) or rate limiting (SEC-RAT-001). RAG-CHK-001 still only chunks text already resident in memory and remains structurally unable to preve

### INC-2026-002 · CRITICAL · 2026-09-02

- **Project:** Core-Transactions
- **Symptom:** Concurrent wallet withdrawal requests allowed balance to drop below zero (lost update race condition).
- **Root Cause:** Service verified balance in-memory without row-level locking (SELECT FOR UPDATE) before issuing update statement.
- **Rule That Would Have Prevented It:** `FW-CON-001 (Branch 2: Pessimistic Row-Level Locking)`

  frameworks/database-concurrency.framework.xml Branch 2 requires SELECT ... FOR UPDATE inside a short transaction for exactly this class of high-contention balance/inventory mutation. BE-DB-002 (prisma.$transaction wrapping for multi-table writes) alone does not prevent this incident: wrapping a read-then-write in a plain transaction does not stop two concurrent transactions from both reading the s

### INC-2026-003 · MINOR · 2026-10-08

- **Project:** veltrix-ai (AI Composer, Clarify step)
- **Symptom:** Option cards showed a tinted brand background, a brand border and a checkmark at the same time; choosing a different option removed the "AI suggested" badge and its rationale line, so the content below jumped up.
- **Root Cause:** The agent copied the existing selected-state classes from other screens without evaluating them, and rendered the rationale line only while the current value equalled the AI suggestion. No Kantanda rule covered selected-state styling or interaction-driven layout shift.
- **Rule That Would Have Prevented It:** `UI-SEL-001`, `UI-STB-001`

  Both rules were added 2026-10-08 from this incident, after checking WCAG 1.4.1 / 1.4.11 and web.dev CLS guidance.

