import asyncio

import httpx
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from httpx import HTTPError
from pydantic import ValidationError

from core.config import config
from core.logger import logger
from main import app
from schemes.telegram import TelegramMessage


async def forward_message(message: Message, chat_id: int | str) -> None:
    try:
        await message.forward(chat_id)
    except TelegramBadRequest as error:
        logger.error(f'An error has occurred: {repr(error)}')


async def send_to_administrators(message: Message, bot: Bot) -> None:
    try:
        admins = await bot.get_chat_administrators(f'@{config.channel}')

        async with asyncio.TaskGroup() as tg:
            for admin in admins:
                if not admin.user.is_bot:
                    tg.create_task(forward_message(message, admin.user.id))

    except (TelegramBadRequest, TypeError) as error:
        logger.error(f'An error has occurred: {repr(error)}')


async def send_for_moderation(message: Message, bot: Bot) -> None:
    try:
        url = config.api_url + app.url_path_for('v1:posts:post-create')
        post = TelegramMessage.model_validate(message, from_attributes=True)

        response = httpx.post(url, json=post.model_dump(exclude={'create_at'}))
        response.raise_for_status()

        await message.answer(response.json()['message'])

    except (TypeError, ValidationError, HTTPError) as error:
        await message.answer('Упс.. Что-то пошло не так')
        await message.send_copy(message.chat.id)

        logger.error(f'An error has occurred: {repr(error)}')
    
    finally:
        await send_to_administrators(message, bot)
