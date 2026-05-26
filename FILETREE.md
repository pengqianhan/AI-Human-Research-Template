# Project Filetree

_Auto-maintained by the filetree skill. Each entry carries a content hash; mismatched hashes indicate stale summaries._

## (root)/

- `.gitignore` - Ignores local environment files, editor settings, caches, scratch directories, and agent-local data. <!--hash:0cb2335a-->
- `AGENTS.md` - Empty placeholder for Codex-style agent entry instructions. <!--hash:e69de29b-->
- `CLAUDE.md` - Claude Code entry instruction that directs agents to read instruction.md first. <!--hash:ddbdd451-->
- `README.md` - Human-facing overview of the AI-Human Research OS template, startup workflow, folder layout, and roadmap. <!--hash:29697560-->
- `instruction.md` - Primary guide for the research template structure, folder purposes, and agent collaboration rules. <!--hash:a179083b-->
- `setup.md` - One-time setup instructions for installing bundled research skills into Claude Code or Codex user directories. <!--hash:d0769f47-->

## .agents/skills/filetree-simple/

- `SKILL.md` - Skill instructions for maintaining FILETREE.md with one-line summaries and content hashes. <!--hash:7a602f9a-->

## .agents/skills/filetree-simple/scripts/

- `filetree.py` - Helper CLI that detects FILETREE.md drift, applies summary decisions, and lints hashes. <!--hash:887fc826-->

## Paper/

- `paper_skeleton.md` - Starter outline for manuscripts, reports, or research notes. <!--hash:eacef85c-->

## References/

- `paper_notes.md` - Empty workspace for shared paper-reading notes and key takeaways. <!--hash:e69de29b-->
- `refs.bib` - Empty BibTeX bibliography placeholder for project references. <!--hash:e69de29b-->

## Research-skills-hub/

- `README.md` - Index of optional research skills and their directory layout. <!--hash:59de986f-->

## Research-skills-hub/skills/literature_search_arxiv/

- `SKILL.md` - Skill instructions for arXiv search, metadata extraction, and paper or source retrieval. <!--hash:d2895c25-->

## Research-skills-hub/skills/literature_search_arxiv/references/

- `query_syntax.md` - Reference for arXiv advanced query prefixes, boolean operators, grouping, phrases, and date filters. <!--hash:713d2726-->

## Research-skills-hub/skills/literature_search_arxiv/scripts/

- `download_paper.py` - CLI helper that downloads arXiv papers as PDF or HTML to a specified output path. <!--hash:87468fae-->
- `download_paper_source.py` - CLI helper that downloads arXiv source archives to a specified output path. <!--hash:07f54446-->
- `search_arxiv.py` - CLI helper that queries arXiv by search expression or ID list and emits normalized JSON metadata. <!--hash:f68b184a-->

## Research-skills-hub/skills/literature_search_biorxiv/

- `SKILL.md` - Skill instructions for bioRxiv and medRxiv metadata lookup by DOI or narrow date/category search. <!--hash:3f870265-->

## Research-skills-hub/skills/literature_search_biorxiv/scripts/

- `search_by_dates.py` - CLI helper that searches bioRxiv or medRxiv date ranges with category, author, and keyword filters. <!--hash:194c1ca6-->
- `search_by_doi.py` - CLI helper that fetches bioRxiv or medRxiv metadata for a known DOI. <!--hash:87d776d1-->

## Research-skills-hub/skills/literature_search_europepmc/

- `SKILL.md` - Skill instructions for Europe PMC open-access literature search, PDFs, full text, citations, and references. <!--hash:0acc481f-->

## Research-skills-hub/skills/literature_search_europepmc/scripts/

- `europepmc_api.py` - CLI helper for Europe PMC search, PDF download, full-text retrieval, citations, and reference lists. <!--hash:694aba7c-->

## Research-skills-hub/skills/literature_search_openalex/

- `SKILL.md` - Skill instructions for OpenAlex scholarly search, entity resolution, bibliometrics, metadata filters, and open-access PDF retrieval. <!--hash:c7a1b779-->

## Research-skills-hub/skills/literature_search_openalex/references/

- `authors.md` - OpenAlex reference listing author entity fields available for sorting, grouping, and filtering. <!--hash:bc01d643-->
- `geo_and_language.md` - OpenAlex reference for continent, country, and language fields used to filter or group scholarly output. <!--hash:f2bb8428-->
- `institutions.md` - OpenAlex reference listing institution entity fields for sorting, grouping, and filtering. <!--hash:6963f83e-->
- `publishers_funders.md` - OpenAlex reference listing publisher and funder fields for sorting, grouping, and filtering. <!--hash:01f2d742-->
- `sources.md` - OpenAlex reference listing source venue fields for sorting, grouping, and filtering. <!--hash:136e702d-->
- `taxonomy.md` - OpenAlex reference for domain, field, subfield, topic, and SDG taxonomy fields. <!--hash:9c4a1c8e-->
- `topics.md` - OpenAlex reference listing topic fields and hierarchy filters. <!--hash:836869c8-->
- `type_values.md` - OpenAlex reference for work, source, institution, license, and keyword type entities. <!--hash:783e0147-->
- `works.md` - OpenAlex reference listing scholarly work fields for sorting, grouping, and filtering. <!--hash:bc5a0b74-->

## Research-skills-hub/skills/literature_search_openalex/scripts/

- `openalex_cli.py` - CLI helper for OpenAlex entity resolution, lookup, filtering, rate-limit checks, and PDF downloads. <!--hash:91c899ec-->

## Research-skills-hub/skills/uv/

- `SKILL.md` - Skill instructions for checking, installing, and exposing uv for script-based research skills. <!--hash:08b9625a-->

## Research-skills-hub/skills/workflow_skill_creator/

- `SKILL.md` - Workflow for distilling a completed interaction into a reusable agent skill with design, implementation, and validation phases. <!--hash:5d61d5e5-->

## Research-skills-hub/skills/workflow_skill_creator/references/

- `cli_script_template.py` - Reusable CLI template for API-backed skills with subcommands, JSON file output, retries, and rate limiting. <!--hash:352961aa-->
