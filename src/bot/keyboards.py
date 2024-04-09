from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from bot.callbacks import (AdminEntranceCallback, AdminModeratorsCallback,
                           EntranceAction, ModeratorsAction)


def admin_entrance_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for action in EntranceAction:
        builder.button(
            text=action.value.title(),
            callback_data=AdminEntranceCallback(action=action)
        )

    return builder.as_markup()


def admin_moderators_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for action in ModeratorsAction:
        builder.button(
            text=action.value.title(),
            callback_data=AdminModeratorsCallback(action=action)
        )
    
    builder.adjust(2, 1)

    return builder.as_markup()
