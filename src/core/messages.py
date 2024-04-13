from typing import NamedTuple


class Messages(NamedTuple):
    welcome: str
    forwarding_error: str
    post_has_been_sent: str
    post_has_been_published: str
    unsupported_type: str


MSG = Messages(
    ('Привет! Ты можешь прислать сюда пост для канала «{}». '
     'Жду твоих сообщений! ✍️'),
    ('При пересылке сообщения произошла ошибка. '
     'Приносим наши извинения. 🙏'),
    'Пост отправлен на модерацию.',
    'Пост опубликован.',
    ('Извини, но данный тип сообщений пока не поддерживается. '
     'Используй текст, фото или видео, пожалуйста. 🙏')
)
