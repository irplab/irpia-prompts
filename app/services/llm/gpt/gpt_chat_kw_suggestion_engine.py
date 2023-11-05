import re

import openai

from app.config import get_app_settings
from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine
from app.settings.app_settings import AppSettings


class GptChatKwSuggestionEngine(SuggestionEngine):
    """
    Concrete OpenAI suggestion engine to use with non fine-tuned models
    """

    async def suggest(self, prompt: str):
        settings: AppSettings = get_app_settings()
        assert settings.openai_api_key is not None, "OpenAI API key not set"
        openai.api_key = settings.openai_api_key
        model = settings.model_name_or_path or self.engine_settings.get("model_name_or_path")
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=float(settings.temperature or self.engine_settings.get("temperature") or 0),
        )
        content: str = response.choices[0].message["content"]
        keywords = [self._strip_dash(kw) for kw in content.split("\n")]
        return Keywords(keywords=keywords)

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^-\s+', '', line)
