from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr = ...
    channel: int = ...


    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


config = Settings()
