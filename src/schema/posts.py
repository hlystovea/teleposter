from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField

from schema.telegram import TelegramMessage


class PostStatus(str, Enum):
    NON_MODERATED = 'non-moderated'
    MODERATED = 'moderated'
    PUBLISHED = 'published'


class Post(TelegramMessage):
    user_name: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    status: PostStatus = PostStatus.NON_MODERATED
    files: list[str] = []

    def __init__(self, **kwargs):
        kwargs['text'] = kwargs.get('text') or kwargs.get('caption')
        super().__init__(**kwargs)


class RequestPost(BaseModel):
    text: str | None = None
    files: list[str] = []


class ResponsePost(Post):
    id: ObjectIdField = Field(alias='_id', serialization_alias='id')


class ResponseMessage(BaseModel):
    message: str
