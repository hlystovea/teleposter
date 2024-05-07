import aiofiles
import random
import string

from fastapi import UploadFile

from core.config import config
from core.logger import logger


def generate_random_string(length: int = 16):
    all_symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(all_symbols) for _ in range(length))


async def save_file(file: UploadFile):
    media_dir = config.media_root
    file_name = f'{generate_random_string()}.{file.filename.split(".")[-1]}'

    try:
        async with aiofiles.open(media_dir / file_name, 'wb') as out_file:
            while content := await file.read(64 * 1000):
                await out_file.write(content)

    except OSError as error:
        logger.error(f'An error occured: {error}')
