from typing import NamedTuple


class Messages(NamedTuple):
    welcome: str
    forwarding_error: str
    post_has_been_sent: str
    post_has_been_deleted: str
    unsupported_type: str


MSG = Messages(
    ('Привет! Ты можешь прислать сюда пост для канала «{}». '
     'Жду твоих сообщений! ✍️'),
    ('При пересылке сообщения произошла ошибка. '
     'Приносим наши извинения. 🙏'),
    'Пост был отправлен на модерацию.',
    'Пост был удален.',
    ('Извини, но данный тип сообщений пока не поддерживается. '
     'Используй текст или фото, пожалуйста. 🙏')
)
