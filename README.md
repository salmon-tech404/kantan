# 🧠 Kantanda 2.0 — The Living Cognitive Architecture

An **LLM-Native Cognitive Architecture and Engineering Rule System** built from the exhaustive synthesis of **18 authoritative software engineering books**, evolved beyond static dogmatic rules into a **living system of trade-off frameworks, dialectical conflict resolutions, and automated tooling**.

Designed specifically for autonomous Coding Agents (Antigravity, Cursor, Claude Code) to achieve deterministic rule compliance, progressive disclosure, zero hallucination, and dual-gate self-auditing.

---

## 🏛️ The 6-Tier Architecture

```
L0 ── SOURCE KNOWLEDGE (18 Authoritative Books in D:\04-knowledge-base)
        │
L1 ── DISTILLED ONTOLOGY (glossary.xml & taxonomy.xml)
        │
L2 ── ATOMIC RULES (93 XML Rules across Backend, Frontend, Common, Design System)
        │
L3 ── DECISION FRAMEWORKS (Trade-off Matrices for State, Concurrency, Architecture)
        │
L4 ── RESOLVED CONFLICTS LOG (Dialectical Trade-off Verdicts for Clashing Principles)
        │
L5 ── PROJECT PROFILES (Veltrix-AI, Market-Strategies, UI-Kit-Standard)
        │
L6 ── CLOSED-LOOP AUDIT (ESLint/Semgrep Tooling + Post-Mortem Incidents Feedback)
```

---

## 📚 The 18 Source Books Catalog

All rules and frameworks are 100% grounded in verifiable evidence quotes from the library at `D:\04-knowledge-base`:

| Book ID | Title | Authors | Domain |
| :--- | :--- | :--- | :--- |
| `BOOK-ARCH-FUNDAMENTALS` | Fundamentals of Software Architecture, 2nd Edition | Mark Richards, Neal Ford | Architecture |
| `BOOK-ARCH-DDD` | Learning Domain-Driven Design | Vlad Khononov | Architecture |
| `BOOK-API-WEB` | Design and Build Great Web APIs | Mike Amundsen | Backend & API |
| `BOOK-API-SECURE` | Secure APIs | John Kinsella | Security & API |
| `BOOK-RAG-HANDSON` | Hands-On RAG for Production | Various | RAG & AI |
| `BOOK-RAG-VECTORDB` | Vector Databases | Various | RAG & Database |
| `BOOK-SEC-ALICE-BOB` | Alice and Bob Learn Application Security | Tanya Janca | Security |
| `BOOK-SEC-AI` | Practical AI Security | Various | AI Security |
| `BOOK-TEST-UNIT` | Unit Testing Principles, Practices, and Patterns | Vladimir Khorikov | Testing |
| `BOOK-TEST-PLAYWRIGHT` | Hands-On Automated Testing with Playwright | Various | Testing |
| `BOOK-CLEAN-CODE` | Clean Code: A Handbook of Agile Software Craftsmanship | Robert C. Martin | Common Code |
| `BOOK-SWE-GOOGLE` | Software Engineering at Google | Titus Winters et al. | Engineering & Review |
| `BOOK-FE-NEXTJS` | Real-World Next.js - Second Edition | Michele Riva | Frontend |
| `BOOK-FE-EFFECTIVE-TS` | Effective TypeScript, 2nd Edition | Dan Vanderkam | TypeScript |
| `BOOK-FE-REACT-TS` | Learn React with TypeScript - Third Edition | Carl Rippon | React |
| `BOOK-UI-DESIGNING-INTERFACES`| Designing Interfaces, 3rd Edition | Jenifer Tidwell et al. | UX/UI |
| `BOOK-UI-LAWS-OF-UX` | Laws of UX, 2nd Edition | Jon Yablonski | UX Psychology |
| `BOOK-DEVOPS-CD` | Continuous Delivery | Jez Humble, David Farley | DevOps & CI/CD |

---

## 📁 Repository Structure

```text
D:\10-kantanda\
├── backend/                       # Backend Atomic Rules (.rules.xml)
│   ├── api/                       # REST endpoints, Envelopes, Zod Validation, Error codes
│   ├── architecture/              # Modular Monolith, Layering, Bounded Contexts
│   ├── database/                  # Anti-BOLA Queries, Atomic Transactions, Migrations
│   ├── rag/                       # Chunking, pgvector Cosine Search, Citations
│   ├── security/                  # JWT Dual Tokens, SSRF Whitelist, Rate Limiting
│   └── testing/                   # Unit AAA, Mocking Boundaries, PostgreSQL Rollback
├── frontend/                      # Frontend Atomic Rules (.rules.xml)
│   ├── architecture/              # Server Components First, Colocation Boundaries
│   ├── react/                     # Form Action State, API Integration, 5 Mandatory States
│   ├── state/                     # Server State vs Client State Separation
│   ├── typescript/                # Zero any policy, Discriminated Unions
│   ├── ux-ui/                     # Focus Traps, Destructive Confirmation, Touch Targets
│   └── testing/                   # Playwright Page Object Models
├── common/                        # Universal Standards (.rules.xml)
│   ├── coding/                    # Single Responsibility, <= 40 lines, Law of Demeter
│   ├── documentation/             # TSDoc on public APIs, 'Why not What' comments
│   ├── git/                       # Conventional Commits, 5-Point Code Review Gate
│   └── security/                  # Zero-trust dependencies, Secret scanners
├── design-system/                 # Design System & UI Tokens (.rules.xml)
│   ├── tokens/                    # Color scales (Tailwind v4), Typography, Spacing
│   └── components/                # Button, Input, Table, Toast, Dialog specs
├── frameworks/                    # Cognitive Decision Frameworks (Trade-off Matrices)
│   ├── ddd-boundaries.framework.xml        # CRUD vs Bounded Context vs Event-Driven
│   ├── state-management.framework.xml      # Server Component vs URL vs Context vs Zustand
│   ├── database-concurrency.framework.xml  # Optimistic vs Pessimistic vs Atomic Increment
│   ├── testing-strategy.framework.xml      # Unit AAA vs Mock vs Testcontainers
│   └── idempotency-strategies.framework.xml # Unique DB constraints vs Redis TTL vs Outbox
├── conflicts/                     # Resolved Dialectical Conflicts Log
│   ├── postel-vs-strict-boundary.xml       # Strict API Boundary vs Robust UI Ingestion
│   ├── dry-vs-bounded-context.xml         # Internal DRY vs Cross-Context Decoupling
│   ├── immutability-vs-performance.xml     # React Immutability vs HFT Mutable Ring Buffer
│   ├── hermetic-mock-vs-real-db.xml        # Pure Logic Mocking vs Real DB Rollback
│   └── inmemory-vs-distributed-lock.xml    # In-memory promise mutex vs Redis Redlock
├── profiles/                      # Context-Aware Project Profiles
│   ├── veltrix-ai.profile.xml          # Next.js 16 + Express 5 + Prisma 7 + pgvector
│   ├── market-strategies.profile.xml   # Low-latency trading, in-place mutable ring buffers
│   └── ui-kit-standard.profile.xml     # Tailwind CSS v4 + Radix Primitives + WCAG 2.2
├── tooling/                       # Mechanized Linting & AST Static Enforcement
│   ├── eslint/.eslintrc.js             # AST limits: <= 40 lines, no 'any', no fetch in JSX
│   └── semgrep/kantanda-security.yml   # AST security: anti-SSRF, anti-BOLA tenant checks
├── incidents/                     # Closed-Loop Feedback & Post-Mortem Feedback
│   ├── template.xml                    # Incident Post-Mortem standard schema
│   └── post-mortems.xml                # Historical production incidents & rule evolutions
├── workflows/                     # Standard Operating Workflows
│   ├── create-api.xml                  # Step-by-step secure API implementation
│   ├── create-component.xml            # Step-by-step 5-state React component workflow
│   ├── database-migration.xml          # Zero-downtime database migration workflow
│   ├── create-adr.xml                  # Step-by-step Architectural Decision Record workflow
│   ├── fix-security-vulnerability.xml  # Security vulnerability triage and fix workflow
│   └── code-review.xml                 # 6-Gate Review Checklist
│
├── index.xml                      # Global Cognitive Architecture Router
├── taxonomy.xml                   # 28 Categorized Tasks with direct ruleset mappings
├── rule-priority.xml              # Hierarchical Priority Matrix (Security > Correctness > Clean Code)
├── glossary.xml                   # 22 Canonical Architectural Terms
├── AGENTS.md                      # AI Agent 5-Step Operating Protocol
└── _engine/                       # Core engine manifest & validation tooling
```

---

## ⚡ The 5-Step Agent Operating Protocol

1. **Profile Detection**: Agent identifies project stack constraints (`profiles/`).
2. **Framework Evaluation**: When facing architectural choices, agent analyzes trade-off matrices (`frameworks/`).
3. **Selective Rule Ingestion**: Agent loads only 2-4 exact `.rules.xml` files mapped in `taxonomy.xml` + applies `conflicts/` verdicts.
4. **Implementation**: Agent writes code adhering to `rule-priority.xml` (Rank 1: Security > Rank 2: Type Safety > Rank 3: Maintainability).
5. **Dual-Gate Verification**:
   - **Gate 1 (Mechanized):** Static AST verification via `tooling/` (ESLint/Semgrep).
   - **Gate 2 (Semantic):** Agent self-audit via `workflows/code-review.xml` + check against `incidents/post-mortems.xml`.
