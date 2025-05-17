import re

from transformers import GenerationConfig

from app.models.keywords import Keywords
from app.services.llm.vigogne.vigogne_gptq_kw_suggestion_engine import VigogneGPTQKwSuggestionEngine


class VigogneInstructGPTQKwSuggestionEngine(VigogneGPTQKwSuggestionEngine):
    """
    Concrete Vigogne suggestion engine to use with instruct models
    """

    async def suggest(self, prompt: str):
        print(f"Using device : {self.model.device}")
        print(f"Prompt:\n{prompt}")
        input_ids = self.tokenizer(prompt, return_tensors="pt")["input_ids"].to(self.model.device)
        input_length = input_ids.shape[1]
        generated_outputs = self.model.generate(
            input_ids=input_ids,
            generation_config=GenerationConfig(
                temperature=self.temperature,
                do_sample=self.temperature > 0.0,
                repetition_penalty=self.repetition_penalty,
                max_new_tokens=self.max_new_tokens,
            ),
            return_dict_in_generate=True,
        )
        generated_tokens = generated_outputs.sequences[0, input_length:]
        generated_text = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        print(f"Generated text:\n{generated_text}")
        keywords = [self._strip_dash(kw.strip()) for kw in generated_text.split("\n") if kw.strip()]
        return Keywords(keywords=keywords)

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^-*\d*\.*\s+', '', line)
