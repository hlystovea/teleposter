import hashlib
import hmac
from typing import Any, AsyncGenerator

from fastapi import HTTPException
from httpx import AsyncClient, HTTPError

from core.config import config
from schema.posts import Post
from schema.telegram import TelegramMedia, TelegramAuthData


def get_api_url(method: str) -> str:
    bot_token = config.bot_token.get_secret_value()
    return f'https://api.telegram.org/bot{bot_token}/{method}'


async def publish_in_channel(post: Post) -> None:
    headers = {'Content-Type': 'application/json'}
    data = {'chat_id': config.channel}

    if post.photo:
        url = get_api_url('sendPhoto')
        data |= {'photo': post.photo[0].file_id, 'caption': post.caption}
    elif post.video:
        url = get_api_url('sendVideo')
        data |= {'video': post.video.file_id, 'caption': post.caption}
    else:
        url = get_api_url('sendMessage')
        data |= {'text': post.text}

    async with AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        data = response.json()

    if not data['ok']:
        raise HTTPError(f'Response: {data}')


def check_auth_data(auth_data: TelegramAuthData) -> bool:
    secret_key = hashlib.sha256(config.bot_token.get_secret_value().encode())
    auth_data_hash = hmac.new(
        secret_key.digest(),
        auth_data.data_check_string.encode(),
        'sha256'
    ).hexdigest()
    return hmac.compare_digest(auth_data_hash, auth_data.hash)


async def get_admin_ids() -> list[int]:
    headers = {'Content-Type': 'application/json'}
    data = {'chat_id': config.channel}
    url = get_api_url('getChatAdministrators')

    async with AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        data = response.json()

    if not data['ok']:
        raise HTTPError(f'Response: {data}')

    return [member['user']['id'] for member in data['result']]


async def get_file(file_id: str) -> TelegramMedia:
    headers = {'Content-Type': 'application/json'}
    data = {'file_id': file_id}
    url = get_api_url('getFile')

    async with AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        data = response.json()

    if not data['ok']:
        raise HTTPException(
            status_code=data['error_code'],
            detail=data['description']
        )

    return TelegramMedia(**data['result'])


async def stream_file(
    file_path: str, chunk_size: int | None = None
) -> AsyncGenerator[bytes, Any]:
    bot_token = config.bot_token.get_secret_value()
    url = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'

    async with AsyncClient() as client:
        async with client.stream('GET', url) as response:
            async for chunk in response.aiter_bytes(chunk_size):
                yield chunk
