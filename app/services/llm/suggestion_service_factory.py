from abc import ABC, abstractmethod

from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service import SuggestionService
from app.services.prompts.prompt_builder import PromptBuilder


class SuggestionServiceFactory(ABC):
    """
    Creates suggestion services with concrete suggestion engine and prompt builder
    """

    @classmethod
    @abstractmethod
    def _suggestion_engine(cls, engine_settings: dict) -> SuggestionEngine:
        pass

    @classmethod
    @abstractmethod
    def _prompt_builder(cls, engine_settings: dict) -> PromptBuilder:
        pass

    @classmethod
    def suggestion_service(cls, engine_settings: dict) -> SuggestionService:
        """
        Return suggestion service with concrete suggestion engine and prompt builder
        :param settings:
        :return:
        """
        return SuggestionService(prompt_builder=cls._prompt_builder(engine_settings),
                                 engine=cls._suggestion_engine(engine_settings),
                                 engine_settings=engine_settings)
