# Copilot Instructions

This is a personal recipe collection. When suggesting content for files in this repo, follow these conventions.

## Recipe file structure

All recipes in `recipes/` follow this exact structure:

```md
# Recipe Name

**Cuisine:** _e.g., Italian_
**Servings:** _e.g., 4_
**Prep time:** _e.g., 10 min_
**Cook time:** _e.g., 20 min_
**Difficulty:** _Easy / Medium / Hard_

## Ingredients

- Item with quantity (e.g., "200g spaghetti", "2 cloves garlic, minced")

## Instructions

1. Numbered steps, written as full sentences in imperative mood.
2. One action per step where possible.

## Notes

- Honest feedback after cooking — what worked, what to change.
- Substitutions, timing tips, what to watch out for.

## Variations

- Optional twists, regional alternatives, dietary swaps.
```

## Style guidelines

- **Ingredients:** use metric units (g, ml) by default. Include preparation in the ingredient line ("finely chopped", "minced"), not in the steps.
- **Instructions:** start each step with a verb. Keep them concise — one action per step. Don't re-state ingredient quantities in steps.
- **Notes:** write in first person, casual tone. These are honest cooking notes, not marketing copy.
- **Tone:** conversational, opinionated, no filler. Avoid phrases like "delicious", "perfect", "amazing".

## Filenames

- Lowercase, hyphenated: `shakshuka.md`, `pad-thai.md`, `apple-pie.md`.
- Place all recipes in the `recipes/` directory.

## When adding a new recipe

- Use the structure above exactly.
- Suggest realistic, accurate ingredient quantities.
- Keep total recipe under ~50 lines unless the dish genuinely needs more.

## When updating the README

- Add new recipes to the table in alphabetical order.
- Match the existing column format: name (linked), cuisine, time, difficulty.

## Validation

- All recipes are validated automatically by GitHub Actions on push and PR.
- The script checks for required metadata fields and sections.
- Run locally before committing: `python scripts/validate_recipes.py`
