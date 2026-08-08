#!/usr/bin/env python3
"""Validate the built-in style library without external dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STYLES = ROOT / "styles"
CATALOG = STYLES / "catalog.md"
SKILL = ROOT / "SKILL.md"

REQUIRED_HEADINGS = [
    "## Identity",
    "## Use",
    "## Visual DNA",
    "## Style Lock",
    "## Page Behavior",
    "## Prompt Prefix",
    "## Quality Gate",
]
LOCK_TERMS = [
    "typography",
    "palette",
    "grid",
    "container",
    "text density",
    "image",
    "negative",
]


def main() -> int:
    errors: list[str] = []
    style_files = sorted(p for p in STYLES.glob("*.md") if p.name != "catalog.md")

    if len(style_files) != 5:
        errors.append(f"expected 5 built-in styles, found {len(style_files)}")

    catalog_text = CATALOG.read_text(encoding="utf-8") if CATALOG.exists() else ""
    skill_text = SKILL.read_text(encoding="utf-8") if SKILL.exists() else ""

    if "styles/catalog.md" not in skill_text:
        errors.append("SKILL.md must route style selection through styles/catalog.md")

    for path in style_files:
        text = path.read_text(encoding="utf-8")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.name}: missing heading {heading}")
        if len(set(re.findall(r"#[0-9A-Fa-f]{6}", text))) < 4:
            errors.append(f"{path.name}: palette must contain at least 4 hex colors")
        lock = text.split("## Style Lock", 1)[-1].split("## Page Behavior", 1)[0]
        for term in LOCK_TERMS:
            if term not in lock.lower():
                errors.append(f"{path.name}: Style Lock missing {term}")
        if f"({path.name})" not in catalog_text:
            errors.append(f"catalog.md: missing link to {path.name}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    print(f"[OK] validated {len(style_files)} styles")
    print("[OK] catalog links and Style Lock contracts are complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())

