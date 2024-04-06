from fastapi import (APIRouter, Depends, status)

from core.messages import MSG
from db.mongo import posts_collection
from schemes.posts import PostCreatedResponse
from schemes.telegram import TelegramMessage


router = APIRouter(prefix='/api/v1/posts', tags=['posts'])


@router.post(
    '/',
    response_model=PostCreatedResponse,
    status_code=status.HTTP_201_CREATED,
    tags=['posts'],
    summary='create post',
    description='Create a new non-moderated post',
    name='v1:posts:post-create',
)
async def create_post(post: TelegramMessage, posts=Depends(posts_collection)):
    _ = await posts.insert_one(post.model_dump())
    return {'message': MSG.post_has_been_sent}
