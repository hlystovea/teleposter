from aiogram import Router, F
from aiogram.types import Message

from core.config import config
from bot.keyboards import admin_entrance_keyboard


router = Router()


@router.message((F.from_user.id == config.admin_id) & (F.text == '/admin'))
async def admin_command_handler(message: Message) -> None:
    """
    This handler will send the admin keyboard
    """
    await message.answer('ADMIN', reply_markup=admin_entrance_keyboard())
