from abc import ABC, abstractmethod

from app.settings.app_settings import AppSettings


class SuggestionEngine(ABC):
    """
    Base abstract class for suggestion engines
    """

    def __init__(self, settings: AppSettings):
        self.settings = settings

    @abstractmethod
    async def suggest(self, prompt: str):
        """
        Abstract suggestion method

        :param prompt: the llm prompt
        """
