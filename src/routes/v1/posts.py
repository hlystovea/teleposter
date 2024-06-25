from bson import ObjectId

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import ValidationError
from pymongo.errors import InvalidOperation
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from core.logger import logger
from core.messages import MSG
from db.mongo import posts
from httpx import HTTPError
from schema.posts import (Post, PostStatus, RequestPost,
                          ResponsePost, ResponseMessage)
from services.telegram import publish_in_channel
from services.files import save_media


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


@router.get(
    '/{post_id}',
    response_model=ResponsePost,
    summary='get a post',
    description='Responds a post',
    name='v1:posts:post-retrieve',
)
async def get_post(post_id: str, posts=Depends(posts)):
    post = await posts.find_one({'_id': ObjectId(post_id)})

    if not post:
        raise HTTPException(status_code=404, detail='The post was not found')

    return post


@router.post(
    '/',
    response_model=ResponsePost,
    status_code=status.HTTP_201_CREATED,
    summary='create post',
    description='Creates a new non-moderated post',
    name='v1:posts:post-create',
)
async def create_post(post: Post, posts=Depends(posts)):
    post = await save_media(post)

    try:
        result: InsertOneResult = await posts.insert_one(post.model_dump())

    except InvalidOperation as error:
        logger.error(f'An error occurred while saving the post: {repr(error)}')
        raise HTTPException(status_code=500, detail='A post was not created')

    return {'_id': result.inserted_id}


@router.delete(
    '/{post_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='delete post',
    description='Deletes a post',
    name='v1:posts:post-delete',
)
async def delete_post(post_id: str, posts=Depends(posts)) -> None:
    result: DeleteResult = await posts.delete_one({'_id': ObjectId(post_id)})

    if not result.deleted_count:
        raise HTTPException(status_code=404, detail='The post was not found')

    return None


@router.patch(
    '/{post_id}',
    response_model=ResponsePost,
    summary='update post',
    description='Updates a post',
    name='v1:posts:post-update',
)
async def update_post(post_id: str, post: RequestPost, posts=Depends(posts)):
    validated_data = post.model_dump(exclude_unset=True)
    validated_data['status'] = PostStatus.MODERATED

    try:
        result: UpdateResult = await posts.update_one(
            filter={'_id': ObjectId(post_id)},
            update={'$set': validated_data}
        )

    except InvalidOperation as error:
        logger.error(
            f'An error occurred while updating the post: {repr(error)}'
        )
        raise HTTPException(
            status_code=500, detail='The post was not updated'
        )

    if not result.matched_count:
        raise HTTPException(status_code=404, detail='The post was not found')

    return await posts.find_one({'_id': ObjectId(post_id)})


@router.post(
    '/{post_id}/publish',
    response_model=ResponseMessage,
    status_code=status.HTTP_200_OK,
    summary='publish post',
    description='Publishes a post in a telegram channel',
    name='v1:posts:post-publish',
)
async def publish_post(post_id: str, posts=Depends(posts)):
    post = await posts.find_one(filter={'_id': ObjectId(post_id)})

    if not post:
        raise HTTPException(status_code=404, detail='The post was not found')

    try:
        await publish_in_channel(Post(**post))
        await posts.update_one(
            filter={'_id': ObjectId(post_id)},
            update={'$set': {'status': PostStatus.PUBLISHED}}
        )

    except HTTPError as error:
        logger.error(
            f'An error occurred while publishing the post: {repr(error)}'
        )
        raise HTTPException(status_code=503, detail='Service unavailable')

    except ValidationError as error:
        logger.error(
            f'An error occurred while validating the post: {repr(error)}'
        )
        raise HTTPException(status_code=500, detail='Internal server error')

    except InvalidOperation as error:
        logger.error(
            f'An error occurred while updating the status: {repr(error)}'
        )

    return {'message': MSG.post_has_been_published}
