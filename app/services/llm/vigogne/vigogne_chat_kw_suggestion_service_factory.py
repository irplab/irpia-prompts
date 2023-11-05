from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.llm.suggestion_service_factory import SuggestionServiceFactory
from app.services.llm.vigogne.vigogne_chat_kw_suggestion_engine import VigogneChatKwSuggestionEngine
from app.services.prompts.prompt_builder import PromptBuilder


class VigogneChatKwSuggestionServiceFactory(SuggestionServiceFactory):
    """
    Factory to get concrete suggestion engine and prompt builder
    to work with non fine tuned Vigogne chat model
    """

    @classmethod
    def _suggestion_engine(cls, engine_settings: dict) -> SuggestionEngine:
        return VigogneChatKwSuggestionEngine(engine_settings=engine_settings)

    @classmethod
    def _prompt_builder(cls, engine_settings: dict) -> PromptBuilder:
        return PromptBuilder("vigogne-chat-keywords.jinja2", engine_settings=engine_settings)
