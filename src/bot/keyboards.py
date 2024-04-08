from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


ADMIN_ENTRANCE_BUTTONS = {
    'moderators': 'Изменить список модераторов',
}


def admin_entrance_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for action, text in ADMIN_ENTRANCE_BUTTONS.items():
        builder.button(text=text, callback_data=f'admin:{action}')

    return builder.as_markup()
