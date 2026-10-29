---
area: backend
path: rules/backend/api.md
rules: 7
---
### BE-ERR-001 · `must` · T1 critical
**Centralized AppError Exception Hierarchy**

Application errors must instantiate or subclass AppError, encapsulating HTTP statusCode, a machine-readable errorCode, and a safe client message.

How to: Throw new AppError(404, 'DOCUMENT_NOT_FOUND', 'Document does not exist'). Let Global Error Middleware catch and format it.

✗ throw new Error('something went wrong'); // Missing HTTP status and machine error code
✓ throw new AppError(404, 'NOT_FOUND', 'Knowledge Base not found');

**Why:** Throwing raw Error instances or string literals causes unhandled promise rejections, inconsistent error responses, and potential server crashes.


### BE-ERR-002 · `must_not` · T1 critical
**Never Expose Internal Stack Traces in Production**

Production error responses must never expose raw stack traces, SQL queries, database column names, or internal file system paths.

How to: In production (NODE_ENV === 'production'), log the full stack trace to Winston and return a generic 500 error payload.

✗ { error: err.stack, sql: 'SELECT * FROM users WHERE...' }
✓ { success: false, error: { code: 'INTERNAL_SERVER_ERROR', message: 'An unexpected error occurred.' } }

**Why:** Stack traces expose internal architecture, database schema, and third-party library versions to potential attackers, facilitating exploit discovery.


### BE-API-001 · `must` · T1 critical
**RESTful Plural Nouns and Kebab-Case Endpoints**

REST API URI paths must use plural nouns in kebab-case for resource collections and avoid verbs in URI paths.

How to: Use /api/v1/knowledge-bases/:id/documents instead of /api/v1/getKnowledgeBaseDocuments.

✗ POST /api/v1/createDocument, GET /api/v1/fetchChunks
✓ GET /api/v1/documents, POST /api/v1/documents/:id/chunks

**Why:** Verbs in URLs duplicate HTTP method semantics (GET, POST, DELETE) and violate REST standard uniform resource identification.


### BE-API-002 · `must` · T2 needs review
**Uniform API Response Envelope**

All API endpoints must return a standardized JSON envelope with consistent success and error schemas.

How to: Format success responses as { success: true, data: T } and error responses as { success: false, error: { code, message, details? } }.

✗ Returning a bare array [] on some routes and { result: ... } on other routes.
✓ { success: true, data: { id: "123", name: "Policy.pdf" } }

**Why:** Inconsistent response formats force frontend clients to implement disparate parsing logic, leading to runtime unhandled exceptions.


### BE-VAL-001 · `must` · T1 critical
**Boundary Request Validation via Zod Schemas**

All incoming HTTP requests (body, query, params) must be validated by Zod schemas in middleware before touching controller logic.

How to: Attach a validate(schema) middleware to every Express route. Reject invalid requests with HTTP 422.

✗ Accessing req.body.documentTitle inside the controller without schema validation.
✓ router.post('/', validate(createDocumentSchema), documentController.create);

**Why:** Unvalidated input is the root cause of injection attacks, data corruption, and unhandled runtime exceptions in downstream services.


### BE-VAL-002 · `must` · T1 critical
**Strict Rejection of Unknown Request Fields**

Validation schemas must strip or strictly reject unrecognized fields to prevent mass assignment vulnerabilities.

How to: Use zodSchema.strict() or ensure Prisma update payloads only use parsed, typed properties.

✗ await prisma.user.update({ where: { id }, data: req.body }); // Mass assignment vulnerability
✓ const schema = z.object({ title: z.string() }).strict();

**Why:** Attackers can submit unexpected fields (e.g., isAdmin: true) that, if passed directly to database models, compromise security.


### BE-IDEM-001 · `must` · T2 needs review
**Active Idempotency Deduplication Execution**

Endpoints receiving mutation requests with an Idempotency-Key must actively query for existing records using fast-path caching or double-checked locking inside database transactions, returning the cached result (HTTP 200) instead of re-executing mutations. Validating and storing the key without duplicate querying is strictly forbidden as decorative security.

How to: Check for an existing completed transaction by idempotency key before entering the critical mutation block. If found, return the cached transfer result with isIdempotentReplay: true. Within transactions, use unique constraints on idempotency_key to guarantee database-level atomicity.

✗ Validating idempotencyKey with Zod and passing it to repository.createTransferRecord() without any findByIdempotencyKey() check.
✓ const existing = await repo.findByIdempotencyKey(key); if (existing) return formatExistingResult(existing);

**Why:** Merely validating the UUID format and storing the key in the database provides zero double-spend protection. Clients retrying requests after network timeouts will trigger duplicate financial debits if the service does no

