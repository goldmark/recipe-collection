# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a demo project used to showcase developer workflows (Git, GitHub, Markdown, AI tooling). The recipe content is illustrative — it is not a real personal collection. There is no code, build system, or dependencies. All content is `.md` files.

## Structure

- `recipes/` — Individual recipe files (one per dish)
- `templates/recipe-template.md` — Canonical template; all new recipes must follow this structure
- `README.md` — Main index; contains a table listing all recipes — update it when adding or removing a recipe
- `.github/PULL_REQUEST_TEMPLATE.md` — Checklist for recipe PRs

## Recipe Conventions

Recipes follow a fixed front-matter block then standard sections:

```
# Recipe Name
**Cuisine:** | **Servings:** | **Prep time:** | **Cook time:** | **Difficulty:**

## Ingredients
## Instructions
## Notes
## Variations
```

- Ingredients are listed in order of use
- The `Notes` section is written as if from actual cooking experience — it is illustrative first-person prose for demo realism
- Filenames are lowercase with hyphens matching the recipe title (e.g., `chicken-tikka-masala.md`)
- Difficulty is one of: Easy / Medium / Hard

## Workflow

New recipes are added via feature branch + PR. The PR template at `.github/PULL_REQUEST_TEMPLATE.md` has the checklist to follow. README.md recipe table must be kept in sync with the `recipes/` directory.
