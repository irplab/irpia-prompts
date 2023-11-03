from app.services.llm.vigogne.vigogne_chat_kw_suggestion_engine import VigogneChatKwSuggestionEngine
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.llm.vigogne.vigogne_instruct_kw_suggestion_engine import VigogneInstructKwSuggestionEngine
from app.services.prompts.prompt_builder import PromptBuilder
from app.settings.app_settings import AppSettings


class VigogneInstructKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder to work with non fine tuned Vigogne instruct model
    """
    @classmethod
    def _suggestion_engine(cls, settings: AppSettings) -> SuggestionEngine:
        return VigogneInstructKwSuggestionEngine(settings)

    @classmethod
    def _prompt_builder(cls, settings: AppSettings) -> PromptBuilder:
        return PromptBuilder("vigogne-keywords.jinja2", settings)
