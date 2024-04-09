
from enum import Enum

from aiogram.filters.callback_data import CallbackData


class EntranceAction(str, Enum):
    moderators = 'Изменить список модераторов'


class AdminEntranceCallback(CallbackData, prefix='admin'):
    action: EntranceAction


class ModeratorsAction(str, Enum):
    add = 'Добавить'
    delete = 'Удалить'
    back = 'Назад'


class AdminModeratorsCallback(CallbackData, prefix='moderators'):
    action: ModeratorsAction
