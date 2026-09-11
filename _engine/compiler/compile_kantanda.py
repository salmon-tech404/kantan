import os
import json
import xml.etree.ElementTree as ET

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(DIST_DIR, exist_ok=True)

print(f"Compiling Kantanda 2.0 Living Cognitive Architecture from {BASE_DIR}...")

manifest = {
    "version": "2.0.0",
    "architecture": "Kantanda Living Cognitive Architecture",
    "summary": {},
    "rules": {},
    "tasks": {},
    "frameworks": {},
    "conflicts": {},
    "profiles": {},
    "incidents": []
}

# 1. Parse all .rules.xml
rule_count = 0
for root, _, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith(".rules.xml"):
            fpath = os.path.join(root, f)
            rel_path = os.path.relpath(fpath, BASE_DIR).replace("\\", "/")
            try:
                tree = ET.parse(fpath)
                r_root = tree.getroot()
                domain = r_root.get("domain", "")
                if not domain and "design-system" in rel_path:
                    domain = "design-system"
                category = r_root.get("category", "")
                for rule in r_root.findall(".//rule"):
                    rid = rule.get("id")
                    severity = rule.get("severity")

                    title = (rule.findtext("title", "") or rule.get("title", "")).strip()
                    statement = (rule.findtext("statement", "") or (rule.text or "")).strip()

                    source_el = rule.find(".//source")
                    book_title = source_el.get("book_title") if source_el is not None else ""
                    book_id = source_el.get("book_id") if source_el is not None else ""
                    section = source_el.get("section") or source_el.get("chapter") if source_el is not None else ""
                    evidence_el = rule.find(".//evidence_quote")
                    adaptation = rule.findtext("adaptation_note", "").strip()

                    if not book_title and "design-system" in rel_path:
                        book_title = "Design System Specifications / Laws of UX"
                        book_id = "BOOK-UI-LAWS-OF-UX"

                    manifest["rules"][rid] = {
                        "id": rid,
                        "file": rel_path,
                        "domain": domain,
                        "category": category,
                        "severity": severity,
                        "title": title,
                        "statement": statement,
                        "book_id": book_id,
                        "book_title": book_title,
                        "section": section,
                        "evidence_quote": evidence_el.text.strip() if evidence_el is not None and evidence_el.text else "",
                        "adaptation_note": adaptation
                    }
                    rule_count += 1
            except Exception as e:
                print(f"Error parsing rule file {fpath}: {e}")

# 2. Parse taxonomy.xml
taxonomy_path = os.path.join(BASE_DIR, "taxonomy.xml")
if os.path.exists(taxonomy_path):
    ttree = ET.parse(taxonomy_path)
    for task in ttree.getroot().findall(".//task"):
        tid = task.get("id")
        domain = task.get("domain", "")
        keywords = [k.text.strip().lower() for k in task.findall(".//keywords/keyword") if k.text]
        rulesets = [f.text.strip() for f in task.findall(".//rulesets/file") if f.text]
        manifest["tasks"][tid] = {
            "id": tid,
            "domain": domain,
            "keywords": keywords,
            "rulesets": rulesets
        }

# 3. Parse frameworks/
fw_dir = os.path.join(BASE_DIR, "frameworks")
if os.path.exists(fw_dir):
    for f in os.listdir(fw_dir):
        if f.endswith(".xml") and f != "index.xml":
            ftree = ET.parse(os.path.join(fw_dir, f))
            froot = ftree.getroot()
            fid = froot.get("id", f)
            manifest["frameworks"][fid] = {
                "id": fid,
                "domain": froot.get("domain", ""),
                "title": froot.findtext("title", "").strip(),
                "problem": froot.findtext("problem_statement", "").strip()
            }

# 4. Parse conflicts/
cf_dir = os.path.join(BASE_DIR, "conflicts")
if os.path.exists(cf_dir):
    for f in os.listdir(cf_dir):
        if f.endswith(".xml") and f != "index.xml":
            ctree = ET.parse(os.path.join(cf_dir, f))
            croot = ctree.getroot()
            cid = croot.get("id", f)
            manifest["conflicts"][cid] = {
                "id": cid,
                "title": croot.findtext("title", "").strip(),
                "verdict": croot.findtext(".//verdict/rule_summary", "").strip()
            }

# 5. Parse profiles/
pf_dir = os.path.join(BASE_DIR, "profiles")
if os.path.exists(pf_dir):
    for f in os.listdir(pf_dir):
        if f.endswith(".profile.xml"):
            ptree = ET.parse(os.path.join(pf_dir, f))
            proot = ptree.getroot()
            pid = proot.get("id", f)
            manifest["profiles"][pid] = {
                "id": pid,
                "name": proot.findtext("name", "").strip(),
                "description": proot.findtext("description", "").strip()
            }

# 6. Parse incidents/post-mortems.xml
incidents_path = os.path.join(BASE_DIR, "incidents", "post-mortems.xml")
if os.path.exists(incidents_path):
    try:
        itree = ET.parse(incidents_path)
        for inc in itree.getroot().findall(".//incident"):
            manifest["incidents"].append({
                "id": inc.get("id"),
                "severity": inc.get("severity", ""),
                "date": inc.get("date", ""),
                "affected_project": inc.findtext("affected_project", "").strip(),
                "symptom": inc.findtext("symptom", "").strip(),
                "root_cause": inc.findtext("root_cause", "").strip(),
                "preventable_by_rule_id": inc.findtext("preventable_by_rule_id", "").strip(),
                "knowledge_feedback": inc.findtext("knowledge_feedback", "").strip()
            })
    except Exception as e:
        print(f"Error parsing post-mortems: {e}")

# Summary
manifest["summary"] = {
    "total_rules": rule_count,
    "total_tasks": len(manifest["tasks"]),
    "total_frameworks": len(manifest["frameworks"]),
    "total_conflicts": len(manifest["conflicts"]),
    "total_profiles": len(manifest["profiles"]),
    "total_incidents": len(manifest["incidents"])
}

output_path = os.path.join(DIST_DIR, "kantanda-manifest.json")
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(manifest, out, indent=2, ensure_ascii=False)

print(f"SUCCESS: Compiled {rule_count} atomic rules, {len(manifest['tasks'])} tasks, "
      f"{len(manifest['frameworks'])} frameworks, {len(manifest['conflicts'])} conflicts, "
      f"and {len(manifest['profiles'])} profiles into {output_path}")
