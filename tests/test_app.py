from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to DevOps Mastery Challenge!" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "UP"}

def test_api_info():
    client = app.test_client()
    response = client.get("/api/info")

    assert response.status_code == 200
    assert response.json == {
        "project": "DevOps Mastery Challenge",
        "version": "1.0",
        "framework": "Flask"
    }
