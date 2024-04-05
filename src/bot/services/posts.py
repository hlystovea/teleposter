import httpx
from aiogram.types import Message

from core.logger import logger


async def send_for_moderation(message: Message) -> None:
    try:
        r = httpx.post(
            'http://backend:8000/posts/',
            json={
                'user_id': message.chat.id,
                'text': message.text,
            }
        )
        await message.answer(r.json()['message'])
    except TypeError as error:
        logger.error(f'An error has occurred: {error}')
