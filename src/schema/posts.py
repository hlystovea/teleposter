from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField

from schema.telegram import TelegramMessage


class Post(TelegramMessage):
    user_name: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    status: Literal['non-moderated', 'published'] = 'non-moderated'
    files: list[str] = []


class RequestPost(BaseModel):
    text: str | None = None
    caption: str | None = None
    files: list[str] = []


class ResponsePost(Post):
    id: ObjectIdField = Field(alias='_id', serialization_alias='id')


class ResponseMessage(BaseModel):
    message: str
