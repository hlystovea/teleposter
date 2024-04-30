import hashlib
import hmac

from httpx import AsyncClient, HTTPError
from async_lru import alru_cache

from core.config import config
from schema.posts import Post
from schema.telegram import TelegramAuthData


def get_api_url(method: str, token=config.bot_token) -> str:
    return f'https://api.telegram.org/bot{token.get_secret_value()}/{method}'


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


@alru_cache(maxsize=32)
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
