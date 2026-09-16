from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_project():

    response = client.post(
        "/projects/",
        json={
            "name": "Test Project",
            "repo_url": "https://github.com/test/project"
        }
    )

    assert response.status_code == 200