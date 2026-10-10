---
area: architecture
path: architecture/conflicts.md
---

Resolution when two principles are both correct but you can only choose one.

## DRY (Clean Code) vs Bounded Context Autonomy (Domain-Driven Design) · `CONF-002`

- **DRY (Don't Repeat Yourself)** — Every piece of knowledge or code must have a single, unambiguous representation within a system.
- **Bounded Context Autonomy (DDD)** — Subsystems must maintain autonomous domain models to evolve independently without hidden coupling.

**Resolution:** SCOPE BOUNDARY RESOLUTION: Inside a single module/package, DRY is mandatory (no duplicate functions, no copy-pasted SQL). Across distinct Bounded Contexts (e.g. Ingestion Context vs Billing Context), DRY is intentionally suspended: duplicate DTOs and data models are preferred over creating a shared monolithic entity library that creates cross-team deployment coupling. Per the book's own guidance (see ddd-boundaries.framework.xml), Separate Ways should be avoided when integrating core subdomains — verify neither context is a core subdomain before applying this resolution.

## Hermetic In-Memory Isolation vs Real Database Vector Search Fidelity · `CONF-004`

- **Hermetic Unit Testing** — Tests must run with zero external network or database dependencies to remain fast and fully isolated from other tests — but most applications have at least one out-of-process dependency, typically the database, that can't be faithfully replaced with a mock.
- **Real Vector Search Fidelity** — In-memory database mocks do not support PostgreSQL pgvector Cosine similarity operators (<=>), leading to false-positive test passes. This is a Kantanda project-specific technical fact about pgvector, not a claim from any book in the current corpus.

**Resolution:** PYRAMID DIVISION RESOLUTION: Business domain logic, prompt formatting, and chunking algorithms use 100% Hermetic Unit Tests with in-memory Fakes. Repository vector queries are tested exclusively in Integration Tests executing against a real PostgreSQL instance with pgvector extension enabled, wrapped in transaction rollback.

## React Functional Immutability vs Real-Time High-Throughput Mutability · `CONF-003`

- **Functional Immutability (React / Redux)** — State objects must never be mutated in place; create new object copies to maintain pure render cycles.
- **High-Throughput Performance (Low-Latency Streaming Engine)** — Creating millions of short-lived objects per second triggers Garbage Collection (GC) pauses, causing latency spikes and dropped events.

**Resolution:** PROFILE DOMAIN RESOLUTION: In Standard Web UI and general application components, Functional Immutability is strictly enforced. In High-Throughput / Low-Latency Streaming Cores, in-memory ring buffers and pre-allocated object pools use mutable in-place updates within synchronized thread-safe boundaries to achieve zero-allocation <1ms latency.

##  · ``

- **** — In-process locking avoids the network round-trip inherent to a distributed lock, but intrinsic locks are themselves costly (Clean Code Ch.13/Appendix A explicitly warns "locks are expensive"); this trade-off is about avoiding network I/O, not about locks being cheap or easy to mock.
- **** — Modern backend services are horizontally scaled and stateless. In-memory locks exist exclusively within a single process heap and are completely invisible across multi-pod load-balanced deployments.

**Resolution:** 

## Postel's Law (Lenience) vs Secure APIs (Strict Validation) · `CONF-001`

- **Postel's Law (Robustness Principle)** — Be liberal in what you accept: tolerate varied inputs, strip whitespace, coerce formats to provide seamless UX — applied at the UI/form layer as accepting varied input formats and normalizing rather than hard-rejecting.
- **Secure APIs (Zero Trust / Anti-Mass-Assignment)** — Strict schema validation: reject any unrecognized parameters, strip extraneous fields, prevent injection.

**Resolution:** LAYERED CONTEXTUAL RESOLUTION: Postel's Law applies exclusively at the Frontend UI Client layer (e.g. forgiving date formats, trimming leading spaces). Secure APIs Strict Validation applies categorically at the Backend API Gateway / Controller boundary (Zod strict mode, rejecting unknown body parameters). The API boundary must never be lenient.
