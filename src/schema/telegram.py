from aiogram.types import Chat, PhotoSize, Video
from pydantic import BaseModel


class TelegramMessage(BaseModel):
    text: str | None = None
    sender_chat: Chat | None = None
    chat: Chat | None = None
    photo: list[PhotoSize] | None = None
    video: Video | None = None
    caption: str | None = None


class TelegramAuthData(BaseModel):
    id: int
    first_name: str = ''
    last_name: str = ''
    username: str
    photo_url: str | None = None
    auth_date: int
    hash: str

    @property
    def data_check_string(self):
        return '\n'.join(
            sorted([f'{k}={v}' for k, v in dict(self).items() if k != 'hash'])
        )
