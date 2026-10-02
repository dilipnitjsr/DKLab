# DKLab Website

Official Flask-based website starter for **DKLab.in** — AI, Machine Learning & Intelligent Systems Research Lab.

## Features

- Responsive single-page research-lab website.
- Flask application factory for testing and deployment.
- `/healthz` health endpoint for reverse proxies and hosting platforms.
- Basic browser security headers.
- Production WSGI deployment with Gunicorn.
- Automated tests and GitHub Actions CI.
- No database or secrets required for the current static-content phase.

## Local setup

```bash
python -m venv .venv
```

### Linux / macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Windows

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

Debug mode is **off by default**. For local development only:

```bash
FLASK_DEBUG=1 python app.py
```

## Production deployment

Run behind a reverse proxy or managed platform with Gunicorn:

```bash
gunicorn --bind 0.0.0.0:${PORT:-8000} app:app
```

The included `Procfile` uses this command.

Health check:

```text
GET /healthz
→ {"status":"ok"}
```

## Tests

```bash
pytest
```

CI verifies the homepage, health endpoint, security headers, and key navigation/content invariants.

## Structure

```text
.
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Next phase

The site is intentionally database-free for now. Future content such as publications, people, projects, datasets, and news can be moved into structured data or a CMS/database while preserving the current routes and design.
