import hashlib
import hmac
from pathlib import Path
from typing import Any, AsyncGenerator

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile, File
from aiogram.utils.media_group import MediaGroupBuilder, MediaType
from httpx import AsyncClient

from core.config import config
from schema.posts import Post
from schema.telegram import TelegramAuthData


bot = Bot(
    token=config.bot_token.get_secret_value(),
    parse_mode=ParseMode.MARKDOWN_V2
)


async def publish_in_channel(post: Post) -> None:
    chat_id = config.channel

    if post.files:
        await bot.send_media_group(chat_id, await create_album(post))
        return

    await bot.send_message(chat_id, post.text or '')


def check_auth_data(auth_data: TelegramAuthData) -> bool:
    secret_key = hashlib.sha256(config.bot_token.get_secret_value().encode())
    auth_data_hash = hmac.new(
        secret_key.digest(),
        auth_data.data_check_string.encode(),
        'sha256'
    ).hexdigest()
    return hmac.compare_digest(auth_data_hash, auth_data.hash)


async def get_file(file_id: str) -> File:
    return await bot.get_file(file_id)


async def stream_file(
    file_path: str, chunk_size: int | None = None
) -> AsyncGenerator[bytes, Any]:
    bot_token = config.bot_token.get_secret_value()
    url = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'

    async with AsyncClient() as client:
        async with client.stream('GET', url) as response:
            async for chunk in response.aiter_bytes(chunk_size):
                yield chunk


async def download_file(file_path: str, destination: str | Path) -> None:
    await bot.download_file(file_path, destination)


async def create_album(post: Post) -> list[MediaType]:
    album_builder = MediaGroupBuilder(caption=post.text)

    for file in post.files:
        album_builder.add_photo(media=FSInputFile(config.media_root / file))

    return album_builder.build()
