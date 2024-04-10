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
from core.messages import MSG
from main import app
from schema.telegram import TelegramMessage


async def forward_message(message: Message, chat_id: int | str) -> None:
    try:
        await message.forward(chat_id)

    except TelegramBadRequest as error:
        logger.error(f'An error has occurred: {repr(error)}')


async def send_to_administrators(message: Message, bot: Bot) -> None:
    try:
        admins = await bot.get_chat_administrators(f'@{config.channel}')

        async with TaskGroup() as tg:
            for admin in admins:
                if not admin.user.is_bot:
                    tg.create_task(forward_message(message, admin.user.id))

    except (TelegramBadRequest, TypeError) as error:
        logger.error(f'An error has occurred: {repr(error)}')


async def save_to_db(message: Message) -> None:
    try:
        url = config.api_url + app.url_path_for('v1:posts:post-create')
        post = TelegramMessage.model_validate(message, from_attributes=True)

        response = httpx.post(url, json=post.model_dump(exclude={'create_at'}))
        response.raise_for_status()

    except (TypeError, KeyError, ValidationError, HTTPError) as error:
        logger.error(f'An error has occurred: {repr(error)}')


async def send_for_moderation(message: Message, bot: Bot) -> None:
    try:
        async with TaskGroup() as tg:
            tg.create_task(save_to_db(message))
            tg.create_task(send_to_administrators(message, bot))

        await message.answer(MSG.post_has_been_sent)

    except (TypeError, CancelledError, InvalidStateError) as error:
        logger.error(f'An error has occurred: {repr(error)}')
        await message.answer(MSG.oops_error)
