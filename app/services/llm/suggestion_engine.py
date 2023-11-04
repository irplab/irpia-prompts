from abc import ABC, abstractmethod

from app.models.keywords import Keywords


class SuggestionEngine(ABC):
    """
    Base abstract class for suggestion engines
    """

    def __init__(self, engine_settings: dict):
        self.engine_settings = engine_settings

    @abstractmethod
    async def suggest(self, prompt: str) -> Keywords:
        """
        Abstract suggestion method

        :param prompt: the llm prompt
        :return: a Keywords object
        """
