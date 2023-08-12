"""
Suggestions routes
"""
from fastapi import APIRouter, Depends

from app.config import get_app_settings
from app.models.metadata import Metadata
from app.models.thread import Thread
from app.settings.app_settings import AppSettings

router = APIRouter()


@router.post("/keywords", response_model=Thread, name="suggest:keywords")
async def keywords(
        metadata: Metadata,
        settings: AppSettings = Depends(get_app_settings),
) -> Thread:
    """
    Create Keywords suggestion thread
    :param metadata: metadata hash
    :param settings: application settings
    :return: Thread with uri
    """
    uri = f"{settings.base_url}" \
          f"{settings.api_prefix}" \
          f"/{settings.api_version}" \
          f"/suggest/keywords/thread/1234"
    return Thread(uri=uri)
