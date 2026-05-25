# AI-Human Research Template Instructions

This repository is a reusable research workspace for human researchers and AI coding
agents such as Codex and Claude Code. Every agent must read this file first, then use
the file tree below as the source of truth for where to find inputs, write notes, run
analysis, and prepare deliverables.

## Core Principles

1. Keep raw inputs untouched. Do not edit or overwrite files in `01_sources/` unless
   the human explicitly asks for it.
2. Keep claims traceable. Important claims in notes, drafts, and deliverables should
   point back to source files, citations, page numbers, URLs, dataset rows, or analysis
   outputs whenever possible.
3. Separate raw, processed, and generated work. Put original data in
   `01_sources/datasets/`, cleaned data in `03_analysis/data_processed/`, and analysis
   outputs in `03_analysis/outputs/`.
4. Log decisions and assumptions. Update `00_project/research_log.md` or
   `00_project/decisions.md` when a non-trivial methodological, analytical, or writing
   decision is made.
5. Be explicit about uncertainty. Do not fabricate sources, citations, quotes, data, or
   results. Mark uncertain points as open questions.
6. Prefer small, reviewable changes. Preserve the human's work and avoid broad
   reorganization unless requested.

## File Tree

```text
.
|-- AGENTS.md
|-- CLAUDE.md
|-- README.md
|-- instruction.md
|-- paper_skeleton.md
|-- 00_project/
|   |-- research_brief.md
|   |-- research_log.md
|   `-- decisions.md
|-- 01_sources/
|   |-- README.md
|   |-- papers/
|   |-- datasets/
|   |-- web/
|   `-- transcripts/
|-- 02_literature/
|   |-- reading_queue.md
|   |-- literature_matrix.md
|   `-- summaries/
|-- 03_analysis/
|   |-- README.md
|   |-- data_raw/
|   |-- data_processed/
|   |-- notebooks/
|   |-- scripts/
|   `-- outputs/
|-- 04_writing/
|   |-- outline.md
|   |-- draft.md
|   |-- claims_and_evidence.md
|   `-- figures_tables/
|-- 05_prompts/
|   |-- reusable_prompts.md
|   `-- agent_session_notes.md
`-- 06_deliverables/
    |-- README.md
    |-- manuscript/
    |-- slides/
    `-- submission/
```

## File and Folder Meanings

### Root files

- `AGENTS.md`: Entry instruction for Codex and other agentic coding tools. Keep it as:
  `READ [instruction.md](instruction.md) first.`
- `CLAUDE.md`: Entry instruction for Claude Code. Keep it as:
  `READ [instruction.md](instruction.md) first.`
- `instruction.md`: The canonical operating guide for humans and AI agents.
- `README.md`: Human-facing overview for how to start a new research project from this
  template.
- `paper_skeleton.md`: General manuscript skeleton that can be copied into
  `04_writing/draft.md` or adapted for a specific venue.

### `00_project/`

Project-level context and governance.

- `research_brief.md`: The human-owned research brief. Fill this first when starting a
  new project.
- `research_log.md`: Chronological log of important work, changes, findings, and open
  questions.
- `decisions.md`: Record major research design, analysis, writing, and tooling
  decisions with rationale.

### `01_sources/`

Original source material. Treat this folder as the immutable evidence base.

- `papers/`: PDFs, bibliographic exports, preprints, and published articles.
- `datasets/`: Original datasets exactly as received or downloaded.
- `web/`: Saved web pages, URLs, screenshots, and copied metadata.
- `transcripts/`: Interview transcripts, meeting transcripts, field notes, or
  observation records.

### `02_literature/`

Human-readable literature processing.

- `reading_queue.md`: Papers and sources to read, prioritize, or revisit.
- `literature_matrix.md`: Comparative table for sources, methods, findings, limitations,
  and relevance.
- `summaries/`: One-file-per-source notes, summaries, annotations, and extraction
  sheets.

### `03_analysis/`

Computational and analytical work.

- `data_raw/`: Local working copies of raw data when needed for scripts. Keep originals
  in `01_sources/datasets/`.
- `data_processed/`: Cleaned, normalized, coded, or transformed data.
- `notebooks/`: Exploratory notebooks.
- `scripts/`: Reusable analysis, cleaning, scraping, or validation scripts.
- `outputs/`: Generated figures, tables, logs, reports, model outputs, and intermediate
  analysis results.

### `04_writing/`

Research argument and manuscript development.

- `outline.md`: Current paper, report, or chapter outline.
- `draft.md`: Main working draft.
- `claims_and_evidence.md`: Claim-level evidence map linking assertions to sources or
  analysis outputs.
- `figures_tables/`: Working versions of figures and tables for the manuscript.

### `05_prompts/`

Reusable AI collaboration material.

- `reusable_prompts.md`: Prompts that are useful across sessions.
- `agent_session_notes.md`: Short records of AI sessions, including what was asked, what
  changed, and what still needs human review.

### `06_deliverables/`

Final or near-final artifacts.

- `manuscript/`: Submitted or shareable manuscript versions.
- `slides/`: Presentation decks.
- `submission/`: Cover letters, supplementary materials, response letters, exports, and
  venue-specific files.

## Recommended Workflow for a New Research Project

1. Clone this template into a new project folder.
2. Fill in `00_project/research_brief.md`.
3. Put original materials into `01_sources/`.
4. Use `02_literature/` for reading notes and literature synthesis.
5. Use `03_analysis/` for scripts, notebooks, cleaned data, and outputs.
6. Use `04_writing/` for outlines, evidence mapping, and drafts.
7. Move stable final artifacts into `06_deliverables/`.
8. Keep `00_project/research_log.md` updated so future humans and agents can recover
   project state quickly.

## Agent Operating Rules

When acting as an AI agent in this repository:

1. Read `instruction.md`, then inspect `00_project/research_brief.md` and
   `00_project/research_log.md` before making substantive changes.
2. If the task involves sources, inspect the relevant files in `01_sources/` and record
   citation details or uncertainty.
3. If the task involves writing, update `04_writing/claims_and_evidence.md` when adding
   or changing important claims.
4. If the task involves analysis, put code in `03_analysis/scripts/` or
   `03_analysis/notebooks/`, processed data in `03_analysis/data_processed/`, and outputs
   in `03_analysis/outputs/`.
5. Before deleting, moving, or rewriting source material, ask for human confirmation.
6. At the end of a substantive session, add a concise note to
   `05_prompts/agent_session_notes.md` or `00_project/research_log.md` if the work
   changes project state.

## Naming Conventions

- Use descriptive lowercase file names with hyphens or underscores.
- For source summaries, prefer `author-year-short-title.md`.
- For dated logs or outputs, prefer `YYYY-MM-DD-short-description.ext`.
- For generated versions, include enough metadata to identify the method or script that
  created them.

## Citation and Evidence Expectations

- Quotes need page numbers, timestamps, URLs, or other precise locators when available.
- Paraphrases still need source attribution.
- Generated summaries must identify which source file they summarize.
- Analysis claims should point to the script, notebook, data file, or output that
  supports them.
