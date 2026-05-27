# Setup

Use this file once after cloning the template for a new research project.

## Install Research Skills

The `Research-skills-hub` folder contains research initialization skills and a skills map (`Research-skills-hub\skills_map.md`) that outlines the available skills. Install them into the
user-level skills directory for the code agent you will use.

### Claude Code

macOS/Linux:

```bash
mkdir -p ~/.claude/skills/
cp -r skills/* ~/.claude/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$HOME\.claude\skills\"
```

### Codex

macOS/Linux:

```bash
mkdir -p ~/.agents/skills/
cp -r skills/* ~/.agents/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$HOME\.agents\skills\"
```
