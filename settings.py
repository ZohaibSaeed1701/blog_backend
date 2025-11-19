from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    DATABASE_URL: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
