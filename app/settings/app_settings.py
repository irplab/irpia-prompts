'''
App settings base class
'''
from pydantic import DirectoryPath
from pydantic_settings import SettingsConfigDict, BaseSettings

from app.settings.app_env_types import AppEnvTypes


class AppSettings(BaseSettings):
    '''
    App settings base class
    '''
    app_env: AppEnvTypes = AppEnvTypes.PROD
    debug: bool = False
    docs_url: str = "/docs"

    api_prefix: str = "/api"
    api_version: str = "v0"

    openai_api_key: str = "missing key"
    openai_chat_gpt_model: str = "missing key"
    openai_kw_gpt_completion_model: str = "missing key"

    template_directory: DirectoryPath = "templates"

    # kw_suggestion_service_factory_module: str = "app.services.llm.gpt" \
    #                                             ".gpt_chat_kw_suggestion_service_factory"
    # kw_suggestion_service_factory_class: str = "GptChatKwSuggestionServiceFactory"
    kw_suggestion_service_factory_module: str = "app.services.llm.vigogne" \
                                                ".vigogne_chat_kw_suggestion_service_factory"
    kw_suggestion_service_factory_class: str = "VigogneChatKwSuggestionServiceFactory"
    kw_suggestion_min_nb: int = 1
    kw_suggestion_max_nb: int = 10

    vigogne_temperature: float = float(0.1) # 0.7 for vigogne chat
    vigogne_top_p: float = float(1.0)
    vigogne_top_k: float = float(0)
    vigogne_repetition_penalty: float = float(1.0)
    vigogne_max_new_tokens: int = 512
    # vigogne_model_name_or_path: str = "bofenghuang/vigogne-2-70b-chat"
    vigogne_model_name_or_path: str = "bofenghuang/vigogne-2-7b-chat"

    # model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    model_config = SettingsConfigDict(env_file='.llm.chat.env', extra='ignore')
