from functools import lru_cache
from locale import setlocale, LC_TIME, Error as LocaleError
import logging

from typing import Type, Dict

from app.core.settings.app import AppSettings
from app.core.settings.base import AppEnv, BaseAppSettings
from app.core.settings import DevelopmentAppSettings

environments: Dict[AppEnv, Type[AppSettings]] = {
    AppEnv.Development: DevelopmentAppSettings
    # AppEnv.Production: ProductionAppSettings,
    # AppEnv.Testing: TestingAppSettings
}

logger = logging.getLogger(__name__)

try:
    setlocale(LC_TIME, 'es_ES.UTF-8')
except LocaleError:
    logger.warning("Locale 'es_ES.UTF-8' not supported, using default locale")


# Aquí generamos la configuración de la aplicación y la almacenamos en la caché de python
@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().env
    config = environments[app_env]
    return config
