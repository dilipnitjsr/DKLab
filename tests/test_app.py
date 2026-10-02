from app import create_app


def test_homepage_loads_and_contains_core_sections():
    app = create_app()
    app.config.update(TESTING=True)

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    text = response.get_data(as_text=True)
    assert "DKLab" in text
    assert 'id="research"' in text
    assert 'id="projects"' in text
    assert 'id="contact"' in text
    assert 'href="#"' not in text


def test_health_endpoint():
    app = create_app()
    app.config.update(TESTING=True)

    with app.test_client() as client:
        response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_security_headers():
    app = create_app()
    app.config.update(TESTING=True)

    with app.test_client() as client:
        response = client.get("/")

    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
    assert "geolocation=()" in response.headers["Permissions-Policy"]
