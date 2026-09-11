# 🧠 KANTANDA 2.0 — AGENT OPERATING PROTOCOL
**The Living Cognitive Architecture for Autonomous Coding Agents**

`D:\10-kantanda\` là chuẩn mực kỹ thuật cao nhất và kiến trúc nhận thức cho toàn bộ chu trình phát triển phần mềm.
Mọi AI Coding Agent (Antigravity, Cursor, Claude Code) **BẮT BUỘC** tuân thủ chu trình 5 bước sau đây:

```
[User Task]
    │
    ▼
┌────────────────────────────────────────────────────────┐
│ Bước 1: Profile & Context Detection                    │
│ Tra cứu profiles/ (Veltrix AI vs MarketStrategies vs UI)│
└───────────────────┬────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────┐
│ Bước 2: Task Routing & Decision Framework              │
│ Tra cứu taxonomy.xml & frameworks/ (Đánh giá trade-off)│
└───────────────────┬────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────┐
│ Bước 3: Load Atomic Rules & Resolved Conflicts        │
│ Nạp 2-4 file .rules.xml + tra cứu conflicts/ tương ứng │
└───────────────────┬────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────┐
│ Bước 4: Code Generation theo rule-priority.xml         │
│ Rank 1: Security > Rank 2: Correctness > Rank 3: Clean │
└───────────────────┬────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────┐
│ Bước 5: Dual-Gate Verification                         │
│ Gate 1: Mechanized Linting (tooling/ eslint + semgrep) │
│ Gate 2: Semantic Self-Audit (workflows/ & incidents/)  │
└────────────────────────────────────────────────────────┘
```

---

## 1. Bước 1: Profile & Context Detection
Trước khi viết mã, Agent xác định ngữ cảnh hệ thống hiện tại từ `profiles/index.xml`:
- **Veltrix AI (`profiles/veltrix-ai.profile.xml`):** Next.js 16, Express 5, Prisma 7, pgvector, SSE streaming.
- **Market Strategies (`profiles/market-strategies.profile.xml`):** In-memory ring buffer, sub-millisecond execution, in-place mutation cho Hot Paths.
- **UI Kit Standard (`profiles/ui-kit-standard.profile.xml`):** Tailwind CSS v4, Radix Primitives, WCAG 2.2 AAA.

---

## 2. Bước 2: Routing & Áp Dụng Decision Framework
Agent tra cứu `taxonomy.xml` để xác định task:
- Không áp đặt quy tắc cứng nhắc khi gặp bài toán kiến trúc phức tạp.
- Khi cần chọn giải pháp kiến trúc, tra cứu `frameworks/`:
  - `frameworks/ddd-boundaries.xml`: Chọn CRUD vs Bounded Context vs Event-Driven.
  - `frameworks/state-management.xml`: Chọn Server Component vs URL Params vs React Context vs Zustand.
  - `frameworks/database-concurrency.xml`: Chọn Optimistic vs Pessimistic Locking vs Atomic Increment.
  - `frameworks/testing-strategy.xml`: Chọn Unit AAA vs Mock vs Testcontainers Integration.

---

## 3. Bước 3: Nạp Atomic Rules & Xử Lý Xung Đột (Resolved Conflicts)
Agent nạp chính xác các file rule được chỉ định trong thẻ `<rulesets>` của `taxonomy.xml`. **Tuyệt đối không quét đệ quy toàn bộ thư mục!**

Khi các nguyên lý kỹ thuật mâu thuẫn nhau, Agent tra cứu `conflicts/` để áp dụng phán quyết chuẩn:
- `conflicts/postel-vs-strict-boundary.xml`:
  - *Tại API Gateway & DB:* Nghiêm ngặt tuyệt đối (`zod.strict()`).
  - *Tại UI Frontend:* Khoan dung (`safeParse`, fallback graceful).
- `conflicts/dry-vs-bounded-context.xml`:
  - Trong cùng 1 module: Tuân thủ DRY tuyệt đối.
  - Giữa 2 Bounded Contexts: Ưu tiên Decoupling (được phép duplicate DTO).
- `conflicts/immutability-vs-performance.xml`:
  - React UI & Business Domain: Bắt buộc Immutability (`Object.freeze`, clone).
  - Trading Hot Path & Tick Buffer: Cho phép In-place Mutable Ring Buffer.
- `conflicts/hermetic-mock-vs-real-db.xml`:
  - Pure Domain & Mathematical Logic: Cô lập 100% bằng Mock/Stubs.
  - Database Transactions & Complex SQL: Bắt buộc chạy trên PostgreSQL thật (Transaction Rollback).

---

## 4. Bước 4: Code Generation theo Ma Trận Ưu Tiên (`rule-priority.xml`)
Khi sinh mã, luôn tuân theo 4 bậc ưu tiên:
1. **Rank 1 - Security & Multi-tenant Privacy:** Anti-BOLA (bắt buộc `tenantId`), Prompt Injection defense, Zod validation, Zero PII logging.
2. **Rank 2 - Correctness & Type Safety:** Zero `any`, Discriminated Unions, Prisma Transactions.
3. **Rank 3 - Maintainability & Clean Code:** Hàm <= 40 dòng, SRP, Low Coupling, High Cohesion.
4. **Rank 4 - Performance:** Tối ưu hóa có đo lường profile, không tối ưu sớm gây rối mã.

---

## 5. Bước 5: Dual-Gate Verification (Kiểm Soát Kép)
Trước khi bàn giao kết quả cho lập trình viên, Agent thực hiện đối soát 2 cổng:

### Gate 1: Mechanized Tooling (Máy móc hóa)
- Rà soát các quy tắc tĩnh thông qua AST / Linting rules tại `tooling/`:
  - ESLint: Không dùng `any`, hàm <= 40 dòng, cấm `fetch` trực tiếp trong JSX body.
  - Semgrep: Chặn SSRF (`fetch` không qua allowlist), chặn BOLA (`findUnique` thiếu `tenantId`), chặn leak token.

### Gate 2: Semantic Self-Audit & Incident Feedback
- Đối soát theo checklist từ `workflows/code-review.xml`.
- Tra cứu `incidents/post-mortems.xml` để đảm bảo không tái phạm các lỗi sự cố đã ghi nhận trong quá khứ (ví dụ: SSRF qua Webhook URL, Race condition trong Wallet balance).
