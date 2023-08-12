"""
Settings for test environment
"""
import logging

from pydantic_settings import SettingsConfigDict

from app.settings.app_settings import AppSettings


class TestAppSettings(AppSettings):
    """
    Settings for test environment
    """
    debug: bool = True

    title: str = "Test FastAPI example application"

    logging_level: int = logging.DEBUG

    model_config = SettingsConfigDict(env_file='.TEST.env', extra='ignore')
