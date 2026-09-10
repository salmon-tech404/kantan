# 🧠 Kantanda Engineering Brain

An **LLM-Native Cognitive Architecture and Engineering Rule System** built from the exhaustive synthesis of **18 authoritative software engineering books**.

Designed specifically for autonomous Coding Agents (Cursor, Antigravity, Claude Code) to achieve deterministic rule compliance, progressive disclosure, zero hallucination, and post-generation self-auditing.

---

## 🏛️ The 6-Tier Architecture

```
L0 ── SOURCE KNOWLEDGE (18 Books in D:\04-knowledge-base)
        │
L1 ── DISTILLED CONCEPTS (Ontology & Vocabulary)
        │
L2 ── ATOMIC RULES (Strict Schema with Verbatim Evidence Quotes)
        │
L3 ── DOMAINS & CATEGORIES (Architecture, Backend, Frontend, Security, RAG, Testing, UX/UI, DevOps)
        │
L4 ── TASK ROUTER & RULE PACKS (Inheritance-based Bundles: destructive-dialog, rag-pipeline)
        │
L5 ── PROJECT PROFILE (Veltrix-AI: Next.js 16, Express 5, Prisma 7, pgvector)
        │
L6 ── CLOSED-LOOP VALIDATION (Pre-generation Rule Loading + Post-generation Self-Audit)
```

---

## 📚 The 18 Source Books Catalog

All rules are 100% grounded in verifiable evidence quotes from the library at `D:\04-knowledge-base`:

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

## 📁 Clean Repository Structure

```text
D:\10-kantanda\
├── backend/                       # Backend Atomic Rules (.rules.xml)
│   ├── api/                       # REST endpoints, Envelopes, Zod Validation, Error codes
│   ├── architecture/              # Modular Monolith, Layering, Bounded Contexts
│   ├── database/                  # Anti-BOLA Queries, Atomic Transactions
│   ├── rag/                       # Chunking, pgvector Cosine Search, Citations
│   ├── security/                  # JWT Dual Tokens, Magic Bytes, Prompt Injection Guards
│   └── testing/                   # Unit AAA, Mocking Boundaries, PostgreSQL Rollback
├── frontend/                      # Frontend Atomic Rules (.rules.xml)
│   ├── architecture/              # Server Components First, Colocation Boundaries
│   ├── react/                     # Form Action State, API Integration
│   ├── state/                     # Server State vs Client State Separation
│   ├── typescript/                # Zero any policy, Discriminated Unions
│   ├── ux-ui/                     # 5 Mandatory States, Focus Traps, Destructive Confirmation
│   └── testing/                   # Playwright Page Object Models
├── common/                        # Universal Standards (.rules.xml)
│   ├── coding/                    # Single Responsibility, <= 40 lines, Guard clauses
│   ├── documentation/             # TSDoc on public APIs, 'Why not What' comments
│   ├── git/                       # Conventional Commits, 5-Point Code Review Gate
│   └── security/                  # Zero-trust dependencies, Secret scanners
├── design-system/                 # Design System & UI Specs
│   ├── tokens/                    # Color scales (Tailwind v4), Typography scales
│   └── components/                # Dialog touch targets, Modal focus rules
├── workflows/                     # Standard Operating Workflows for Agents
│   ├── create-api.xml             # Step-by-step secure API implementation
│   ├── create-component.xml       # Step-by-step 5-state React component workflow
│   └── code-review.xml            # 5-Gate Review Checklist
│
├── index.xml                      # Global XML Knowledge Router
├── taxonomy.xml                   # Task classification & domain mapping
├── rule-priority.xml              # Matrix resolving rule conflicts (Security > Correctness > Clean Code)
├── glossary.xml                   # Veltrix architectural domain terms
├── AGENTS.md                      # AI Agent Operating Protocol
└── _engine/                       # Internal infrastructure (sources catalog, audit manifest, compiler)
```

---

## ⚡ How LLMs Use the Brain (The 4-Step Protocol)

1. **Routing**: LLM reads `taxonomy.xml` & `index.xml` to match task intent to domains.
2. **Selective Ingestion**: LLM loads only the 3-5 relevant `.rules.xml` files (~1,000 tokens), avoiding full-context bloat.
3. **Execution**: LLM codes with strict adherence to `rule-priority.xml` (Rank 1: Security > Rank 2: Type Safety > Rank 3: Maintainability).
4. **Self-Audit**: LLM runs pre-commit verification against `workflows/code-review.xml`.

