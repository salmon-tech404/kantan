import os
import json
import yaml
import sys

BASE_DIR = r"D:\10-kantanda"
RULES_DIR = os.path.join(BASE_DIR, "rules")
PACKS_DIR = os.path.join(BASE_DIR, "brain", "rule-packs")
DIST_DIR = os.path.join(BASE_DIR, "dist")
BUNDLES_DIR = os.path.join(DIST_DIR, "bundles")

os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(BUNDLES_DIR, exist_ok=True)

print("Starting Veltrix Engineering Brain Compiler...")

# 1. Load all rules
all_rules = []
rules_by_id = {}
for root, dirs, files in os.walk(RULES_DIR):
    for f in files:
        if f.endswith(".rules.yaml"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as rf:
                data = yaml.safe_load(rf)
                if "rules" in data:
                    for r in data["rules"]:
                        all_rules.append(r)
                        rules_by_id[r["id"]] = r

print(f"Loaded {len(all_rules)} atomic rules.")

# 2. Validate rules
validation_errors = []
for r in all_rules:
    rid = r.get("id")
    if not rid:
        validation_errors.append("Rule missing 'id'")
        continue
    if not r.get("severity") in ["MUST", "MUST_NOT", "SHOULD", "SHOULD_NOT", "MAY"]:
        validation_errors.append(f"Rule {rid} has invalid severity: {r.get('severity')}")
    if not r.get("statement"):
        validation_errors.append(f"Rule {rid} missing 'statement'")
    if not r.get("sources"):
        validation_errors.append(f"Rule {rid} missing 'sources'")

if validation_errors:
    print(f"FAILED validation with {len(validation_errors)} errors:")
    for err in validation_errors[:5]:
        print("  -", err)
    sys.exit(1)
else:
    print("All rules PASSED schema validation 100%.")

# 3. Resolve Rule Packs with Inheritance
resolved_packs = {}
raw_packs = {}
for pf in os.listdir(PACKS_DIR):
    if pf.endswith(".pack.yaml"):
        with open(os.path.join(PACKS_DIR, pf), "r", encoding="utf-8") as f:
            pdata = yaml.safe_load(f)
            raw_packs[pdata["pack_id"]] = pdata

def resolve_pack_rules(pack_id, visited=None):
    if visited is None:
        visited = set()
    if pack_id in visited:
        return []
    visited.add(pack_id)
    pack = raw_packs.get(pack_id)
    if not pack:
        return []
    accumulated = list(pack.get("rules", []))
    for ext in pack.get("extends", []):
        accumulated = resolve_pack_rules(ext, visited) + accumulated
    # Deduplicate while preserving order
    seen = set()
    ordered = []
    for rid in accumulated:
        if rid not in seen:
            seen.add(rid)
            ordered.append(rid)
    return ordered

for pid in raw_packs:
    resolved_packs[pid] = {
        "pack_id": pid,
        "title": raw_packs[pid]["title"],
        "description": raw_packs[pid]["description"],
        "total_rules": len(resolve_pack_rules(pid)),
        "resolved_rule_ids": resolve_pack_rules(pid)
    }

print(f"Compiled {len(resolved_packs)} rule packs with inheritance.")

# 4. Dependency Graph
dependency_graph = {}
for r in all_rules:
    dependency_graph[r["id"]] = {
        "depends_on": r.get("related_rules", []),
        "domain": r.get("domain"),
        "severity": r.get("severity")
    }

# 5. Compact Compiled Registry
compiled_registry = {}
for r in all_rules:
    compiled_registry[r["id"]] = {
        "id": r["id"],
        "title": r["title"],
        "severity": r["severity"],
        "domain": r["domain"],
        "category": r["category"],
        "summary": r.get("statement", "")[:120] + "...",
        "tags": r.get("tags", []),
        "sources": [
            f"{s['book_title']} ({s['chapter']})" for s in r.get("sources", [])
        ]
    }

# 6. Task Lookup Index
task_lookup = {
    "keyword_index": {},
    "packs": resolved_packs
}
for r in all_rules:
    for tag in r.get("tags", []):
        t = tag.lower()
        if t not in task_lookup["keyword_index"]:
            task_lookup["keyword_index"][t] = []
        task_lookup["keyword_index"][t].append(r["id"])

# 7. Write Distribution Artifacts
with open(os.path.join(DIST_DIR, "compiled-registry.json"), "w", encoding="utf-8") as f:
    json.dump(compiled_registry, f, indent=2, ensure_ascii=False)

with open(os.path.join(DIST_DIR, "resolved-packs.json"), "w", encoding="utf-8") as f:
    json.dump(resolved_packs, f, indent=2, ensure_ascii=False)

with open(os.path.join(DIST_DIR, "dependency-graph.json"), "w", encoding="utf-8") as f:
    json.dump(dependency_graph, f, indent=2, ensure_ascii=False)

with open(os.path.join(DIST_DIR, "task-lookup-index.json"), "w", encoding="utf-8") as f:
    json.dump(task_lookup, f, indent=2, ensure_ascii=False)

print("Saved dist/ JSON distribution artifacts.")

# 8. Generate Bundles for Web/Markdown use
domains = sorted(list(set(r["domain"] for r in all_rules)))
for dom in domains:
    dom_rules = [r for r in all_rules if r["domain"] == dom]
    md_lines = [f"# VELTRIX ENGINEERING STANDARDS: {dom.upper()}", f"Total Rules: {len(dom_rules)}\n"]
    for r in dom_rules:
        md_lines.append(f"## [{r['id']}] {r['title']} ({r['severity']})")
        md_lines.append(f"**Statement**: {r['statement']}")
        md_lines.append(f"**Rationale**: {r.get('rationale', '')}")
        md_lines.append(f"**Guidance**: {r.get('implementation_guidance', '')}")
        if r.get("good_example"):
            md_lines.append(f"**Good Practice**:\n```typescript\n{r['good_example']}\n```")
        if r.get("bad_example"):
            md_lines.append(f"**Anti-pattern**:\n```typescript\n{r['bad_example']}\n```")
        src_strs = [f"- {s['book_title']} by {', '.join(s['authors'])}, {s['chapter']} (Evidence: \"{s['evidence_quote']}\")" for s in r.get("sources", [])]
        md_lines.append(f"**Evidence & Sources**:\n" + "\n".join(src_strs) + "\n")
    
    bundle_path = os.path.join(BUNDLES_DIR, f"{dom}-rules.md")
    with open(bundle_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Generated Bundle: {bundle_path}")

# Full System Bundle
full_md = ["# VELTRIX ENGINEERING BRAIN: MASTER STANDARDS BUNDLE", f"Compiled {len(all_rules)} Atomic Rules across 18 Books\n"]
for r in all_rules:
    full_md.append(f"### [{r['id']}] {r['title']} [{r['domain'].upper()}] - {r['severity']}")
    full_md.append(f"> {r['statement']}")
    full_md.append(f"- **Guidance**: {r.get('implementation_guidance', '')}")
    if r.get("bad_example"):
        full_md.append(f"- **Forbidden**: `{r.get('bad_example').splitlines()[0]}`")
    full_md.append("")

with open(os.path.join(BUNDLES_DIR, "full-system-standard.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(full_md))
print("Generated Bundle: dist/bundles/full-system-standard.md")

print("\nVeltrix Engineering Brain Compilation COMPLETE!")
