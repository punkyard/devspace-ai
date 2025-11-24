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

ROOT = Path(__file__).resolve().parents[2]
CONTEXT = ROOT / "context"

FILENAME_RE = re.compile(r"^(?P<date>\d{8})-(?P<slug>[a-z0-9-]+)-(?P<kind>conversation|synthesis)\.md$")
DATE_RE = re.compile(r"^\d{8}$")

errors = []

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

# ensure pairs
for base, kinds in bases.items():
    if 'conversation' not in kinds or 'synthesis' not in kinds:
        errors.append(f"Missing pair for base {base}: found kinds {sorted(list(kinds))}")

if errors:
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print("All context conversation/synthesis files valid")
    sys.exit(0)
