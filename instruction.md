# AI-Human Research Template Instructions

This repository is a lightweight template for research projects where humans work with
AI agents such as Codex or Claude Code.

Research is iterative. Ideas, references, experiments, figures, and writing often update
each other, so the folders are organized by material type instead of by a fixed sequence
of steps.

## File Tree

```text
.
|-- AGENTS.md
|-- CLAUDE.md
|-- instruction.md
|-- paper_skeleton.md
|-- Code/
|-- Datasets/
|-- Figs/
|-- Ideas/
|-- References/
`-- skills/
```

## What Goes Where

- `AGENTS.md`: Entry point for Codex and similar agents. Keep it as
  `READ [instruction.md](instruction.md) first.`
- `CLAUDE.md`: Entry point for Claude Code. Keep it as
  `READ [instruction.md](instruction.md) first.`
- `instruction.md`: The main guide for humans and AI agents.
- `paper_skeleton.md`: A simple paper/report writing skeleton.
- `Code/`: Scripts, notebooks, analysis code, data processing code, and small helper
  tools.
- `Datasets/`: Raw or processed datasets. Preserve original data when possible, and do
  not overwrite user-provided data without confirmation.
- `Figs/`: Figures, tables, plots, screenshots, and visual outputs used for analysis or
  writing.
- `Ideas/`: Research ideas, evolving hypotheses, notes, outlines, meeting notes,
  experiment plans, and reflections after reading or analysis.
- `References/`: Papers, bibliographic files, literature notes, source PDFs, links, and
  citation material.
- `skills/`: Research initialization skills. When starting a new research project from
  this template, copy these skills into the user-level skills directory for the code
  agent being used.

## Installing Skills During Initialization

If the project will use Claude Code:

```bash
mkdir -p ~/.claude/skills/
cp -r skills/* ~/.claude/skills/
```

If the project will use Codex:

```bash
mkdir -p ~/.agents/skills/
cp -r skills/* ~/.agents/skills/
```

For Claude Code on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$HOME\.claude\skills\"
```

For Codex on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$HOME\.agents\skills\"
```

## Agent Rules

1. Read this file first.
2. Treat research as iterative. Do not assume work must move through the folders in a
   fixed order.
3. Preserve original datasets and references unless explicitly asked to modify them.
4. Keep claims traceable to references, notes, data, code, or figures.
5. Do not invent citations, quotes, data, or results.
6. Ask before deleting or rewriting user-provided research materials.
