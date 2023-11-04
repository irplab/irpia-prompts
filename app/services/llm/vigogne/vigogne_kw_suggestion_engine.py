import re
from abc import abstractmethod, ABC

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.config import get_app_settings
from app.models.keywords import Keywords
from app.services.llm.suggestion_engine import SuggestionEngine
from app.settings.app_settings import AppSettings


class VigogneKwSuggestionEngine(SuggestionEngine, ABC):
    """
    Concrete Vigogne suggestion engine to use with instruct models
    """

    def __init__(self, engine_settings):
        super().__init__(engine_settings)
        settings: AppSettings = get_app_settings()
        self.temperature = float(settings.temperature
                                 or self.engine_settings.get("temperature")
                                 or 0)
        self.top_p = float(settings.top_p
                           or self.engine_settings.get("top_p")
                           or 0)
        self.top_k = int(settings.top_k
                         or self.engine_settings.get("top_k")
                         or 0)
        self.repetition_penalty = float(
            settings.repetition_penalty
            or self.engine_settings.get("repetition_penalty")
            or 0)
        self.max_new_tokens = int(settings.max_new_tokens
                                  or self.engine_settings.get("max_new_tokens")
                                  or 0)
        model_name_or_path = settings.model_name_or_path \
                             or self.engine_settings.get("model_name_or_path")
        assert model_name_or_path, "No model name or path provided"
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device for model : {device}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path,
                                                       padding_side="right",
                                                       use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                                          torch_dtype=torch.float16,
                                                          resume_download=True,
                                                          offload_folder="offload",
                                                          device_map=device)

    @abstractmethod
    async def suggest(self, prompt: str) -> Keywords:
        """
        Abstract suggestion method

        :param prompt: the llm prompt
        :return: a Keywords object
        """

    @classmethod
    def _strip_dash(cls, line):
        return re.sub(r'^-\s+', '', line)
