from aiogram import Bot, F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.callbacks import (AdminEntranceCallback, AdminModeratorsCallback,
                           EntranceAction, ModeratorsAction)
from bot.keyboards import admin_entrance_keyboard, admin_moderators_keyboard
from core.config import config


router = Router()


class NewModeratorForm(StatesGroup):
    username = State()


@router.message(F.text == '/admin')
async def admin_command_handler(message: Message) -> None:
    """
    This handler sends the admin keyboard
    """
    if message.from_user.id == config.admin_id:
        await message.answer(
            'Выберите команду:',
            reply_markup=admin_entrance_keyboard()
        )


@router.callback_query(
    AdminEntranceCallback.filter(F.action == EntranceAction.moderators)
)
async def moderators_action_handler(
    query: CallbackQuery, callback_data: AdminEntranceCallback, bot: Bot
) -> None:
    """
    This handler sends the moderators keyboard
    """
    await query.message.edit_text(
        'Выберите действие для изменения списка модераторов:',
        reply_markup=admin_moderators_keyboard()
    )


@router.callback_query(
    AdminModeratorsCallback.filter(F.action == ModeratorsAction.add)
)
async def add_moderator_handler(
    query: CallbackQuery, callback_data: AdminModeratorsCallback, state: FSMContext) -> None:
    """
    This handler requests the username to be added to the list of moderators
    """
    await state.set_state(NewModeratorForm.username)
    await query.message.edit_text(
        'Введите **username** пользователя, которого хотите добавить '\
        'в список модераторов канала:'
    )


@router.message(NewModeratorForm.username)
async def save_new_moderator(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await message.answer(
        f'Добавить пользователя @{message.text} в список модераторов?',
    )


@router.callback_query(
    AdminModeratorsCallback.filter(F.action == ModeratorsAction.delete)
)
async def delete_moderator_handler(
    query: CallbackQuery, callback_data: AdminModeratorsCallback, bot: Bot
) -> None:
    """
    This handler sends a list of moderators to be deleted
    """
    await query.message.edit_text(
        'Выберите пользователя для удаления из списка модераторов:'
    )
