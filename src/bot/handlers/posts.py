from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message

from core.config import config
from core.logger import logger
from core.messages import MSG
from bot.services.posts import save_to_db, send_to_administrators


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(MSG.welcome.format(config.channel))


@router.message(F.photo | F.text)
async def text_and_photo_message_handler(message: Message, bot: Bot) -> None:
    """
    This handler will forward receive a text message to the Administrators
    """
    try:
        await send_to_administrators(message, bot)
        await message.answer(MSG.post_has_been_sent)

    except (TypeError, TelegramBadRequest) as error:
        logger.error(f'An error has occurred: {repr(error)}')
        await message.answer(
            'При пересылке сообщения произошла ошибка. '
            'Приносим наши извинения.'
        )
    
    else:
        await save_to_db(message)


@router.message(F.video | F.sticker | F.file)
async def unsupported_type_message_handler(message: Message) -> None:
    """
    This handler will send a notification that the message type is unsupported
    """
    await message.answer(MSG.unsupported_type)
