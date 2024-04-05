from datetime import datetime

from pydantic import BaseModel, Field


def now():
    return datetime.now()


class Post(BaseModel):
    user_id: int
    text: str
    create_at: datetime = Field(default_factory=now)
