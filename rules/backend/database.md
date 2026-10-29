---
area: backend
path: rules/backend/database.md
rules: 3
---
### BE-DB-001 · `must` · T1 critical
**Mandatory Tenant and User Scoping on Database Queries**

Every database query retrieving or mutating user-owned resources must include an explicit WHERE {{ownership_key}} filter.

How to: Always inject req.user.id into Service methods and enforce it in Prisma find, update, and vector cosine queries.

✗ await prisma.knowledgeBase.findUnique({ where: { id } }); // Missing user ownership verification
✓ await prisma.knowledgeBase.findFirst({ where: { id, userId: currentUser.id } });

**Why:** Failing to scope queries to the authenticated user leads directly to Broken Object Level Authorization (BOLA), allowing unauthorized cross-user data access.

**Parameter:** `{{ownership_key}}`


### SEC-BOLA-002 · `must` · T2 needs review
**Defense-in-Depth Anti-BOLA: Opaque IDs, 403/404 Strategy, and Automated Testing**

BE-DB-001's userId/orgId WHERE-scoping is the mandatory primary control against BOLA, but it must not be the only one. (1) Internal sequential integer primary keys must never be exposed directly in API paths/responses; expose a surrogate public ID (UUID/GUID, or an encoded value such as Sqids) instead, mapped internally to the real key. (2) When an owned resource is not found for the requesting user, return 404; only return 403 when the product intentionally needs to acknowledge the resource's existence (e.g. "this ticket exists in your org but you lack access") — and once that choice is made, response latency for the "exists but forbidden" and "does not exist" cases must be kept consistent to avoid a timing side-channel that lets an attacker enumerate resource IDs. (3) Every endpoint enforcing per-user/per-tenant access control must have an automated test asserting that a valid, authenticated user cannot retrieve another user's resource by ID.

How to: Generate public-facing resource IDs as UUIDv4 (or Sqids-encoded) even when the database primary key stays an incremental integer internally. Standardize a single "ownership check" helper that returns 404 by default when `WHERE id = :id AND userId = :currentUserId` yields no row, and pad/normalize ha

✗ // path: /orders/{id} where id is the raw auto-increment DB primary key exposed directly to clients — trivially enumerable
✓ test('user B cannot fetch user A order by id', async () => { const res = await request(app).get(`/orders/${userAOrder.publicId}`).set('Authorization', `Bearer ${userBToken}`); expect(res.status).toBe(

**Why:** Surrogate/opaque IDs are depth, not a substitute for the authorization check itself — the book explicitly warns nonpredictable IDs do not make an endpoint immune to BOLA. Conversely, a consistent 403/404 policy without c


### BE-DB-002 · `must` · T2 needs review
**Atomic Transactions for Multi-Table Writes**

All database write operations affecting multiple tables or cascading dependencies must be encapsulated within an atomic transaction.

How to: Wrap multi-table mutations inside prisma.$transaction(async (tx) => { ... }).

✗ await prisma.document.create(...); await externalService(); await prisma.chunk.createMany(...); // Inconsistent if chunk creation fails
✓ await prisma.$transaction(async (tx) => { await tx.document.create(...); await tx.chunk.createMany(...); });

**Why:** If a partial write fails midway (e.g. document created but chunking throws), the database is left in a corrupted, inconsistent state.

