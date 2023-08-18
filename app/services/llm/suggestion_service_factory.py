from abc import ABC, abstractmethod

from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service import SuggestionService
from app.services.prompts.prompt_builder import PromptBuilder
from app.settings.app_settings import AppSettings


class SuggestionServiceFactory(ABC):
    """
    Creates suggestion services with concrete suggestion engine and prompt builder
    """

    @classmethod
    @abstractmethod
    def _suggestion_engine(cls, settings: AppSettings) -> SuggestionEngine:
        pass

    @classmethod
    @abstractmethod
    def _prompt_builder(cls, settings: AppSettings) -> PromptBuilder:
        pass

    @classmethod
    def suggestion_service(cls, settings: AppSettings) -> SuggestionService:
        """
        Return suggestion service with concrete suggestion engine and prompt builder
        :param settings:
        :return:
        """
        return SuggestionService(prompt_builder=cls._prompt_builder(settings),
                                 engine=cls._suggestion_engine(settings),
                                 settings=settings)
