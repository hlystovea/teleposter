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


class TelegramAuthData(BaseModel):
    id: int
    first_name: str = ''
    last_name: str = ''
    username: str
    photo_url: str | None = None
    auth_date: str
    hash: str

    @property
    def data_check_string(self):
        return (f'auth_date={self.auth_date}\n'
                f'first_name={self.first_name}\n'
                f'id={self.id}\n'
                f'username={self.username}')
