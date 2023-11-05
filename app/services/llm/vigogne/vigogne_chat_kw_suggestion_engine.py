import re

from transformers import GenerationConfig, TextStreamer

from app.models.keywords import Keywords
from app.services.llm.vigogne.vigogne_kw_suggestion_engine import VigogneKwSuggestionEngine


class VigogneChatKwSuggestionEngine(VigogneKwSuggestionEngine):
    """
    Concrete Vigogne suggestion engine to use with non chat models
    """

    def __init__(self, engine_settings: dict):
        super().__init__(engine_settings)
        self.streamer = TextStreamer(self.tokenizer,
                                     timeout=10.0,
                                     skip_prompt=True,
                                     skip_special_tokens=True)

    async def suggest(self, prompt: str):
        print(f"Using device : {self.model.device}")
        print(f"Prompt:\n{prompt}")
        history = [{"role": "user", "content": prompt}]
        input_ids = self.tokenizer.apply_chat_template(history, return_tensors="pt") \
            .to(self.model.device)
        input_length = input_ids.shape[1]
        generated_outputs = self.model.generate(
            input_ids=input_ids,
            generation_config=GenerationConfig(
                temperature=self.temperature,
                do_sample=self.temperature > 0.0,
                top_p=self.top_p,
                top_k=self.top_k,
                repetition_penalty=self.repetition_penalty,
                max_new_tokens=self.max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
            ),
            streamer=self.streamer,
            return_dict_in_generate=True,
        )

        generated_tokens = generated_outputs.sequences[0, input_length:]
        generated_text = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        print(generated_text)
        keywords = [self._strip_dash(kw) for kw in generated_text.split("\n")]
        return Keywords(keywords=keywords)

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^-\s+', '', line)
