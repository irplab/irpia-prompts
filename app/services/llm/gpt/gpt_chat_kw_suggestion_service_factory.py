from app.services.llm.gpt.gpt_chat_kw_suggestion_engine import GptChatKwSuggestionEngine
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.prompts.prompt_builder import PromptBuilder
from app.settings.app_settings import AppSettings


class GptChatKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder to work with non fine tuned models
    """
    @classmethod
    def _suggestion_engine(cls, settings: AppSettings) -> SuggestionEngine:
        return GptChatKwSuggestionEngine(settings)

    @classmethod
    def _prompt_builder(cls, settings: AppSettings) -> PromptBuilder:
        return PromptBuilder("gpt-3.5-keywords.jinja2", settings)
