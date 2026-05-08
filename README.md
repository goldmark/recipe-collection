# 🍳 Recipe Collection

A demo project for exploring a modern developer workflow: Git, GitHub, Copilot, and Markdown. The recipes are illustrative sample content. This is not a real personal collection, but the content is structured as if it were. The goal is to have realistic files that show how an AI assistant can help maintain a project like this.

## What's in here

- **[recipes/](./recipes/)** — the recipes themselves, one per file
- **[templates/](./templates/)** — a starter template for adding new recipes

## Recipes

| Recipe | Cuisine | Time | Difficulty |
|---|---|---|---|
| [Bread Pudding](./recipes/bread-pudding.md) | British | 60 min | Easy |
| [Chicken Tikka Masala](./recipes/chicken-tikka-masala.md) | Indian | 45 min | Medium |
| [Chocolate Chip Cookies](./recipes/chocolate-chip-cookies.md) | Dessert | 30 min | Easy |
| [Pasta Carbonara](./recipes/pasta-carbonara.md) | Italian | 20 min | Easy |
| [Shakshuka](./recipes/shakshuka.md) | Middle Eastern | 30 min | Easy |

## Adding a new recipe

1. Copy `templates/recipe-template.md` into `recipes/`
2. Rename it to `your-recipe-name.md` (lowercase, hyphens)
3. Fill in the sections
4. Add it to the table above
5. Open a Pull Request

## Conventions

- Ingredients are listed in the order they're used
- Times include prep + cook
- Notes section is for honest feedback after cooking — what to change next time

## Validation

Every recipe is checked automatically by GitHub Actions on push and PR. The check verifies the file has all required metadata and sections.

Run it locally:

```bash
python scripts/validate_recipes.py
```

---

*Maintained by one person who likes to cook and likes Git.*
