from pydantic import SecretStr, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    title: str = 'Teleposter'
    host: str = '0.0.0.0'
    bot_token: SecretStr = ...
    channel: int = ...
    api_url: HttpUrl = 'http://localhost:8000'
    mongo_url: str = ...

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


config = Settings()
