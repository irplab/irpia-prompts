"""
Test the suggestions routes
"""
import re

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_suggestion():
    """
    Test the creation of a suggestion thread
    """
    response = client.post("/api/v1/suggest/keywords", json={
        "title": "Foo",
        "description": "There goes my hero"
    })
    assert response.status_code == 200
    assert "uri" in response.json()
    assert re.match('.+/suggest/keywords/thread/[0-9]+', response.json()["uri"])
