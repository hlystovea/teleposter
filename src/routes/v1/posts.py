from bson import ObjectId

from fastapi import APIRouter, Depends, HTTPException, status

from core.messages import MSG
from db.mongo import posts_collection
from schemes.posts import ResponsePost, ResponseMessage
from schemes.telegram import TelegramMessage


router = APIRouter(prefix='/api/v1/posts', tags=['posts'])


@router.get(
    '/',
    response_model=list[ResponsePost],
    tags=['posts'],
    summary='get posts',
    description='Responds with a list of posts',
    name='v1:posts:post-list',
)
async def get_posts(posts=Depends(posts_collection)):
    return await posts.find().sort(
        [
            ('status', 1),
            ('created_at', -1)
        ]
    ).to_list(1000)


@router.post(
    '/',
    response_model=ResponseMessage,
    status_code=status.HTTP_201_CREATED,
    tags=['posts'],
    summary='create post',
    description='Creates a new non-moderated post',
    name='v1:posts:post-create',
)
async def create_post(post: TelegramMessage, posts=Depends(posts_collection)):
    _ = await posts.insert_one(post.model_dump())
    return {'message': MSG.post_has_been_sent}


@router.delete(
    '/{post_id}',
    response_model=ResponseMessage,
    tags=['posts'],
    summary='delete post',
    description='Deletes the post',
    name='v1:posts:post-delete',
)
async def delete_post(post_id: str, posts=Depends(posts_collection)):
    result = await posts.delete_one({'_id': ObjectId(post_id)})

    if not result.deleted_count:
        raise HTTPException(status_code=404, detail='Post not found')

    return {'message': MSG.post_has_been_deleted}
