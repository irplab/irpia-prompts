'''
App settings base class
'''
import os

import yaml
from pydantic import DirectoryPath
from pydantic_settings import SettingsConfigDict, BaseSettings

from app.settings.app_env_types import AppEnvTypes


class AppSettings(BaseSettings):
    '''
    App settings base class
    '''

    @staticmethod
    def settings_file_path(filename: str) -> str:
        """
        Get the path of a settings file

        :param filename: The name of the settings file
        :return: The path of the settings file
        """
        return os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", filename
        )

    @staticmethod
    def dict_from_yml(yml_file: str) -> dict:
        """
        Load settings from yml file
        """
        with open(yml_file, encoding="utf8") as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    app_env: AppEnvTypes = AppEnvTypes.PROD
    debug: bool = False
    docs_url: str = "/docs"

    api_prefix: str = "/api"
    api_version: str = "v1"

    openai_api_key: str | None = None
    openai_kw_gpt_completion_model: str | None = None

    template_directory: DirectoryPath = "templates"

    engine: str = "vigogne-instruct"

    engines: dict = dict_from_yml(yml_file=settings_file_path(filename="engines.yml"))

    kw_suggestion_min_nb: int | None = None
    kw_suggestion_max_nb: int | None = None

    temperature: float | None = None
    top_p: float | None = None
    top_k: float | None = None
    repetition_penalty: float | None = None
    max_new_tokens: int | None = None
    model_name_or_path: str | None = None
    model_revision: str | None = None

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
