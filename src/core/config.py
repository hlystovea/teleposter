from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    title: str = 'Teleposter'
    host: str = '0.0.0.0'
    bot_token: SecretStr = ...
    channel: int = ...
    api_url: str = 'http://localhost:8000'
    mongo_url: str = ...
    jwt_secret_key: SecretStr = ...
    cookie_name: str = 'auth-token'
    base_dir: Path = Path(__file__).resolve().parent.parent.parent
    media_root: Path = base_dir / 'media'

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


config = Settings()
