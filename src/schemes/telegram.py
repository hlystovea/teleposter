from pydantic import BaseModel

from schemes.posts import Post


class TelegramChat(BaseModel):
    id: int
    type: str
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_forum: bool | None = None


class TelegramPhotoSize(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int


class TelegramMessage(Post):
    sender_chat: TelegramChat | None = None
    chat: TelegramChat | None = None
    photo: list[TelegramPhotoSize] | None = None
    caption: str | None = None
