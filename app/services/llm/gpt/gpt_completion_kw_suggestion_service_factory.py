from app.services.llm.gpt.gpt_completion_kw_suggestion_engine import GptCompletionKwSuggestionEngine
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.prompts.prompt_builder import PromptBuilder
from app.settings.app_settings import AppSettings


class GptCompletionKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder to work with fine tuned models
    """

    @classmethod
    def _suggestion_engine(cls, settings: AppSettings) -> SuggestionEngine:
        return GptCompletionKwSuggestionEngine(settings)

    @classmethod
    def _prompt_builder(cls, settings: AppSettings) -> PromptBuilder:
        return PromptBuilder("gpt-3.5-curie-ft-keywords.jinja2", settings)
