import re

import torch

from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, TextStreamer


class GigogneChatKwSuggestionEngine(SuggestionEngine):
    """
    Concrete OpenAI suggestion engine to use with non fine-tuned models
    """

    def __init__(self, settings):
        super().__init__(settings)
        self.temperature = settings.gigogne_temperature
        self.top_p = settings.gigogne_top_p
        self.top_k = settings.gigogne_top_k
        self.repetition_penalty = settings.gigogne_repetition_penalty
        self.max_new_tokens = settings.gigogne_max_new_tokens
        model_name_or_path = settings.gigogne_model_name_or_path
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device for model : {device}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, padding_side="right", use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained(model_name_or_path, torch_dtype=torch.float16,
                                                          resume_download=True, offload_folder="offload").to(device)

        self.streamer = TextStreamer(self.tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

    async def suggest(self, prompt: str):
        history = [{"role": "user", "content": prompt}]
        print(f"Using device for tensor : {self.model.device}")
        input_ids = self.tokenizer.apply_chat_template(history, return_tensors="pt").to(self.model.device)
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
