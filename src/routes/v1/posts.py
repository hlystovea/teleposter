from bson import ObjectId

from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.results import DeleteResult, UpdateResult

from core.messages import MSG
from db.mongo import posts
from schema.posts import Post, ResponsePost, ResponseMessage


router = APIRouter(prefix='/api/v1/posts', tags=['posts'])


@router.get(
    '/',
    response_model=list[ResponsePost],
    summary='get posts',
    description='Responds with a list of posts',
    name='v1:posts:post-list',
)
async def get_posts(posts=Depends(posts)):
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
    summary='create post',
    description='Creates a new non-moderated post',
    name='v1:posts:post-create',
)
async def create_post(post: Post, posts=Depends(posts)):
    _ = await posts.insert_one(post.model_dump())
    return {'message': MSG.post_has_been_sent}


@router.delete(
    '/{post_id}',
    response_model=ResponseMessage,
    summary='delete post',
    description='Deletes the post',
    name='v1:posts:post-delete',
)
async def delete_post(post_id: str, posts=Depends(posts)):
    result: DeleteResult = await posts.delete_one({'_id': ObjectId(post_id)})

    if not result.deleted_count:
        raise HTTPException(status_code=404, detail='Post not found')

    return {'message': MSG.post_has_been_deleted}


@router.put(
    '/{post_id}',
    response_model=ResponseMessage,
    summary='update post',
    description='Updates the post',
    name='v1:posts:post-update',
)
async def update_post(post_id: str, post: Post, posts=Depends(posts)):
    result: UpdateResult = await posts.update_one(
        filter={'_id': ObjectId(post_id)},
        update=post.model_dump(exclude={'id'})
    )

    if not result.matched_count or not result.modified_count:
        raise HTTPException(status_code=404, detail='Post not found')

    return {'message': MSG.post_has_been_updated}


@router.post(
    '/{post_id}/publish',
    response_model=ResponseMessage,
    summary='publish post',
    description='Publishes the post in a telegram channel',
    name='v1:posts:post-publish',
)
async def publish_post(post_id: str, posts=Depends(posts)):
    post = posts.find_one(filter={'_id': ObjectId(post_id)})

    if not post:
        raise HTTPException(status_code=404, detail='Post not found')

    return {'message': MSG.post_has_been_published}
