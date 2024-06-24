from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message, Chat

from core.config import config
from core.logger import logger
from core.messages import MSG
from bot.services.posts import save_to_db, send_to_administrators


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    """
    This handler receives messages with `/start` command
    """
    channel: Chat = await bot.get_chat(config.channel)
    await message.answer(MSG.welcome.format(channel.title or channel.username))


@router.message(F.photo | F.text | F.video)
async def common_message_handler(message: Message, bot: Bot) -> None:
    """
    This handler will forward receive a text message to the Administrators
    """
    try:
        await send_to_administrators(message, bot)
        await message.answer(MSG.post_has_been_sent)

    except (TypeError, TelegramBadRequest) as error:
        logger.error(f'An error has occurred: {repr(error)}')
        await message.answer(MSG.forwarding_error)

    else:
        await save_to_db(message)


@router.message(F.sticker | F.file)
async def unsupported_type_message_handler(message: Message) -> None:
    """
    This handler will send a notification that the message type is unsupported
    """
    await message.answer(MSG.unsupported_type)
