import httpx
from aiogram.types import Message
from httpx import HTTPError
from pydantic import ValidationError

from core.config import config
from core.logger import logger
from main import app
from schemes.posts import TelegramPost


async def send_for_moderation(message: Message) -> None:
    try:
        post = TelegramPost.model_validate(message)
        url = config.api_url + app.url_path_for('v1:posts:post-create')
        response = httpx.post(url, json=dict(post))
        await message.answer(response.json()['message'])
    except (TypeError, ValidationError, HTTPError) as error:
        await message.answer('Упс.. Что-то пошло не так')
        await message.send_copy(message.chat.id)
        logger.error(f'An error has occurred: {repr(error)}')
