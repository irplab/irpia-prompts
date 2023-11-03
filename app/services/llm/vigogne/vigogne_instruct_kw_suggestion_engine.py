import re

import torch

from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, TextStreamer
from vigogne.preprocess import generate_instruct_prompt

class VigogneInstructKwSuggestionEngine(SuggestionEngine):
    """
    Concrete Vigogne suggestion engine to use with instruct models
    """

    def __init__(self, settings):
        super().__init__(settings)
        self.temperature = settings.vigogne_temperature
        self.top_p = settings.vigogne_top_p
        self.top_k = settings.vigogne_top_k
        self.repetition_penalty = settings.vigogne_repetition_penalty
        self.max_new_tokens = settings.vigogne_max_new_tokens
        model_name_or_path = settings.vigogne_model_name_or_path
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device for model : {device}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, padding_side="right", use_fast=False)
        self.model = model = AutoModelForCausalLM.from_pretrained(model_name_or_path, torch_dtype=torch.float16,
                                                                  resume_download=True, offload_folder="offload").to(
            device)
    async def suggest(self, prompt: str):
        prompt = generate_instruct_prompt(prompt)
        print(f"Using device for tensor : {self.model.device}")
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
        print(generated_text)
        keywords = [self._strip_dash(kw) for kw in generated_text.split("\n")]
        return Keywords(keywords=keywords)

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^-\s+', '', line)
