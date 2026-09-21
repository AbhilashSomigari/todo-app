# todo-app

A small CRUD todo list built with Flask and Flask-SQLAlchemy. Add, update,
and delete todos through a Bootstrap-styled web UI backed by SQLite.

## Project layout

```
app.py                    Flask app, routes, and the Todo model
templates/
  base.html                Shared layout/navbar
  index.html                Todo list + "add a todo" form
  update.html               "Edit a todo" form
requirements.txt          Dependencies
procfile                  Process entrypoint for gunicorn-based deploys
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The app starts at http://127.0.0.1:5000 and creates a local `todo.db`
SQLite file on first run.

## Routes

| Method | Route              | Description                          |
|--------|--------------------|---------------------------------------|
| GET    | `/`                | List all todos                        |
| POST   | `/`                | Add a todo (`title`, `desc` fields)   |
| GET    | `/update/<SNo>`    | Show the edit form for a todo         |
| POST   | `/update/<SNo>`    | Save edits to a todo                  |
| GET    | `/delete/<SNo>`    | Delete a todo                         |

Requesting `/update/<SNo>` or `/delete/<SNo>` for an id that doesn't exist
returns a 404.

## Deployment

The included `procfile` runs the app with gunicorn:

```
web: gunicorn app:app
```
