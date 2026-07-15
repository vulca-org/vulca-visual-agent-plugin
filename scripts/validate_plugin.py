#!/usr/bin/env python3
"""Validate the repository-level Vulca plugin distribution contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_URL = "https://github.com/vulca-org/vulca-visual-agent-plugin"

JSON_PATHS = (
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".mcp.json",
    "gemini-extension.json",
    "hooks/hooks.json",
    "plugins/vulca/.codex-plugin/plugin.json",
    "plugins/vulca/.mcp.json",
)

CURRENT_REFERENCE_PATHS = (
    "README.md",
    "SUBMISSION.md",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "plugins/vulca/.codex-plugin/plugin.json",
)

LEGACY_REFERENCE_PATTERNS = (
    re.compile(r"vulca-org/vulca-plugin\b"),
    re.compile(r"github\.com/vulca-org/vulca(?:[/?#]|$)"),
)


def load_json(relative_path: str, errors: list[str]) -> Any:
    try:
        return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{relative_path}: {exc}")
        return None


def validate() -> list[str]:
    errors: list[str] = []
    documents = {path: load_json(path, errors) for path in JSON_PATHS}
    if errors:
        return errors
    if not all(isinstance(document, dict) for document in documents.values()):
        return ["every plugin JSON document must contain a top-level object"]

    version_values = {
        ".claude-plugin/plugin.json": documents[".claude-plugin/plugin.json"].get(
            "version"
        ),
        ".codex-plugin/plugin.json": documents[".codex-plugin/plugin.json"].get(
            "version"
        ),
        "plugins/vulca/.codex-plugin/plugin.json": documents[
            "plugins/vulca/.codex-plugin/plugin.json"
        ].get("version"),
        "gemini-extension.json": documents["gemini-extension.json"].get("version"),
        ".claude-plugin/marketplace.json metadata": documents[
            ".claude-plugin/marketplace.json"
        ]
        .get("metadata", {})
        .get("version"),
        ".claude-plugin/marketplace.json plugin": documents[
            ".claude-plugin/marketplace.json"
        ]
        .get("plugins", [{}])[0]
        .get("version"),
    }
    if len(set(version_values.values())) != 1 or None in version_values.values():
        errors.append(f"plugin versions are inconsistent: {version_values}")

    name_values = {
        documents[".claude-plugin/plugin.json"].get("name"),
        documents[".codex-plugin/plugin.json"].get("name"),
        documents["gemini-extension.json"].get("name"),
        documents["plugins/vulca/.codex-plugin/plugin.json"].get("name"),
    }
    if name_values != {"vulca"}:
        errors.append(f"internal plugin identity must remain 'vulca': {name_values}")

    repository_fields = {
        ".claude-plugin/plugin.json homepage": documents[
            ".claude-plugin/plugin.json"
        ].get("homepage"),
        ".codex-plugin/plugin.json homepage": documents[
            ".codex-plugin/plugin.json"
        ].get("homepage"),
        ".codex-plugin/plugin.json repository": documents[
            ".codex-plugin/plugin.json"
        ].get("repository"),
        ".codex-plugin/plugin.json websiteURL": documents[".codex-plugin/plugin.json"]
        .get("interface", {})
        .get("websiteURL"),
        "nested Codex manifest homepage": documents[
            "plugins/vulca/.codex-plugin/plugin.json"
        ].get("homepage"),
        "nested Codex manifest repository": documents[
            "plugins/vulca/.codex-plugin/plugin.json"
        ].get("repository"),
        "nested Codex manifest websiteURL": documents[
            "plugins/vulca/.codex-plugin/plugin.json"
        ]
        .get("interface", {})
        .get("websiteURL"),
    }
    for label, value in repository_fields.items():
        if value != REPOSITORY_URL:
            errors.append(f"{label} must be {REPOSITORY_URL!r}, got {value!r}")

    for relative_path in CURRENT_REFERENCE_PATHS:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for pattern in LEGACY_REFERENCE_PATTERNS:
            if pattern.search(text):
                errors.append(
                    f"{relative_path}: legacy repository reference matches {pattern.pattern!r}"
                )

    root_skills = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    nested_skills = {
        path.name for path in (ROOT / "plugins/vulca/skills").iterdir() if path.is_dir()
    }
    if root_skills != nested_skills:
        errors.append(
            "root and nested skill sets differ: "
            f"root={sorted(root_skills)}, nested={sorted(nested_skills)}"
        )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Vulca plugin validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Vulca plugin validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
