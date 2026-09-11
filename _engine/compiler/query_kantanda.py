import os
import json
import sys
import argparse

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MANIFEST_PATH = os.path.join(BASE_DIR, "dist", "kantanda-manifest.json")

if not os.path.exists(MANIFEST_PATH):
    print("Manifest not found. Please run compile_kantanda.py first.")
    sys.exit(1)

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

def query(prompt):
    prompt_lower = prompt.lower()
    matched_task = None
    best_score = 0
    
    # 1. Match task based on keywords score
    words = prompt_lower.replace(".", " ").replace("-", " ").replace("/", " ").split()
    for tid, task in manifest["tasks"].items():
        score = 0
        for kw in task["keywords"]:
            if kw in prompt_lower:
                score += 2
        for w in words:
            if len(w) > 2 and w in tid:
                score += 1
        if score > best_score:
            best_score = score
            matched_task = task
            
    if not matched_task or best_score == 0:
        if any(w in prompt_lower for w in ["ui", "react", "component", "dialog", "button", "modal"]):
            matched_task = manifest["tasks"].get("frontend.ui.component")
        elif any(w in prompt_lower for w in ["api", "rest", "endpoint", "controller"]):
            matched_task = manifest["tasks"].get("backend.api.endpoint")
        elif any(w in prompt_lower for w in ["db", "database", "query", "migration", "prisma"]):
            matched_task = manifest["tasks"].get("backend.database.query")
        else:
            matched_task = manifest["tasks"].get("backend.api.endpoint") or list(manifest["tasks"].values())[0]

    print("================================================================================")
    print("🧠 KANTANDA 2.0 COGNITIVE ROUTER")
    print("================================================================================")
    print(f"🎯 Matched Task: {matched_task['id']} (Domain: {matched_task['domain'].upper()})")
    print(f"🔑 Matched Keywords: {', '.join(matched_task['keywords'])}")
    print(f"\n📂 Ingesting Rulesets ({len(matched_task['rulesets'])} files):")
    for rf in matched_task["rulesets"]:
        print(f"  - {rf}")

    print("\n⚖️ Relevant Decision Frameworks & Dialectical Conflicts:")
    if any(k in matched_task["id"] for k in ["api", "backend", "database", "security"]):
        print("  - Framework: frameworks/database-concurrency.xml (Optimistic vs Pessimistic Locking)")
        print("  - Conflict Verdict: conflicts/postel-vs-strict-boundary.xml (Strict Zod at Gateway)")
        print("  - Conflict Verdict: conflicts/dry-vs-bounded-context.xml (Decoupling over DRY across contexts)")
        print("  - Conflict Verdict: conflicts/hermetic-mock-vs-real-db.xml (Real DB Rollback for Transactions)")
    if any(k in matched_task["id"] for k in ["ui", "frontend", "form", "state", "react"]):
        print("  - Framework: frameworks/state-management.xml (Server Component vs URL vs Zustand)")
        print("  - Conflict Verdict: conflicts/immutability-vs-performance.xml (Mandatory Immutability in React UI)")
    if any(k in matched_task["id"] for k in ["test", "testing", "unit", "mock", "e2e"]):
        print("  - Framework: frameworks/testing-strategy.xml (Unit AAA vs Mock vs Testcontainers)")
        print("  - Conflict Verdict: conflicts/hermetic-mock-vs-real-db.xml (Pure Logic Mocking vs Real DB Rollback)")

    print("\n🔍 Active Atomic Rules for this Task:")
    for rf in matched_task["rulesets"]:
        for rid, rule in manifest["rules"].items():
            if rule["file"] == rf:
                book_str = rule['book_title'] or rule['book_id'] or 'Unknown Book'
                sec_str = f" - {rule['section']}" if rule.get('section') else ""
                print(f"\n  [{rule['severity'].upper()}] {rule['id']}: {rule['title']}")
                print(f"    Source: {book_str}{sec_str}")
                print(f"    Statement: {rule['statement']}")
                if rule.get("adaptation_note"):
                    print(f"    * Adaptation Note: {rule['adaptation_note']}")

    print("\n🛡️ Dual-Gate Verification Checklist:")
    print("  [ ] Gate 1 (Mechanized Tooling): ESLint / Semgrep (Max 40 lines, zero 'any', anti-BOLA, anti-SSRF)")
    print("  [ ] Gate 2 (Semantic Self-Audit): Workflows/code-review.xml & check against incidents/post-mortems.xml")
    print("================================================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Kantanda 2.0 Cognitive Engine")
    parser.add_argument("query", nargs="*", help="Natural language description of task")
    args = parser.parse_args()
    query_text = " ".join(args.query) if args.query else "Tạo REST API thanh toán và xác thực"
    query(query_text)
