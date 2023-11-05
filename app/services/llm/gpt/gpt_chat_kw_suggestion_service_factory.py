from app.services.llm.gpt.gpt_chat_kw_suggestion_engine import GptChatKwSuggestionEngine
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.prompts.prompt_builder import PromptBuilder


class GptChatKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder to work with non fine tuned models
    """
    @classmethod
    def _suggestion_engine(cls, engine_settings:dict) -> SuggestionEngine:
        return GptChatKwSuggestionEngine(engine_settings=engine_settings)

    @classmethod
    def _prompt_builder(cls, engine_settings: dict) -> PromptBuilder:
        return PromptBuilder("gpt-3.5-keywords.jinja2", engine_settings=engine_settings)
