---
area: architecture
path: architecture/guidance.md
rules: 6
---
### ARCH-DDD-001 · `must` · T3 guidance
**Explicit Definition of Bounded Contexts**

Each subsystem must maintain an explicit Bounded Context with its own Ubiquitous Language; domain models must not be shared indiscriminately across contexts.

How to: Define separate models for IngestionDocument (file buffer, extraction metadata) and RagDocument (vector embeddings, chunks, citations).

✗ A single giant Document class with 50 optional properties catering to every subsystem.
✓ Separate DocumentIngestionEntity and RagVectorEntity with explicit boundary mapper.

**Why:** Sharing a single entity class across ingestion, billing, vector indexing, and chat results in an bloated entity with conflicting invariants.


### ARCH-DDD-003 · `must` · T3 guidance
**Aggregate Root Invariant Encapsulation and Transactional Boundary**

Domain mutations must be executed strictly through the Aggregate Root entity; external code must never directly alter the state of child entities within an aggregate boundary.

How to: KnowledgeBase is the Aggregate Root. To add or reorder documents and chunks, invoke kb.addDocument(...) rather than executing direct Prisma mutations on Document or Chunk tables.

✗ await prisma.chunk.update({ where: { id: chunkId }, data: { status: 'processed' } }); // Bypassing KnowledgeBase invariant
✓ const kb = await kbRepo.findById(kbId); kb.markChunkProcessed(chunkId); await kbRepo.save(kb);

**Why:** Bypassing the Aggregate Root to modify child records directly corrupts domain invariants and breaks consistency guarantees within the business model.


### ARCH-DDD-004 · `must` · T3 guidance
**Domain Events and Transactional Outbox for Asynchronous Decoupling**

Cross-subsystem side effects (e.g. triggering embedding, vector indexing, email notifications) must be emitted as Domain Events and committed via the Transactional Outbox pattern within the same database transaction.

How to: Save the business entity and an OutboxEvent row inside a single prisma.$transaction. An independent background worker polls and dispatches outbox events reliably.

✗ await prisma.document.create({ data }); await rabbitmq.publish('doc_created', data); // Dual-write risk: if MQ fails, state is inconsistent
✓ await prisma.$transaction([prisma.document.create({ data }), prisma.outboxEvent.create({ data: eventPayload })]);

**Why:** Directly calling external message queues or third-party APIs inside a database transaction leads to dual-write inconsistencies if the network or transaction aborts.


### ARCH-SINK-001 · `should_not` · T3 guidance
**Avoid Architecture Sinkhole Anti-Pattern**

Do not construct redundant pass-through layers that perform no calculation, validation, transformation, or orchestration.

How to: For simple read-only data fetches, allow Controller to invoke an Open Query Gateway directly rather than building empty 5-line wrapper services.

✗ Controller -> DocumentService.get() -> DocumentManager.get() -> DocumentRepo.get() with identical arguments and no logic.
✓ A dedicated DocumentQueryService returning formatted DTOs directly.

**Why:** When 80% of service methods do nothing but call repository methods with identical parameters, layered abstraction adds pure boilerplate without value.


### ARCH-MOD-001 · `must` · T3 guidance
**High Cohesion within Domain Modules**

Modules must exhibit high functional cohesion, where all classes, services, and schemas within a module contribute directly to a single well-defined business domain.

How to: Colocate routes, controllers, services, validation schemas, and types within src/modules/<feature>/.

✗ A generic utils/ folder containing chunkDocument(), calculateTax(), and renderNavbar() in the same file.
✓ src/modules/documents/ containing documents.service.ts, documents.routes.ts, documents.validation.ts, documents.types.ts

**Why:** Low cohesion distributes related business concepts across unrelated folders, increasing cognitive load and causing scattered multi-file edits for a single requirement modification.


### ARCH-MOD-003 · `must_not` · T3 guidance
**Eliminate Connascence of Execution Order**

Public service methods must not require external callers to invoke separate methods in an undocumented chronological sequence to produce a valid domain state.

How to: Combine sequential steps into a single atomic method or use Builder/Factory patterns with validated completion.

✗ service.upload(); service.parse(); service.embed(); // Caller must remember the exact sequence
✓ await documentService.uploadAndIndex({ file, metadata });

**Why:** Connascence of Execution forces external callers to understand internal operational mechanics, leading to uninitialized state bugs and race conditions.

