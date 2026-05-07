#!/usr/bin/env python3
"""Validate the Charlie skills layout.

Checks:
- All SKILL.md files have valid YAML frontmatter
- Required fields present (name, description, version, author, license, metadata.hermes.tags, metadata.hermes.related_skills)
- description <= 1024 chars
- No SKILL.md > 15000 chars (warns)
- Reports total auto-load size + est. tokens
"""
import os, re, sys, yaml, json

ROOT = os.path.join(os.path.dirname(__file__), "..", "profiles", "charlie-morgan", "skills")
ROOT = os.path.abspath(ROOT)

REQUIRED = ["name", "description", "version", "author", "license", "metadata"]
HARD_LIMIT = 15000
DESC_LIMIT = 1024

def main():
    errors = []
    warnings = []
    rows = []
    if not os.path.isdir(ROOT):
        print(f"ERROR: skills dir not found at {ROOT}")
        sys.exit(2)

    for u in sorted(os.listdir(ROOT)):
        udir = os.path.join(ROOT, u)
        if not os.path.isdir(udir):
            continue
        p = os.path.join(udir, "SKILL.md")
        if not os.path.isfile(p):
            errors.append(f"{u}: no SKILL.md")
            continue
        text = open(p).read()
        sz = len(text)
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{u}: no frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{u}: YAML parse error: {e}")
            continue
        for k in REQUIRED:
            if k not in fm:
                errors.append(f"{u}: missing required field '{k}'")
        if "description" in fm and len(fm["description"]) > DESC_LIMIT:
            errors.append(f"{u}: description exceeds {DESC_LIMIT} chars ({len(fm['description'])})")
        if "metadata" in fm:
            h = fm["metadata"].get("hermes", {}) if isinstance(fm["metadata"], dict) else {}
            for k in ("tags", "related_skills"):
                if k not in h:
                    errors.append(f"{u}: missing metadata.hermes.{k}")
        if sz > HARD_LIMIT:
            warnings.append(f"{u}: SKILL.md is {sz} chars (>{HARD_LIMIT})")
        rows.append((u, sz))

    total = sum(sz for _, sz in rows)
    print(f"Skills found: {len(rows)}")
    print(f"Total auto-load chars: {total}")
    print(f"Estimated tokens (~4 chars/tok): {total // 4}")
    print()
    print("Per-skill:")
    for u, sz in rows:
        print(f"  {u}: {sz} chars")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("\nOK: all skills valid.")

if __name__ == "__main__":
    main()
