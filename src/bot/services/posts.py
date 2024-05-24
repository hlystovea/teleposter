from asyncio import TaskGroup

import httpx
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.types import Message
from httpx import HTTPError
from pydantic import ValidationError

from core.config import config
from core.logger import logger
from schema.telegram import TelegramMessage


async def forward_message(message: Message, chat_id: int | str) -> None:
    try:
        await message.forward(chat_id)

    except (TelegramBadRequest, TelegramForbiddenError) as error:
        logger.error(
            f'An error occurred while forwarding the message: {repr(error)}'
        )


async def send_to_administrators(message: Message, bot: Bot) -> None:
    admins = await bot.get_chat_administrators(config.channel)

    async with TaskGroup() as tg:
        for admin in admins:
            if not admin.user.is_bot:
                tg.create_task(forward_message(message, admin.user.id))
