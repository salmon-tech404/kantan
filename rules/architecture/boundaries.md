---
area: architecture
path: rules/architecture/boundaries.md
rules: 5
---
### ARCH-DDD-002 · `must` · T1 critical
> applies_to: `any`
**Anti-Corruption Layer (ACL) for External Services**

Third-party APIs (e.g. Gemini, DeepSeek, S3) must be isolated behind an Anti-Corruption Layer (ACL) that translates vendor payloads into internal domain models.

How to: Wrap external clients in adapter classes (e.g., GeminiEmbeddingAdapter) implementing an internal interface (IEmbeddingService).

✗ Passing GoogleGenAI.GenerateContentResponse directly through controllers and services.
✓ interface IEmbeddingService { embed(text: string): Promise<number[]>; }

**Why:** Directly exposing external schemas in application code tightly couples the codebase to third-party vendor contracts, making provider switching or SDK upgrades painful.


### ARCH-DDD-005 · `must` · T1 critical
> applies_to: `hexagonal`
**Ports & Adapters (Hexagonal) Architecture for Domain-Model Business Logic**

Where business logic is implemented with the Domain Model pattern (complex invariants, not simple CRUD), the business logic must not depend on any infrastructure layer directly. Infrastructure (database, message bus, external APIs) must implement "port" interfaces defined by and owned by the business logic, with concrete "adapters" plugged in from the outside.

How to: Define repository/gateway interfaces (ports) inside the domain/application layer (e.g. `IKnowledgeBaseRepository`); implement them in the infrastructure layer (e.g. `PrismaKnowledgeBaseRepository`) and inject the concrete adapter at composition root.

✗ Domain service class directly importing `PrismaClient` and constructing SQL-shaped queries inline with business rule evaluation.
✓ interface IKnowledgeBaseRepository { findById(id: string): Promise<KnowledgeBase>; } // port owned by domain; PrismaKnowledgeBaseRepository implements it as the adapter

**Why:** In a traditional layered architecture, the domain layer depends downward on infrastructure, so infrastructure changes (swapping ORMs, message brokers) ripple into business logic and business logic can't be tested without


### ARCH-LAY-001 · `must` · T2 needs review
> applies_to: `layered`
**Layer Isolation: Requests Flow Through the Defined Layers**

In a module that uses the layered style, a request must flow through the layers the project defines (default: Route → Controller → Service → Repository). A layer must not reach past the next layer to the database or an external client. Route handlers and controllers in particular must not call the database directly.

Exception (open layer): a project may declare one layer open, so callers may skip it, for read-only queries that carry no business logic (see `ARCH-SINK-001`). The open layer must be declared in the profile's Architecture section. Skipping a layer that is not declared open is a violation.

How to: The handler calls a service method; only the repository touches the database client.

✗ `export async function getDoc(req, res) { const doc = await prisma.document.findUnique(...); res.json(doc); }` (TypeScript/Express example; handler calls the database)
✓ `export async function getDoc(req, res) { const doc = await docService.get(req.params.id); res.json(doc); }`

Does not apply to projects declaring `hexagonal` or another style; those follow their own dependency rule (see `ARCH-DDD-005`).

**Why:** Bypassing layers prevents centralized security filtering, audit logging, transaction demarcation, and data normalization.


### ARCH-MOD-002 · `must` · T1 critical
> applies_to: `any`
**Low Coupling and Explicit Module Contracts**

Inter-module dependencies must be strictly decoupled and accessed exclusively through exported public service interfaces or event contracts, never reaching into internal sub-paths.

How to: Export a single index.ts or clear Service class per module. Never deep-import into internal helpers of another module.

✗ import { internalParser } from '@/modules/documents/internal/parsers/pdf-ast';
✓ import { DocumentService } from '@/modules/documents';

**Why:** Direct deep imports create hidden connascence and fragile coupling, causing internal refactorings of one module to cascade into compilation failures across the codebase.


### ARCH-MONO-001 · `must` · T2 needs review
> applies_to: `domain-partitioned`
**Modular Monolith Domain-Driven Partitioning**

Monolithic backends must partition code by domain/feature boundaries rather than technical layers, encapsulating data schemas, logic, and endpoints together.

How to: Group code under src/modules/auth/, src/modules/documents/, src/modules/rag/, and src/modules/chat/.

✗ src/controllers/ (all controllers), src/services/ (all services) in flat horizontal buckets.
✓ src/modules/rag/ containing vector services, chunking logic, and similarity query routes.

**Why:** Domain partitioning allows individual features to evolve independently, maintains high cohesion, and simplifies future extraction into separate services.

