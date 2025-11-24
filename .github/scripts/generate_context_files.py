#!/usr/bin/env python3
"""
Generate context/session files from README checklist.

Creates:
- context/YYYYMMDD-todo.md (built-in todo list)
- context/YYYYMMDD-initial-setup-conversation.md
- context/YYYYMMDD-initial-setup-synthesis.md

The script attempts to call a time MCP via npx first (if present) to obtain a canonical date (YYYYMMDD). If not available, it falls back to `date -u +%Y%m%d`.
"""

from pathlib import Path
import subprocess
import sys
import re
import yaml
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
CONTEXT = ROOT / "context"
README = ROOT / "README.md"

def get_date():
    # try npx MCP time generator
    try:
        out = subprocess.check_output(["npx", "mcp_time_get_current_time", "--timezone", "UTC", "--format", "YYYYMMDD"], stderr=subprocess.DEVNULL)
        date = out.decode().strip()
        if re.match(r"^\d{8}$", date):
            return date
    except Exception:
        pass
    # fallback
    return datetime.utcnow().strftime("%Y%m%d")

def parse_readme():
    if not README.exists():
        return []
    checklist = []
    pattern = re.compile(r"^\s*[-*]\s*\[.?\]\s*(.*)")
    with README.open(encoding='utf-8') as fh:
        for line in fh:
            m = pattern.match(line)
            if m:
                text = m.group(1).strip()
                checklist.append(text)
    return checklist

def write_todo(date, checklist):
    slug = "todo"
    base = f"{date}-{slug}"
    out = CONTEXT / f"{base}.md"
    if out.exists():
        # don't overwrite
        return out
    front = {
        'created': date,
        'session_id': f"{date}-initial-setup",
        'summary': 'initial setup built-in todo',
        'items': checklist,
    }
    CONTENT = f"---\n" + yaml.safe_dump(front, sort_keys=False) + "---\n\n"
    # include checklist in body as markdown
    for item in checklist:
        CONTENT += f"- [ ] {item}\n"
    CONTEXT.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(CONTENT)
    return out

def create_skeletons(date):
    slug = 'initial-setup'
    base = f"{date}-{slug}"
    convo = CONTEXT / f"{base}-conversation.md"
    synth = CONTEXT / f"{base}-synthesis.md"
    created = date
    convo_fm = {
        'created': created,
        'conversation_id': base,
        'summary': 'Conversation transcript for initial setup',
        'commit': '<pending>',
        'safe-to-push': False,
    }
    synth_fm = {
        'created': created,
        'conversation_id': base,
        'summary': 'Synthesis of initial setup conversation',
        'commit': '<pending>',
        'safe-to-push': False,
    }
    if not convo.exists():
        with open(convo, 'w', encoding='utf-8') as fh:
            fh.write('---\n')
            fh.write(yaml.safe_dump(convo_fm, sort_keys=False))
            fh.write('---\n\n# Conversation transcript\n')
    if not synth.exists():
        with open(synth, 'w', encoding='utf-8') as fh:
            fh.write('---\n')
            fh.write(yaml.safe_dump(synth_fm, sort_keys=False))
            fh.write('---\n\n# Synthesis\n')
    return convo, synth

def stage_files(files):
    try:
        subprocess.check_call(["git", "add"] + [str(f) for f in files])
    except Exception:
        pass

def main():
    date = get_date()
    checklist = parse_readme()
    todo = write_todo(date, checklist)
    convo, synth = create_skeletons(date)
    stage_files([todo, convo, synth])
    print("Created:", todo, convo, synth)

if __name__ == '__main__':
    main()
