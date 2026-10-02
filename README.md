# DKLab Website

A Flask-based responsive homepage for DKLab.in.

## Run locally

```bash
python -m venv .venv
```

### Windows
```bash
.venv\Scripts\activate
pip install flask
python app.py
```

### Linux / macOS
```bash
source .venv/bin/activate
pip install flask
python app.py
```

Open:

http://127.0.0.1:5000

## Structure

dklab_website/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

The homepage is intentionally built without a database so the visual design can be deployed first.
Content can later be moved into MongoDB/PostgreSQL and individual pages/routes can be added.
