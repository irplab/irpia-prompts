from app.models.keywords import Keywords
from app.models.metadata import Metadata
from app.services.llm.suggestion_engine import SuggestionEngine
from app.services.prompts.prompt_builder import PromptBuilder


class SuggestionService:
    """
    Service to suggest values from various endpoints
    """

    def __init__(self, prompt_builder: PromptBuilder,
                 engine: SuggestionEngine, engine_settings: dict):
        self.prompt_builder = prompt_builder
        self.engine = engine
        self.engine_settings = engine_settings

    async def suggest(self, metadata: Metadata) -> Keywords:
        """
        Suggest keywords
        :param metadata:
        :return:
        """
        if f"{metadata.title} {metadata.description}".isspace():
            return Keywords(keywords=[])
        prompt = self.prompt_builder.build(metadata)

        return await self.engine.suggest(prompt)
