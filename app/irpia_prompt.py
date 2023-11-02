import importlib
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.config import get_app_settings
from app.services.llm.suggestion_service import SuggestionService
from app.settings.app_settings import AppSettings


@asynccontextmanager
async def initialize_model(app: FastAPI):
    settings: AppSettings = get_app_settings()
    app.model_service = _service_factory(settings)
    print("service initialized")
    yield


def _service_factory(settings: AppSettings) -> SuggestionService:
    factory_class = _factory_class(settings.kw_suggestion_service_factory_module,
                                   settings.kw_suggestion_service_factory_class)
    return factory_class.suggestion_service(settings)


def _factory_class(engine_module: str, engine_class: str):
    return getattr(importlib.import_module(engine_module), engine_class)


class IrpiaPrompt(FastAPI):

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
