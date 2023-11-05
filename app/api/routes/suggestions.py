"""
Suggestions routes
"""

from fastapi import APIRouter
from starlette.requests import Request

from app.models.keywords import Keywords
from app.models.metadata import Metadata
from app.services.llm.suggestion_service import SuggestionService

router = APIRouter()

service: SuggestionService = None


@router.post("/keywords", response_model=Keywords, name="suggest:keywords")
async def suggest_keywords(
        metadata: Metadata,
        request: Request
) -> Keywords:
    """
    Create Keywords suggestion thread
    :param metadata: metadata hash
    :param settings: application settings
    :return: Thread with uri
    """
    assert request.app.model_service is not None, "service not initialized"
    keywords = await request.app.model_service.suggest(metadata)
    return keywords
