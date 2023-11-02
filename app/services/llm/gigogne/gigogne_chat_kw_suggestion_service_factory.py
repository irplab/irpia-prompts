from app.services.llm.gigogne.gigogne_chat_kw_suggestion_engine import GigogneChatKwSuggestionEngine
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.prompts.prompt_builder import PromptBuilder
from app.settings.app_settings import AppSettings


class GigogneChatKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder to work with non fine tuned Gigogne model
    """
    @classmethod
    def _suggestion_engine(cls, settings: AppSettings) -> SuggestionEngine:
        return GigogneChatKwSuggestionEngine(settings)

    @classmethod
    def _prompt_builder(cls, settings: AppSettings) -> PromptBuilder:
        return PromptBuilder("gigogne-keywords.jinja2", settings)
