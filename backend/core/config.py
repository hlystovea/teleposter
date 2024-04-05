from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    debug: bool = False
    host: str = '127.0.0.1'
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


app_settings = AppSettings()
