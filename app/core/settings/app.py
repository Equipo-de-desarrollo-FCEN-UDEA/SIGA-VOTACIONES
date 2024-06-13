import logging
from typing import Any, Dict, Optional, Tuple, Union

from pydantic import PostgresDsn, SecretStr, validator, RedisDsn, MongoDsn, AnyHttpUrl

from app.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):
    # Configuración de la base de datos postgres
    postgres_server: str
    db_port: int
    db_user: str
    db_password: SecretStr
    db_name: str
    db_url: Optional[PostgresDsn] = None

    # App
    database_uri: Optional[PostgresDsn] = None

    