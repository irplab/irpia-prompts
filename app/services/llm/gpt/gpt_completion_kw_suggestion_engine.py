import re

import openai

from app.config import get_app_settings
from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine
from app.settings.app_settings import AppSettings


class GptCompletionKwSuggestionEngine(SuggestionEngine):
    """
    Concrete OpenAI suggestion engine to use with fine-tuned models
    """

    async def suggest(self, prompt: str):
        settings: AppSettings = get_app_settings()
        assert settings.openai_api_key is not None, "OpenAI API key not set"
        openai.api_key = settings.openai_api_key
        model = settings.openai_kw_gpt_completion_model \
                or settings.model_name_or_path \
                or self.engine_settings.get("model_name_or_path")
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            stop=[" END"]
        )
        content: str = response.choices[0].text
        keywords = [self._strip_dash(kw) for kw in content.split("\n")]
        return Keywords(keywords=keywords)

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^\s*-\s*', '', line)
