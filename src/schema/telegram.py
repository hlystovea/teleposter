from pydantic import BaseModel


class TelegramChat(BaseModel):
    id: int
    type: str
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_forum: bool | None = None


class TelegramMedia(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int | None = None


class TelegramPhotoSize(TelegramMedia):
    width: int
    height: int


class TelegramVideo(TelegramMedia):
    width: int
    height: int
    duration: int
    thumbnail: TelegramPhotoSize | None = None
    file_name: str | None = None
    mime_type: str | None = None


class TelegramMessage(BaseModel):
    text: str | None = None
    sender_chat: TelegramChat | None = None
    chat: TelegramChat | None = None
    photo: list[TelegramPhotoSize] | None = None
    video: TelegramVideo | None = None
    caption: str | None = None
