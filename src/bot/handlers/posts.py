from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from core.config import config
from core.messages import MSG
from bot.services.posts import send_for_moderation


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(MSG.welcome.format(config.channel))


@router.message(F.photo | F.text)
async def text_and_photo_message_handler(message: Message) -> None:
    """
    This handler will forward receive a text message to the Admin
    """
    await send_for_moderation(message)


@router.message(F.video | F.sticker | F.file)
async def unsupported_type_message_handler(message: Message) -> None:
    """
    This handler will send a notification that the message type is unsupported
    """
    await message.answer(MSG.unsupported_type)
