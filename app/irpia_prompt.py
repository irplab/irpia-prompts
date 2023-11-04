import importlib
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.config import get_app_settings
from app.services.llm.suggestion_service import SuggestionService
from app.settings.app_settings import AppSettings


@asynccontextmanager
async def initialize_model(app: FastAPI) -> AsyncGenerator[SuggestionService, None]:
    """
    Initialize model service with appropiate engine

    :param app: FastAPI app
    :return: 
    """
    print("initializing service")
    app.model_service = _service_factory()
    print("service initialized")
    yield


def _service_factory() -> SuggestionService:
    settings: AppSettings = get_app_settings()
    if settings.engine not in settings.engines:
        raise ValueError(
            f"Invalid model engine {settings.engine}, choose among {list(settings.engines.keys())}")
    engine_settings = settings.engines.get(settings.engine)
    factory_class = _factory_class(engine_settings.get('kw_suggestion_service_factory_module'),
                                   engine_settings.get('kw_suggestion_service_factory_class'))
    return factory_class.suggestion_service(engine_settings.get("defaults"))


def _factory_class(engine_module: str, engine_class: str):
    return getattr(importlib.import_module(engine_module), engine_class)


class IrpiaPrompt(FastAPI):
    """
    FastAPI app to serve IRPIA prompt
    """

    def __init__(self):
        super().__init__(lifespan=initialize_model)
        settings = get_app_settings()

        self.model_service = None

        origins = [
            "http://localhost",
        ]

        self.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.include_router(api_router, prefix=f"{settings.api_prefix}/{settings.api_version}")
