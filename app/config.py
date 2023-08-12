'''
Setting classes loader
'''
from functools import lru_cache
from typing import Dict, Type

from app.settings.app_env_types import AppEnvTypes

from app.settings.app_settings import AppSettings
from app.settings.development import DevAppSettings
from app.settings.production import ProdAppSettings
from app.settings.test import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.DEV: DevAppSettings,
    AppEnvTypes.PROD: ProdAppSettings,
    AppEnvTypes.TEST: TestAppSettings,
}


@lru_cache()
def get_app_settings() -> AppSettings:
    """

    :return:
    """
    app_env = AppSettings().app_env
    config = environments[app_env]
    return config()
