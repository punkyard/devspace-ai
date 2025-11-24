#!/usr/bin/env python3
"""
Validation script for context conversation & synthesis files.
Checks:
 - filenames match YYYYMMDD-slug-(conversation|synthesis).md
 - frontmatter created matches YYYYMMDD and date in filename
 - conversation_id matches the base (YYYYMMDD-slug)
 - updated if present is list of YYYYMMDD
 - both conversation and synthesis exist for each base
"""

import sys
import os
import re
from glob import glob
from pathlib import Path
import yaml
import argparse

ROOT = Path(__file__).resolve().parents[2]
CONTEXT = ROOT / "context"

FILENAME_RE = re.compile(r"^(?P<date>\d{8})-(?P<slug>[a-z0-9-]+)-(?P<kind>conversation|synthesis)\.md$")
DATE_RE = re.compile(r"^\d{8}$")

errors = []

parser = argparse.ArgumentParser(description='Validate context conversation and synthesis files')
parser.add_argument('--ensure-todo', action='store_true', help='ensure a context YYYYMMDD-todo.md exists')
args = parser.parse_args()

files = [Path(p) for p in glob(str(CONTEXT / "*-conversation.md"))] + [Path(p) for p in glob(str(CONTEXT / "*-synthesis.md"))]

bases = {}
for f in files:
    name = f.name
    m = FILENAME_RE.match(name)
    if not m:
        errors.append(f"Invalid filename: {name} - must match YYYYMMDD-slug-(conversation|synthesis).md")
        continue

    date = m.group('date')
    slug = m.group('slug')
    kind = m.group('kind')
    base = f"{date}-{slug}"

    # parse frontmatter
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # find YAML frontmatter
    if content.startswith('---'):
        try:
            parts = content.split('---', 2)
            fm_text = parts[1]
            fm = yaml.safe_load(fm_text) or {}
        except Exception as e:
            errors.append(f"{name}: invalid frontmatter YAML: {e}")
            continue
    else:
        errors.append(f"{name}: missing YAML frontmatter (---)")
        continue

    # check created
    created = fm.get('created')
    if not created:
        errors.append(f"{name}: frontmatter 'created' missing")
    else:
        if not DATE_RE.match(str(created)):
            errors.append(f"{name}: 'created' should be YYYYMMDD, got: {created}")
        if created != date:
            errors.append(f"{name}: 'created' date {created} does not match filename date {date}")

    # check conversation_id
    conversation_id = fm.get('conversation_id')
    if not conversation_id:
        errors.append(f"{name}: frontmatter 'conversation_id' missing")
    else:
        if conversation_id != base:
            errors.append(f"{name}: 'conversation_id' ({conversation_id}) must equal filename base ({base})")

    # updated field if present must be list of YYYYMMDD
    updated = fm.get('updated')
    if updated is not None:
        if not isinstance(updated, list):
            errors.append(f"{name}: 'updated' must be a list of YYYYMMDD strings")
        else:
            for u in updated:
                if not DATE_RE.match(str(u)):
                    errors.append(f"{name}: 'updated' entry '{u}' invalid - should be YYYYMMDD")

    # remember base kinds
    bases.setdefault(base, set()).add(kind)

errors += []
for base, kinds in bases.items():
    if 'conversation' not in kinds or 'synthesis' not in kinds:
        errors.append(f"Missing pair for base {base}: found kinds {sorted(list(kinds))}")

if args.ensure_todo:
    # check for todo files
    todos = [Path(p) for p in glob(str(CONTEXT / "*-todo.md"))]
    if not todos:
        errors.append("No context/*-todo.md file found (build-in todo file missing)")
    else:
        for todo in todos:
            name = todo.name
            m = re.match(r"^(?P<date>\d{8})-.*-todo\.md$", name)
            if not m:
                errors.append(f"Invalid todo filename: {name} - must match YYYYMMDD-*-todo.md")
            else:
                date = m.group('date')
                with open(todo, 'r', encoding='utf-8') as fh:
                    content = fh.read()
                if content.startswith("---"):
                    try:
                        parts = content.split('---', 2)
                        fm = yaml.safe_load(parts[1]) or {}
                    except Exception as e:
                        errors.append(f"{name}: invalid frontmatter YAML: {e}")
                        continue
                    created = fm.get('created')
                    if not created:
                        errors.append(f"{name}: frontmatter 'created' missing")
                    elif str(created) != date:
                        errors.append(f"{name}: 'created' date {created} does not match filename date {date}")

if errors:
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print("All context conversation/synthesis files valid")
    sys.exit(0)
