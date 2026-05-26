---
name: filetree-simple
description: Maintain a repository FILETREE.md index with one-line file purpose summaries and content hashes. Use this same skill from Codex or Claude Code when asked to create, update, or lint FILETREE.md.
license: MIT
---

# Filetree

Maintain `FILETREE.md`: one entry per useful text/code file, grouped by
directory, with an 8-character content hash for drift detection.

This is a plain shared skill, not a Claude Code plugin. Codex and Claude Code
should both read this `SKILL.md` directly and run the same helper script:
`scripts/filetree.py`.

Run commands from the target repository root.

## Summary Rules

- One line, max 25 words.
- Describe what the file is for, not its internal implementation details.
- Match the language of existing entries when updating an existing manifest.
- For changed files, output `UNCHANGED` when the old summary still describes the
  file purpose. Prefer `git diff HEAD -- <path>` before reading the full file.
- Write a new summary only when the file purpose meaningfully changed.

## Create Or Update

1. Run:
   ```bash
   python filetree-skill-simple/scripts/filetree.py todo
   ```
2. For each `added` item, read the file and write a fresh summary.
3. For each `changed` item, use `UNCHANGED` unless the old summary no longer
   describes the file purpose.
4. Pass decisions to `apply`:
   ```bash
   python filetree-skill-simple/scripts/filetree.py apply
   ```
   stdin shape:
   ```json
   {
     "updates": [{"path": "...", "hash": "...", "summary": "..." }],
     "removals": ["..."],
     "renames": [{"old_path": "...", "new_path": "..."}]
   }
   ```
   `summary` may be `UNCHANGED` for changed files.

## Lint

Run:

```bash
python filetree-skill-simple/scripts/filetree.py lint
```

Exit code `0` means clean. Exit code `1` means `FILETREE.md` has drift.

## Agent Wiring

To make agents discover this skill, reference this file from both instruction
entry points:

```markdown
- `./filetree-skill-simple/SKILL.md` - FILETREE.md maintenance skill. Read it
  before creating, updating, or linting FILETREE.md.
```

## Guardrails

- Do not commit automatically.
- Do not summarize skipped files; the script filters `FILETREE.md`, lock files,
  `.gitkeep`, and common binary/asset formats.
- Do not rewrite summaries just because hashes changed.
