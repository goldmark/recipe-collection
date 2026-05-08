"""
Recipe validator.

Checks every file in recipes/ has the required sections.
Run locally: python scripts/validate_recipes.py
Used by:     .github/workflows/validate.yml
"""

import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Ingredients",
    "## Instructions",
    "## Notes",
    "## Variations",
]

REQUIRED_METADATA = [
    "**Cuisine:**",
    "**Servings:**",
    "**Prep time:**",
    "**Cook time:**",
    "**Difficulty:**",
]

RECIPES_DIR = Path(__file__).parent.parent / "recipes"


def validate_recipe(path: Path) -> list[str]:
    """Return a list of problems found in this recipe. Empty list = valid."""
    problems = []
    content = path.read_text(encoding="utf-8")

    # Must start with a top-level heading
    if not content.lstrip().startswith("# "):
        problems.append("missing top-level heading (# Recipe Name)")

    # Required metadata fields
    for field in REQUIRED_METADATA:
        if field not in content:
            problems.append(f"missing metadata field: {field}")

    # Required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            problems.append(f"missing section: {section}")

    return problems


def main() -> int:
    if not RECIPES_DIR.exists():
        print(f"❌ recipes/ directory not found at {RECIPES_DIR}")
        return 1

    recipe_files = sorted(RECIPES_DIR.glob("*.md"))
    if not recipe_files:
        print("⚠️  no recipe files found")
        return 0

    failures = 0
    for recipe in recipe_files:
        problems = validate_recipe(recipe)
        if problems:
            failures += 1
            print(f"❌ {recipe.name}")
            for problem in problems:
                print(f"     - {problem}")
        else:
            print(f"✅ {recipe.name}")

    print()
    print(f"Checked {len(recipe_files)} recipe(s), {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())