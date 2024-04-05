from aiogram import Router
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from loguru import logger


router = Router()


@router.error(ExceptionTypeFilter(TelegramBadRequest))
async def bad_request_error_handler(event: ErrorEvent) -> None:
    """
    This handler logging TelegramBadRequest error
    """
    logger.error(f'{event.exception}: message={event.update.message}')


@router.error(ExceptionTypeFilter(TelegramForbiddenError))
async def forbidden_error_handler(event: ErrorEvent):
    """
    This handler logging TelegramForbiddenError error
    """
    logger.error(f'{event.exception}: message={event.update.message}')
