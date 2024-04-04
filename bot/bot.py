import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import config


bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        f'Привет! Ты можешь прислать сюда пост для канала @{config.channel} \
          Жду твоих сообщений! ✍️'
    )


@dp.message(F.photo | F.text)
async def text_and_photo_message_handler(message: Message) -> None:
    """
    This handler will forward receive a text message to the Admin
    """
    try:
        await bot.send_message(
            chat_id=config.admin_id,
            text=f'Сообщение от {message.from_user.full_name}:'
        )
        await message.send_copy(chat_id=config.admin_id)
    except TypeError as error:
        logging.ERROR(f'An error has occurred: {error}')


@dp.message(F.video | F.sticker | F.file)
async def unsupported_type_message_handler(message: Message) -> None:
    """
    This handler will send a notification that the message type is unsupported
    """
    await message.answer(
        'Извини, но данный тип сообщений пока не поддерживается. \
         Используй текст или фото, пожалуйста. 🙏'
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
