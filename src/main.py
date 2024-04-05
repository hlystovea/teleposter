from http import HTTPStatus

import uvicorn
from fastapi import FastAPI

from core.config import config
from schemes.posts import Post


app = FastAPI(redoc_url=None)


@app.post('/posts/', status_code=HTTPStatus.CREATED)
async def create_post(post: Post):
    return {'message': 'Пост был отправлен на модерацию'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host=config.host, port=config.port, reload=config.debug
    )