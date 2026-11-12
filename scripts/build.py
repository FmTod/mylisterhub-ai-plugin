"""Check the package and build the upload ZIPs into dist/.

dist/chatgpt.zip: Agent Plugins package for the ChatGPT plugin directory.
dist/claude.zip:  Claude plugin for claude.ai (Customize > Plugins > Upload plugin).

Run from the repo root: python3 scripts/build.py
"""

import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

# claude.ai rejects skill uploads with any other frontmatter key.
SKILL_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

SHARED = ["skills", "assets"]
BUNDLES = {
    "chatgpt.zip": ["plugin.json", "mcp.json", *SHARED],
    "claude.zip": [".claude-plugin/plugin.json", ".mcp.json", *SHARED],
}


def check() -> None:
    portable = json.loads((ROOT / "plugin.json").read_text())
    claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    for key in ("name", "version"):
        assert portable[key] == claude[key], f"{key} differs between plugin.json and .claude-plugin/plugin.json"

    portable_url = json.loads((ROOT / "mcp.json").read_text())["mcpServers"]["mylisterhub"]["url"]
    claude_url = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]["mylisterhub"]["url"]
    assert portable_url == claude_url, "MCP server URL differs between mcp.json and .mcp.json"

    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        match = re.match(r"---\n(.*?)\n---\n", skill.read_text(), re.S)
        assert match, f"{skill}: missing frontmatter"
        fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
        assert set(fields) <= SKILL_KEYS, f"{skill}: unsupported keys {set(fields) - SKILL_KEYS}"
        assert fields.get("name") == skill.parent.name, f"{skill}: name must match its folder"
        assert 0 < len(fields.get("description", "")) <= 200, f"{skill}: description must be 1-200 characters"


def build() -> None:
    DIST.mkdir(exist_ok=True)
    for name, paths in BUNDLES.items():
        with zipfile.ZipFile(DIST / name, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in paths:
                source = ROOT / path
                files = sorted(source.rglob("*")) if source.is_dir() else [source]
                for file in files:
                    if file.is_file():
                        archive.write(file, file.relative_to(ROOT).as_posix())
        print(f"dist/{name}")


if __name__ == "__main__":
    check()
    build()
