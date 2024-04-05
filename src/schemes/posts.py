from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


def now():
    return datetime.now()


class BasePost(BaseModel):
    user_id: int | None = None
    text: str


class RequestPost(BasePost):
    create_at: datetime = Field(default_factory=now)


class TelegramPost(BasePost):
    model_config = ConfigDict(from_attributes=True)

    def __init__(self, **kwargs):
        kwargs['user_id'] = kwargs['chat']['id']
        super().__init__(**kwargs)


class ResponsePost(BaseModel):
    message: str
