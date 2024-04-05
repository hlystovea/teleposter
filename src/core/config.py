from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    host: str = '127.0.0.1'
    port: int = 8000
    bot_token: SecretStr = ...
    admin_chat_id: int = ...
    channel: str = ...

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


config = Settings()
