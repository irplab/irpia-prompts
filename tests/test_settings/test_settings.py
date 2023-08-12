"""
Settings customizations tests
"""
import re

from fastapi.testclient import TestClient

from app.config import get_app_settings
from app.main import app
from app.settings.app_settings import AppSettings


def get_settings_override():
    """
    Override default settings

    :return: custom app settings
    """
    return AppSettings(api_prefix="/any_prefix",
                       api_version="any_version",
                       base_url='http://testserver')


client = TestClient(app)

app.dependency_overrides[get_app_settings] = get_settings_override


def test_api_path():
    """
    Test setting usage in URI generation
    """
    response = client.post("/api/v1/suggest/keywords",
                           json={"title": "Foo", "description": "There goes my hero"})
    assert response.status_code == 200
    assert re.match(
        'http://testserver/any_prefix/any_version/suggest/keywords/thread/[0-9]+',
        response.json()["uri"]
    )
