from asyncio import TaskGroup
from asyncio.exceptions import CancelledError, InvalidStateError

import httpx
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from httpx import HTTPError
from pydantic import ValidationError

from core.config import config
from core.logger import logger
from main import app
from schema.telegram import TelegramMessage


async def forward_message(message: Message, chat_id: int | str) -> None:
    try:
        await message.forward(chat_id)

    except TelegramBadRequest as error:
        logger.error(
            f'An error occurred while forwarding the message: {repr(error)}'
        )


async def send_to_administrators(message: Message, bot: Bot) -> None:
    admins = await bot.get_chat_administrators(config.channel)

    async with TaskGroup() as tg:
        for admin in admins:
            if not admin.user.is_bot:
                tg.create_task(forward_message(message, admin.user.id))


async def save_to_db(message: Message) -> None:
    try:
        url = f'{config.api_url}{app.url_path_for("v1:posts:post-create")}'
        post = TelegramMessage.model_validate(message, from_attributes=True)
        data = post.model_dump(exclude={'create_at'})

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)
            response.raise_for_status()

    except (TypeError, KeyError, ValidationError, HTTPError) as error:
        logger.error(
            f'An error occurred while saving the message: {repr(error)}'
        )
