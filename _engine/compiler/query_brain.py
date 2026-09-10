import os
import json
import yaml
import sys
import argparse

BASE_DIR = r"D:\10-kantanda"
DIST_DIR = os.path.join(BASE_DIR, "dist")
ROUTER_PATH = os.path.join(BASE_DIR, "brain", "task-router.yaml")

with open(os.path.join(DIST_DIR, "compiled-registry.json"), "r", encoding="utf-8") as f:
    registry = json.load(f)

with open(os.path.join(DIST_DIR, "resolved-packs.json"), "r", encoding="utf-8") as f:
    packs = json.load(f)

with open(ROUTER_PATH, "r", encoding="utf-8") as f:
    router = yaml.safe_load(f)

def query_by_prompt(prompt_text):
    prompt_lower = prompt_text.lower()
    selected_pack = None
    matched_intent = None
    
    # 1. Evaluate Router
    for route in router.get("routes", []):
        if any(kw in prompt_lower for kw in route.get("keywords", [])):
            matched_intent = route["intent"]
            selected_pack = route["default_pack"]
            # Check facets
            for facet in route.get("facets", []):
                if any(fkw in prompt_lower for fkw in facet.get("keywords", [])):
                    selected_pack = facet["activate_pack"]
            break
            
    if not selected_pack:
        # Fallback to frontend-base or backend-api-base
        if any(k in prompt_lower for k in ["ui", "component", "dialog", "react", "page", "css"]):
            selected_pack = "frontend-base"
        else:
            selected_pack = "backend-api-base"

    return get_pack_details(selected_pack, matched_intent)

def get_pack_details(pack_id, intent_name=None):
    pack = packs.get(pack_id)
    if not pack:
        print(f"Error: Pack '{pack_id}' not found.")
        sys.exit(1)
        
    rule_ids = pack["resolved_rule_ids"]
    output = []
    output.append(f"# [BRAIN ROUTER] MATCHED PACK: {pack_id.upper()}")
    if intent_name:
        output.append(f"Intent: {intent_name}")
    output.append(f"Description: {pack['description']}")
    output.append(f"Total Rules Loaded: {len(rule_ids)}\n")
    output.append("=== MANDATORY APPLIED RULES ===")
    
    for rid in rule_ids:
        r = registry.get(rid)
        if r:
            output.append(f"- [{r['id']}] ({r['severity']}) {r['title']}")
            output.append(f"  Summary: {r['summary']}")
            output.append(f"  Sources: {', '.join(r['sources'][:1])}")
    
    output.append("\n=== LLM SELF-AUDIT CHECKLIST ===")
    output.append("Before returning code, verify each rule ID:")
    for rid in rule_ids:
        output.append(f"  [ ] {rid} : PASS")
        
    return "\n".join(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Veltrix Engineering Brain")
    parser.add_argument("query", nargs="?", default="", help="Natural language task description")
    parser.add_argument("--pack", help="Direct Rule Pack ID")
    
    args = parser.parse_args()
    
    if args.pack:
        print(get_pack_details(args.pack))
    elif args.query:
        print(query_by_prompt(args.query))
    else:
        print("Usage: python query_brain.py <task_description> OR python query_brain.py --pack <pack_id>")
        print("\nAvailable Packs:")
        for pid, pdata in packs.items():
            print(f"  - {pid:22} : {pdata['title']} ({pdata['total_rules']} rules)")
