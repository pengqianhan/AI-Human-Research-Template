#!/usr/bin/env python3
"""Deterministic FILETREE.md maintenance helpers."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


MANIFEST_PATH = Path("FILETREE.md")

SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".svg", ".bmp",
    ".woff", ".woff2", ".ttf", ".otf", ".eot",
    ".mp4", ".mp3", ".wav", ".ogg", ".webm",
    ".zip", ".tar", ".gz", ".bz2", ".7z",
    ".pdf", ".psd", ".ai",
}

SKIP_FILENAMES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "Cargo.lock", "poetry.lock", "Pipfile.lock", "go.sum",
    ".gitkeep", "FILETREE.md",
}

ENTRY_RE = re.compile(
    r"^- `([^`]+)` (?:-|\u2014) (.+?) <!--hash:([a-f0-9]+)-->\s*$"
)
SECTION_RE = re.compile(r"^## (.+?)/?\s*$")


def require_git() -> None:
    """Require a git repository; change detection depends on git."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            check=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.exit(
            "Error: filetree requires a git repository.\n"
            "Run `git init` first, then rerun this command."
        )


def should_skip(path: str) -> bool:
    p = Path(path)
    return p.suffix.lower() in SKIP_EXTENSIONS or p.name in SKIP_FILENAMES


def list_current_files() -> list[str]:
    """Return tracked plus untracked-unignored files, deduped and sorted."""
    tracked = subprocess.check_output(
        ["git", "-c", "core.quotePath=false", "ls-files", "-z"],
        encoding="utf-8",
    ).split("\0")

    staged = subprocess.check_output(
        ["git", "-c", "core.quotePath=false", "ls-files", "--stage", "-z"],
        encoding="utf-8",
    ).split("\0")
    gitlinks = {
        rec.split("\t", 1)[1]
        for rec in staged
        if rec.startswith("160000 ") and "\t" in rec
    }

    untracked = subprocess.check_output(
        [
            "git",
            "-c",
            "core.quotePath=false",
            "ls-files",
            "--others",
            "--exclude-standard",
            "-z",
        ],
        encoding="utf-8",
    ).split("\0")

    files = set(tracked) | set(untracked)
    return sorted(f for f in files if f and f not in gitlinks and not should_skip(f))


def hash_files(paths: list[str]) -> dict[str, str]:
    """Return {path: 8-char git object hash} for paths."""
    if not paths:
        return {}

    proc = subprocess.run(
        ["git", "hash-object", "--stdin-paths"],
        input="\n".join(paths),
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    hashes = proc.stdout.strip().splitlines()
    if len(hashes) != len(paths):
        raise RuntimeError(f"git hash-object returned {len(hashes)} hashes for {len(paths)} paths")
    return {path: digest[:8] for path, digest in zip(paths, hashes)}


def detect_renames() -> list[tuple[str, str]]:
    """Return staged rename pairs from git status porcelain output."""
    out = subprocess.check_output(
        ["git", "-c", "core.quotePath=false", "status", "--porcelain=v1", "-z"],
        encoding="utf-8",
    )

    fields = out.split("\0")
    renames: list[tuple[str, str]] = []
    i = 0
    while i < len(fields):
        entry = fields[i]
        if len(entry) < 4:
            i += 1
            continue
        xy = entry[:2]
        new_path = entry[3:]
        if xy[0] in ("R", "C") and i + 1 < len(fields):
            renames.append((fields[i + 1], new_path))
            i += 2
        else:
            i += 1
    return renames


def _unquote_git_path(value: str) -> str:
    """Decode legacy quoted git paths; leave normal paths unchanged."""
    if len(value) < 2 or value[0] != '"' or value[-1] != '"':
        return value

    inner = value[1:-1]
    raw = bytearray()
    i = 0
    while i < len(inner):
        char = inner[i]
        if char == "\\" and i + 1 < len(inner):
            nxt = inner[i + 1]
            if nxt in "01234567" and i + 4 <= len(inner):
                raw.append(int(inner[i + 1:i + 4], 8))
                i += 4
                continue
            simple = {"n": 0x0A, "t": 0x09, "r": 0x0D, "\\": 0x5C, '"': 0x22}
            raw.append(simple.get(nxt, ord(nxt)))
            i += 2
        else:
            raw.append(ord(char))
            i += 1
    return raw.decode("utf-8", errors="replace")


def parse_manifest() -> list[dict[str, str]]:
    """Read FILETREE.md into entries with path, summary, and hash."""
    if not MANIFEST_PATH.exists():
        return []

    entries: list[dict[str, str]] = []
    section = ""
    for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        section_match = SECTION_RE.match(line)
        if section_match:
            section = section_match.group(1).strip().rstrip("/").replace("\\", "/")
            if section == "(root)":
                section = ""
            continue

        entry_match = ENTRY_RE.match(line)
        if not entry_match:
            continue

        filename, summary, digest = entry_match.groups()
        filename = _unquote_git_path(filename)
        if "/" in filename:
            path = filename
        elif section:
            path = f"{section}/{filename}"
        else:
            path = filename
        entries.append({"path": path, "summary": summary.strip(), "hash": digest})
    return entries


def write_manifest(entries: list[dict[str, str]]) -> None:
    """Group by directory, sort stably, and write FILETREE.md."""
    by_dir: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        directory = str(PurePosixPath(entry["path"]).parent)
        if directory == ".":
            directory = ""
        by_dir.setdefault(directory, []).append(entry)

    lines = [
        "# Project Filetree",
        "",
        "_Auto-maintained by the filetree skill. Each entry carries a content hash; mismatched hashes indicate stale summaries._",
        "",
    ]

    for directory in sorted(by_dir):
        heading = f"{directory}/" if directory else "(root)/"
        lines.append(f"## {heading}")
        lines.append("")
        for entry in sorted(by_dir[directory], key=lambda item: item["path"]):
            filename = PurePosixPath(entry["path"]).name
            lines.append(f"- `{filename}` - {entry['summary']} <!--hash:{entry['hash']}-->")
        lines.append("")

    tmp = MANIFEST_PATH.with_name(MANIFEST_PATH.name + ".tmp")
    tmp.write_text("\n".join(lines), encoding="utf-8")
    tmp.replace(MANIFEST_PATH)


def cmd_todo() -> dict:
    """Diff current repository files against FILETREE.md."""
    require_git()
    current_paths = set(list_current_files())
    manifest = parse_manifest()
    manifest_by_path = {entry["path"]: entry for entry in manifest}

    renames = [
        {"old_path": old, "new_path": new}
        for old, new in detect_renames()
        if old in manifest_by_path and not should_skip(new)
    ]
    renamed_olds = {item["old_path"] for item in renames}
    renamed_news = {item["new_path"] for item in renames}

    added_paths = sorted(current_paths - set(manifest_by_path) - renamed_news)
    removed = sorted(set(manifest_by_path) - current_paths - renamed_olds)
    common = sorted(current_paths & set(manifest_by_path))

    hashes = hash_files(common + added_paths)

    changed = []
    for path in common:
        if hashes[path] != manifest_by_path[path]["hash"]:
            changed.append(
                {
                    "path": path,
                    "old_summary": manifest_by_path[path]["summary"],
                    "old_hash": manifest_by_path[path]["hash"],
                    "new_hash": hashes[path],
                }
            )

    return {
        "added": [{"path": path, "hash": hashes[path]} for path in added_paths],
        "changed": changed,
        "removed": removed,
        "renamed": renames,
        "stats": {
            "total_in_repo": len(current_paths),
            "total_in_manifest": len(manifest_by_path),
            "need_llm": len(added_paths) + len(changed),
        },
    }


def cmd_apply(payload: str) -> dict[str, int]:
    """Apply summary decisions to FILETREE.md."""
    require_git()
    updates = json.loads(payload)
    current_paths = set(list_current_files())
    by_path = {entry["path"]: entry for entry in parse_manifest()}

    for rename in updates.get("renames", []):
        old_path = rename["old_path"]
        new_path = rename["new_path"]
        if old_path in by_path and new_path in current_paths:
            entry = by_path.pop(old_path)
            entry["path"] = new_path
            entry["hash"] = hash_files([new_path]).get(new_path, entry["hash"])
            by_path[new_path] = entry

    for path in updates.get("removals", []):
        by_path.pop(path, None)

    for update in updates.get("updates", []):
        path = update["path"]
        digest = update["hash"]
        summary = update["summary"]
        if path not in current_paths:
            continue
        if summary == "UNCHANGED":
            if path in by_path:
                by_path[path]["hash"] = digest
        else:
            by_path[path] = {"path": path, "hash": digest, "summary": summary}

    write_manifest(list(by_path.values()))
    return {"total_entries": len(by_path)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["todo", "lint", "apply"])
    args = parser.parse_args()

    if args.command in ("todo", "lint"):
        result = cmd_todo()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.command == "lint":
            drift = (
                len(result["added"])
                + len(result["changed"])
                + len(result["removed"])
                + len(result["renamed"])
            )
            sys.exit(0 if drift == 0 else 1)
        return

    result = cmd_apply(sys.stdin.read())
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
