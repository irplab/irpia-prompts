from app.services.llm.gpt.gpt_completion_kw_suggestion_engine import GptCompletionKwSuggestionEngine
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.prompts.prompt_builder import PromptBuilder


class GptCompletionKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder to work with fine tuned models
    """

    @classmethod
    def _suggestion_engine(cls, engine_settings: dict) -> SuggestionEngine:
        return GptCompletionKwSuggestionEngine(engine_settings=engine_settings)

    @classmethod
    def _prompt_builder(cls, engine_settings: dict) -> PromptBuilder:
        return PromptBuilder("gpt-3.5-curie-ft-keywords.jinja2", engine_settings=engine_settings)
