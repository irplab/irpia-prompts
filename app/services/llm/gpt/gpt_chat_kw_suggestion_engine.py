import re

import openai

from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine


class GptChatKwSuggestionEngine(SuggestionEngine):
    """
    Concrete OpenAI suggestion engine to use with non fine-tuned models
    """

    async def suggest(self, prompt: str):
        openai.api_key = self.settings.openai_api_key
        model = self.settings.openai_chat_gpt_model
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0
        )
        content: str = response.choices[0].message["content"]
        keywords = [self._strip_dash(kw) for kw in content.split("\n")]
        return Keywords(keywords=keywords)

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^-\s+', '', line)
