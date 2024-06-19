import logging
from typing import Any, Dict, Optional, Tuple, Union

from pydantic import PostgresDsn, SecretStr, validator, RedisDsn, MongoDsn, AnyHttpUrl

from app.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):

    # postgres
    postgres_server: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    # App
    database_uri: Optional[PostgresDsn] = None

    @validator("database_uri", pre=True)
    def validate_database_uri(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get('postgres_user'),
            password=values.get('postgres_password'),
            host=values.get('postgres_server'),
            path=f"/{values.get('postgres_db')}"
        )


    