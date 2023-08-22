"""
Test the suggestions routes
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_suggestion():
    """
    Test the creation of suggestions
    """
    response = client.post("/api/v1/suggest/keywords", json={
        "title": "Foo",
        "description": "There goes my hero"
    })
    assert response.status_code == 200
    assert "keywords" in response.json()
    assert len(response.json()["keywords"]) == 2
    assert "foo" in response.json()["keywords"]


def test_create_suggestion_with_empty_metadata():
    """
    Test sening empty metadata to API
    """
    response = client.post("/api/v1/suggest/keywords", json={
        "title": "",
        "description": ""
    })
    assert response.status_code == 200
    assert "keywords" in response.json()
    assert len(response.json()["keywords"]) == 0
