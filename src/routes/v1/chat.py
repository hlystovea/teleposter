from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Chat
from fastapi import APIRouter, HTTPException, status
from services.telegram import get_chat_info

from core.logger import logger
from schema.chat import ChatInfo


router = APIRouter(prefix='/api/v1/chat', tags=['chat'])


@router.get(
    '/info',
    response_model=ChatInfo,
    summary='get a chat info',
    description='Responds a chat info',
    name='v1:chat:chat-info',
)
async def get_info():
    try:
        chat_info = await get_chat_info()

    except TelegramBadRequest as error:
        logger.error(
            f'An error occurred while geting chat info: {repr(error)}'
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An error occurred'
        )

    return chat_info
