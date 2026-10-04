# Taskwolf - Panel

[![CI](https://github.com/taskwolf-net/taskwolf-panel/actions/workflows/ci.yml/badge.svg)](https://github.com/taskwolf-net/taskwolf-panel/actions/workflows/ci.yml)

This is the repository that manages all functionalities of the web panel in the frontend and the middleware. It provides the central interface for employees to answer tickets and emails. It also performs other administrative tasks.

## Installation

```bash
python -m venv env

source env/bin/activate

pip install django gunicorn django-cors-headers requests jwt

django-admin compilemessages

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Run

```bash
source env/bin/activate

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Compile locales

```bash
django-admin compilemessages
```
