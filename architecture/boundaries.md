---
area: architecture
path: architecture/boundaries.md
rules: 5
---
### ARCH-DDD-002 · `must` · T1 critical
**Anti-Corruption Layer (ACL) for External Services**

Third-party APIs (e.g. Gemini, DeepSeek, S3) must be isolated behind an Anti-Corruption Layer (ACL) that translates vendor payloads into internal domain models.

How to: Wrap external clients in adapter classes (e.g., GeminiEmbeddingAdapter) implementing an internal interface (IEmbeddingService).

✗ Passing GoogleGenAI.GenerateContentResponse directly through controllers and services.
✓ interface IEmbeddingService { embed(text: string): Promise<number[]>; }

**Why:** Directly exposing external schemas in application code tightly couples the codebase to third-party vendor contracts, making provider switching or SDK upgrades painful.


### ARCH-DDD-005 · `must` · T1 critical
**Ports & Adapters (Hexagonal) Architecture for Domain-Model Business Logic**

Where business logic is implemented with the Domain Model pattern (complex invariants, not simple CRUD), the business logic must not depend on any infrastructure layer directly. Infrastructure (database, message bus, external APIs) must implement "port" interfaces defined by and owned by the business logic, with concrete "adapters" plugged in from the outside.

How to: Define repository/gateway interfaces (ports) inside the domain/application layer (e.g. `IKnowledgeBaseRepository`); implement them in the infrastructure layer (e.g. `PrismaKnowledgeBaseRepository`) and inject the concrete adapter at composition root.

✗ Domain service class directly importing `PrismaClient` and constructing SQL-shaped queries inline with business rule evaluation.
✓ interface IKnowledgeBaseRepository { findById(id: string): Promise<KnowledgeBase>; } // port owned by domain; PrismaKnowledgeBaseRepository implements it as the adapter

**Why:** In a traditional layered architecture, the domain layer depends downward on infrastructure, so infrastructure changes (swapping ORMs, message brokers) ripple into business logic and business logic can't be tested without


### ARCH-LAY-001 · `must` · T1 critical
**Strict Enforcement of Layer Isolation (No Layer Skipping)**

Requests must flow strictly through defined architectural layers: Route -> Controller -> Service -> Repository/Prisma. Upper layers must not bypass intermediate layers.

How to: Express controllers must only call Service methods. Never invoke prisma queries directly in controllers.

✗ export async function getDoc(req, res) { const doc = await prisma.document.findUnique(...); res.json(doc); }
✓ export async function getDoc(req, res) { const doc = await docService.get(req.params.id); res.json(doc); }

**Why:** Bypassing layers prevents centralized security filtering, audit logging, transaction demarcation, and data normalization.


### ARCH-MOD-002 · `must` · T1 critical
**Low Coupling and Explicit Module Contracts**

Inter-module dependencies must be strictly decoupled and accessed exclusively through exported public service interfaces or event contracts, never reaching into internal sub-paths.

How to: Export a single index.ts or clear Service class per module. Never deep-import into internal helpers of another module.

✗ import { internalParser } from '@/modules/documents/internal/parsers/pdf-ast';
✓ import { DocumentService } from '@/modules/documents';

**Why:** Direct deep imports create hidden connascence and fragile coupling, causing internal refactorings of one module to cascade into compilation failures across the codebase.


### ARCH-MONO-001 · `must` · T2 needs review
**Modular Monolith Domain-Driven Partitioning**

Monolithic backends must partition code by domain/feature boundaries rather than technical layers, encapsulating data schemas, logic, and endpoints together.

How to: Group code under src/modules/auth/, src/modules/documents/, src/modules/rag/, and src/modules/chat/.

✗ src/controllers/ (all controllers), src/services/ (all services) in flat horizontal buckets.
✓ src/modules/rag/ containing vector services, chunking logic, and similarity query routes.

**Why:** Domain partitioning allows individual features to evolve independently, maintains high cohesion, and simplifies future extraction into separate services.

