from http import HTTPStatus

import uvicorn
from fastapi import FastAPI

from core.config import config
from core.messages import MSG
from schemes.posts import RequestPost, ResponsePost


app = FastAPI(title=config.title, redoc_url=None)


@app.post(
    '/posts/',
    response_model=ResponsePost,
    status_code=HTTPStatus.CREATED,
    tags=['posts'],
    summary='create post',
    description='Create a new non-moderated post',
    name='v1:posts:post-create',
)
async def create_post(post: RequestPost):
    return {'message': MSG.post_has_been_sent}


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host=config.host, port=config.port, reload=config.debug
    )
