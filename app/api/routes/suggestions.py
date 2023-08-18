"""
Suggestions routes
"""
import importlib

from fastapi import APIRouter, Depends

from app.config import get_app_settings
from app.models.keywords import Keywords
from app.models.metadata import Metadata
from app.services.llm.suggestion_service import SuggestionService
from app.settings.app_settings import AppSettings

router = APIRouter()


def _service_factory(settings: AppSettings) -> SuggestionService:
    factory_class = _factory_class(settings.kw_suggestion_service_factory_module,
                                   settings.kw_suggestion_service_factory_class)
    return factory_class.suggestion_service(settings)


def _factory_class(engine_module: str, engine_class: str):
    return getattr(importlib.import_module(engine_module), engine_class)


@router.post("/keywords", response_model=Keywords, name="suggest:keywords")
async def suggest_keywords(
        metadata: Metadata,
        settings: AppSettings = Depends(get_app_settings),
) -> Keywords:
    """
    Create Keywords suggestion thread
    :param metadata: metadata hash
    :param settings: application settings
    :return: Thread with uri
    """
    service = _service_factory(settings)
    keywords = await service.suggest(metadata)
    return keywords
