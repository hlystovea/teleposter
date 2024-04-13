from httpx import AsyncClient, HTTPError

from core.config import config
from schema.posts import Post


def get_api_url(method: str, token=config.bot_token) -> str:
    return f'https://api.telegram.org/bot{token.get_secret_value()}/{method}'


async def publish_in_channel(post: Post) -> None:
    url = get_api_url('sendMessage')

    headers = {'Content-Type': 'application/json'}

    data = {
        'chat_id': config.channel,
        'text': post.text,
    }

    async with AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        data = response.json()

    if not data['ok']:
        raise HTTPError(f'Response: {data}')
