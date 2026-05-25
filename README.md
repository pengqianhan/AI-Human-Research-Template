# AI-Human Research Template

This repository is a lightweight template for research projects where humans work with
AI agents such as Codex or Claude Code.

The folder structure is intentionally simple and non-linear. Research ideas,
references, experiments, figures, and writing often update each other, so the folders
are organized by material type rather than by a fixed workflow.

## Start a New Research Project

1. Clone this template for the new research project.
2. Open the project with the code agent you plan to use, such as Codex or Claude Code.
3. Ask the agent to read `setup.md` and run the one-time initialization steps for that
   agent.
4. After setup, use `instruction.md` as the long-term guide for human-AI collaboration
   in the project.

## Folders

- `Code/`: Scripts, notebooks, analysis code, and helper tools.
- `Datasets/`: Raw or processed datasets.
- `Figs/`: Figures, tables, plots, screenshots, and visual outputs.
- `Ideas/`: Research ideas, hypotheses, outlines, meeting notes, and reflections.
- `References/`: Papers, bibliographic files, source PDFs, links, and citation material.
- `skills/`: Research initialization skills installed through `setup.md`.

## TODO

1. Design this template as a CLI so agents can use commands to understand the whole
   research project.
2. Design bash commands that make agents deterministically read specific files, such as
   `instruction.md`, at the start of each session.
3. Add `read_paper` workflow， which manages the process of reading a paper, including summarizing it, extracting key points, and relating it to the research project. The workflow can be used in both `Ideas/` and `References/` folders. Besides, when AI meet a problem that it cannot solve, it can use this workflow to read relevant papers and find solutions. All the new reading papers will be stored in `References/` folder, and the summary and key points will be stored in `Ideas/` folder.
3. Add a workspace where holding a group meeting with humans and AI, humans discuss research with the AI. Because AI can search paper and read fast, they can point out if the idea is feasible or not, and they can also point out relevant papers that humans might miss. This can be a good way to brainstorm research ideas and get feedback on them. After discussion, the AI can implement the idea or feadback immediately.
4. The final goal of the repo is to build a Research OS.
