from aiogram.types import ChatPhoto
from pydantic import BaseModel


class ChatInfo(BaseModel):
    title: str | None = None
    photo: ChatPhoto | None = None
