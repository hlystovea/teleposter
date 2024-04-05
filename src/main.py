from http import HTTPStatus

from fastapi import FastAPI

from src.schemes.posts import Post


app = FastAPI(redoc_url=None)


@app.post('/posts/', status_code=HTTPStatus.CREATED)
async def create_post(post: Post):
    return {'message': 'Пост был отправлен на модерацию'}
