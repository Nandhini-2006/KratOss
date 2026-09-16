from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_signup():

    response = client.post(
        "/auth/signup",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "Test1234"
        }
    )

    assert response.status_code in [200, 400]