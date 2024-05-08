import aiofiles
import random
import string
from typing import AsyncGenerator

from fastapi import UploadFile, HTTPException

from core.config import config
from core.logger import logger
from schema.posts import Post
from services.telegram import get_file, stream_file


def generate_random_string(length: int = 16):
    all_symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(all_symbols) for _ in range(length))


async def save_file(file: UploadFile) -> str:
    media_dir = config.media_root
    file_name = f'{generate_random_string()}.{file.filename.split(".")[-1]}'

    try:
        async with aiofiles.open(media_dir / file_name, 'wb') as out_file:
            while content := await file.read(64 * 1000):
                await out_file.write(content)

        return file_name

    except OSError as error:
        logger.error(f'An error occured: {error}')
        raise HTTPException(status_code=500, detail='Internal server error')


async def save_media(post: Post) -> Post:
    media_dir = config.media_root

    if post.photo:
        file = await get_file(post.photo[-1].file_id)
        file_name = f'{generate_random_string()}.jpg'

        try:
            async with aiofiles.open(media_dir / file_name, 'wb') as out_file:
                streaming_file = stream_file(file.file_path)
                async for chunk in streaming_file:
                    await out_file.write(chunk)

            post.files.append(file_name)

        except OSError as error:
            logger.error(f'An error occured: {error}')
            raise HTTPException(status_code=500, detail='Internal server error')
    
    if post.video:
        file = await get_file(post.video.file_id)
        file_name = f'{generate_random_string()}.mp4'

        try:
            async with aiofiles.open(media_dir / file_name, 'wb') as out_file:
                streaming_file = stream_file(file.file_path)
                async for chunk in streaming_file:
                    await out_file.write(chunk)

            post.files.append(file_name)

        except OSError as error:
            logger.error(f'An error occured: {error}')
            raise HTTPException(status_code=500, detail='Internal server error')

    return post
