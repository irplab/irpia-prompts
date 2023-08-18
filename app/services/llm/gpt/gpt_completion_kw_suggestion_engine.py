import re

import openai

from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine


class GptCompletionKwSuggestionEngine(SuggestionEngine):
    """
    Concrete OpenAI suggestion engine to use with fine-tuned models
    """

    async def suggest(self, prompt: str):
        openai.api_key = self.settings.openai_api_key
        model = self.settings.openai_kw_gpt_completion_model
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
