# LazyPuzzle

An early Django learning project for a puzzle and verbal-riddle catalog, with themes, user accounts, and administration models.

## Code organization

- `LazyPuzzle/` — Django settings and root URL configuration.
- `Storage/` — puzzle/riddle models, forms, views and templates.
- `Users/` — account-related views and routes.
- `manage.py` — Django management entry point.

The settings identify Django 4.0.3 as the original generation version, but no dependency manifest is included.

## Local exploration

Create an isolated Python environment and establish a compatible Django dependency set before running the management commands:

```sh
python manage.py check
python manage.py migrate
python manage.py runserver
```

These are exploration steps, not a verified quick start. Prefer a new SQLite database over the checked-in `db.sqlite3` after reviewing what data needs to be preserved.

## Known prototype issues

Some views refer to templates that are absent or use different directory casing. The riddle gallery filters `is_published` directly even though publication state belongs to the related `BasicSettings` model. These need correction before the affected pages work reliably.

The repository tracks a database, Python bytecode, development settings and a Django secret key. Use a new key and review database contents before any deployment. Treat this project as a learning archive.
