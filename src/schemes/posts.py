from datetime import datetime

from pydantic import BaseModel, Field


class Post(BaseModel):
    user_name: str | None = None
    text: str | None = None
    create_at: datetime = Field(default_factory=datetime.now)


class PostCreatedResponse(BaseModel):
    message: str
