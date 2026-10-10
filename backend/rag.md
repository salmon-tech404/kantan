---
area: backend
path: backend/rag.md
optional: true
module: rag-pgvector
rules: 9
---
### RAG-CHK-001 · `must` · T2 needs review
**Deterministic Word Window Chunking with Overlap**

Document text must be chunked into deterministic word windows ({{chunk_words}} words) with a mandatory boundary overlap ({{chunk_overlap}} words).

How to: Implement sliding window chunking. Preserve sheet prefixes for Excel rows and page metadata for PDFs.

✗ Splitting text by raw character length without overlap, cutting words and sentences in half.
✓ const chunks = chunkText(extractedText, { windowSize: 500, overlap: 50 });

**Why:** Without overlap, critical contextual sentences split across chunk boundaries are lost during embedding, destroying retrieval accuracy.

**Parameter:** `({{chunk_words}} words)`, `({{chunk_overlap}} words)`


### RAG-ING-002 · `must` · T2 needs review
**Streaming / Bounded-Buffer Parsing for Large Document Ingestion**

Document ingestion — whether synchronous or inside a background worker — must never load an entire source file into a single in-memory buffer before parsing. Parsers must consume the source incrementally (page-by-page for PDF, row-by-row for CSV/XLSX) with a hard cap on bytes held in memory at any one time, independent of any file-size dispatch threshold (RAG-ASY-001) or request-rate limit (SEC-RAT-001).

How to: Use a streaming parser that yields pages/rows incrementally (e.g. a PDF library's per-page iterator) and feed each page directly into RAG-CHK-001's chunking window, releasing the raw page buffer once it has been chunked. Never call a "read entire file into a buffer/string" API on an uploaded documen

✗ const fullText = await pdfParse(fs.readFileSync(uploadedPath)); const chunks = chunkText(fullText, ...); // loads the whole file into one buffer before any chunking happens
✓ for await (const page of streamPdfPages(uploadedPath)) { const pageChunks = chunkText(page.text, { windowSize: 500, overlap: 50 }); await persistChunks(pageChunks); }

**Why:** Loading an entire large document into memory before processing is a near-certain way to trigger an out-of-memory crash in the ingestion worker. This exact failure mode caused a real production incident (INC-2026-001): 50


### RAG-CIT-001 · `must` · T1 critical
**Verifiable Source Grounding and Citation Metadata**

Every retrieved chunk injected into the LLM context must carry immutable provenance metadata (documentId, documentTitle, pageNumber, sheetName).

How to: Format retrieved chunks in the system prompt with citation tags: [Source: {title}, Page: {page}, Sheet: {sheet}] {content}.

✗ Concatenating raw text chunks into the prompt with no attribution or origin tracking.
✓ Injecting '[Source: Contract.pdf, Page 4] The warranty period is 24 months' into the context prompt.

**Why:** Enterprise RAG platforms must provide auditability and verifiable citations so users can cross-check AI claims directly against source documents.


### RAG-PRM-001 · `must` · T3 guidance
**Strict Contextual Framing and Anti-Hallucination Prompting**

System instructions must explicitly instruct the LLM to answer strictly using the provided context, and to state clearly that information is missing if the context is insufficient.

How to: Include: 'You must answer exclusively using the provided context. If the answer cannot be found, reply: I do not have enough information.'

✗ System: 'You are a helpful assistant, answer any questions.'
✓ System: 'Rely solely on the facts provided below. Do not assume or extrapolate beyond this text.'

**Why:** Without strict negative constraints, LLMs default to parametric web knowledge, hallucinating plausible but incorrect organizational facts.


### RAG-ASY-001 · `must` · T2 needs review
**Asynchronous Background Processing for Multi-Page Document Ingestion**

Documents exceeding {{async_size}} or {{async_pages}} must be ingested asynchronously via background worker jobs, returning an immediate 202 Accepted status with a job status tracking endpoint.

How to: Accept upload, save file to disk/S3, enqueue BullMQ / background job, return { documentId, status: 'processing' }. Update status via WebSocket or polling.

✗ Holding the HTTP POST request open for 60 seconds while Mammoth/pdf-parse and Gemini generate 200 embeddings synchronously.
✓ POST /api/v1/documents returns 202 with { jobId: '123', statusUrl: '/api/v1/jobs/123' }; client polls or listens to WS.

**Why:** Synchronous parsing and embedding of a 100-page PDF takes 30-90 seconds, causing HTTP reverse-proxy timeouts (504 Gateway Timeout) and blocking Node.js event loop threads.

**Parameter:** `exceeding {{async_size}} or {{async_pages}}`


### RAG-EVL-001 · `should` · T2 needs review
**Automated Groundedness and Faithfulness Evaluation**

RAG generation quality must be continuously audited against a golden evaluation dataset measuring Faithfulness (answer grounded in context) and Answer Relevance.

How to: Run an automated evaluation suite comparing model answers against context chunks to compute a Faithfulness Score >= 0.85.

✗ Relying purely on manual inspection of 2 sample queries when upgrading embedding models.
✓ Automated CI step checking 50 benchmark queries with RAGAS or LLM-as-a-judge for faithfulness.

**Why:** Prompt tweaks or model upgrades can silently degrade answer faithfulness or introduce subtle hallucinations without unit test failure.


### RAG-VEC-001 · `must` · T2 needs review
**Normalized High-Dimensional Cosine Similarity Search**

pgvector similarity search must compute Cosine Distance (<=> operator) against normalized {{embedding_dims}}-dimensional embedding vectors.

How to: Use SELECT ... ORDER BY embedding <=> query_vector LIMIT topK with an IVFFlat or HNSW index on the embedding column.

✗ Using Euclidean distance (<->) on unnormalized embedding vectors of variable text lengths.
✓ SELECT id, content, 1 - (embedding <=> $1) AS score FROM document_chunks WHERE user_id = $2 ORDER BY embedding <=> $1 LIMIT 8;

**Why:** Cosine similarity measures angular semantic direction independently of document chunk length, ensuring short definitions match long explanations accurately.

**Parameter:** `{{embedding_dims}}-dimensional`


### RAG-VEC-002 · `should` · T2 needs review
**Tuned HNSW Index Parameters for pgvector**

The pgvector HNSW index on the embedding column must be created with explicit `m` and `ef_construction` parameters chosen for the collection size and recall target, not left at implicit defaults, and `ef_search` should be tuned per-query when the default recall/speed balance is insufficient.

How to: Start from `m = 16, ef_construction = 64` as a reasonable default for a small-to-medium collection (as used for an ArXiv-paper-scale corpus, giving recall >0.95 with reasonable build time), and re-tune upward for larger collections or higher recall requirements.

✗ CREATE INDEX ON document_chunks USING hnsw (embedding vector_cosine_ops); -- no m/ef_construction chosen, implicit defaults for every collection size
✓ CREATE INDEX idx_chunks_embedding ON document_chunks USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);

**Why:** HNSW's build-time and query-time behavior is directly controlled by these parameters: `m` controls the number of bidirectional links per node (affecting both index size and search quality/recall), and `ef_construction` c


### RAG-VEC-003 · `should` · T2 needs review
**Embedding Model Version Pinning and Re-Index-on-Change**

The embedding model identifier and version used to generate stored vectors must be pinned and recorded (e.g. alongside the collection/index, or per-row metadata). Changing the embedding model or its version must trigger a full re-embedding and re-index of existing content — old and new embeddings must never be compared against each other in the same similarity search.

How to: Pin the exact embedding model name/version (and ideally the inference library version) used at embedding time, store it alongside the index/collection, and treat an embedding-model change as a migration requiring a full re-embed rather than an in-place row update.

✗ Upgrading the embedding model in code without re-embedding existing rows, leaving old-model and new-model vectors mixed in the same similarity search.
✓ class EmbeddingGenerator { constructor(modelName = 'text-embedding-3-large') { this.modelName = modelName; } } // pinned and recorded; a model change is a tracked migration, not a silent swap

**Why:** Embeddings from different model versions are not guaranteed to live in a comparable vector space; silently mixing them (e.g. after an unplanned model upgrade) produces similarity scores that look valid but are semantical

