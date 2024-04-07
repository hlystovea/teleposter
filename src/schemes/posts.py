from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_mongo import ObjectIdField


class Post(BaseModel):
    user_name: str | None = None
    text: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    status: Literal['non-moderated', 'published'] = 'non-moderated'


class ResponsePost(Post):
    id: ObjectIdField = Field(alias='_id', serialization_alias='id')


class ResponseMessage(BaseModel):
    message: str
