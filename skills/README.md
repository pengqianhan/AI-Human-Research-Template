# Skills

This folder contains optional research skills that can be installed with
`setup.md`. Use this file as the lightweight index; open an individual
`SKILL.md` only when that skill is relevant to the current task.

## Available Skills

- `uv/`: Checks and installs the `uv` Python package manager required by the
  script-based skills.
- `literature_search_arxiv/`: Searches arXiv metadata and downloads arXiv PDFs,
  HTML pages, or source archives.
- `literature_search_biorxiv/`: Searches bioRxiv and medRxiv metadata by DOI or
  narrow date/category ranges.
- `literature_search_europepmc/`: Searches Europe PMC open-access literature and
  retrieves PDFs, full text, citations, or references.
- `literature_search_openalex/`: Queries OpenAlex for works, authors,
  institutions, topics, sources, funders, and bibliometric metadata.
- `workflow_skill_creator/`: Distills a completed research workflow into a
  reusable agent skill.

## Layout

Each skill directory should include a `SKILL.md`. Some skills also include
`scripts/` for helper CLIs and `references/` for syntax or API notes.
