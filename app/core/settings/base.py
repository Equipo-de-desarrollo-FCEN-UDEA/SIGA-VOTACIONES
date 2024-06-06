from enum import Enum
from pydantic import BaseSettings

class AppEnv(Enum):
    Development: str = "development"
    
class BaseAppSetting(BaseSettings):
    env: AppEnv = AppEnv.Development
    class Config:
        env_file=".env"