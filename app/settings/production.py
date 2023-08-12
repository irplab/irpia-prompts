"""
Settings for production environment
"""
import logging

from app.settings.app_settings import AppSettings


class ProdAppSettings(AppSettings):
    """
    Settings for production environment
    """
    debug: bool = False

    title: str = "FastAPI example application"

    logging_level: int = logging.INFO
