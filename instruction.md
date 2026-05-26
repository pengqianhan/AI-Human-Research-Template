# AI-Human Research Template Instructions

This repository is a lightweight template for research projects where humans work with
AI agents such as Codex or Claude Code.

Research is iterative. Ideas, references, experiments, figures, and writing often update
each other, so the folders are organized by material type instead of by a fixed sequence
of steps.

## File Tree

Generated from `git ls-files | grep -Ev '(^|/)\.gitkeep$'`. The `skills/`
subtree is summarized because skill details live in `skills/README.md`.

```text
.
|-- .gitignore
|-- AGENTS.md
|-- CLAUDE.md
|-- README.md
|-- instruction.md
|-- paper_skeleton.md
|-- setup.md
|-- Code/
|-- Datasets/
|-- Figs/
|-- Ideas/
|-- References/
|   |-- paper_notes.md
|   `-- refs.bib
`-- skills/
    |-- README.md
    |-- literature_search_arxiv/
    |-- literature_search_biorxiv/
    |-- literature_search_europepmc/
    |-- literature_search_openalex/
    |-- uv/
    `-- workflow_skill_creator/
```

## What Goes Where

- `.gitignore`: Ignore local, generated, or environment-specific files.
- `AGENTS.md`: Entry-point instructions for Codex-style agents. It points agents
  to `instruction.md`.
- `CLAUDE.md`: Entry-point instructions for Claude Code-style agents.
- `README.md`: Human-facing overview of the Research OS template and starting
  workflow.
- `instruction.md`: The main guide for humans and AI agents.
- `setup.md`: One-time setup steps after cloning this template for a new research
  project.
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
- `References/paper_notes.md`: Shared notes for reading papers and recording key
  takeaways.
- `References/refs.bib`: Project bibliography file for BibTeX-compatible
  citations.
- `skills/`: Research initialization skills. Install them during setup using
  `setup.md`. Read `skills/README.md` only when skill details are needed.
- `skills/README.md`: Short index of available skills and their intended use.
- Empty research folders may contain `.gitkeep` files so Git can track them.

## Agent Rules

1. Read this file first.
2. If this is a newly cloned project, read `setup.md` next.
3. Treat research as iterative. Do not assume work must move through the folders in a
   fixed order.
4. Preserve original datasets and references unless explicitly asked to modify them.
5. Keep claims traceable to references, notes, data, code, or figures.
6. Do not invent citations, quotes, data, or results.
7. Ask before deleting or rewriting user-provided research materials.
