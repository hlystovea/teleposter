from typing import NamedTuple


class Messages(NamedTuple):
    welcome: str
    oops_error: str
    post_has_been_sent: str
    unsupported_type: str


MSG = Messages(
    ('Привет! Ты можешь прислать сюда пост для канала @{}. '
     'Жду твоих сообщений! ✍️'),
    'Упс.. Что-то пошло не так.',
    'Пост был отправлен на модерацию.',
    ('Извини, но данный тип сообщений пока не поддерживается. '
     'Используй текст или фото, пожалуйста. 🙏')
)
