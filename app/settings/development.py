"""
Settings for development environment
"""
import logging

from app.settings.app_settings import AppSettings


class DevAppSettings(AppSettings):
    """
    Settings for development environment
    """
    debug: bool = True

    logging_level: int = logging.DEBUG
