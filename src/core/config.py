from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    title: str = 'Teleposter'
    host: str = '0.0.0.0'
    bot_token: SecretStr = ...
    channel: str = ...
    api_schema: str = 'http'
    api_domain: str = 'localhost'
    api_port: int = ...
    mongo_url: str = ...

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )

    @property
    def api_url(self) -> str:
        return f'{self.api_schema}://{self.api_domain}:{self.api_port}'


config = Settings()
