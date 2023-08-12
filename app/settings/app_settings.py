'''
App settings base class
'''
from pydantic_settings import SettingsConfigDict, BaseSettings

from app.settings.app_env_types import AppEnvTypes


class AppSettings(BaseSettings):
    '''
    App settings base class
    '''
    app_env: AppEnvTypes = AppEnvTypes.PROD
    debug: bool = False
    docs_url: str = "/docs"

    base_url: str = "http://localhost:8000"

    api_prefix: str = "/api"
    api_version: str = "v0"

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
