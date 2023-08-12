'''
Desc: router for all API
'''
from fastapi import APIRouter

from app.api.routes import suggestions

router = APIRouter()
router.include_router(suggestions.router, tags=["suggestions"], prefix="/suggest")
