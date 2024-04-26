import hmac
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse, RedirectResponse
from joserfc import jwt

from core.config import config

router = APIRouter(prefix='/auth')


@router.get('/telegram-callback')
async def telegram_callback(
        request: Request,
        user_id: Annotated[int, Query(alias='id')],
        query_hash: Annotated[str, Query(alias='hash')],
        next_url: Annotated[str, Query(alias='next')] = '/',
):
    params = request.query_params.items()
    data_check_string = '\n'.join(sorted(f'{x}={y}' for x, y in params if x not in ('hash', 'next')))
    computed_hash = hmac.new(config.bot_token.get_secret_value.digest(), data_check_string.encode(), 'sha256').hexdigest()
    is_correct = hmac.compare_digest(computed_hash, query_hash)
    if not is_correct:
        return PlainTextResponse('Authorization failed. Please try again', status_code=401)

    token = jwt.encode({'alg': 'HS256'}, {'k': user_id}, config.jwt_secret_key.get_secret_value)
    response = RedirectResponse(next_url)
    response.set_cookie(key=config.cookie_name, value=token)
    return response


@router.get('/logout')
async def logout():
    response = RedirectResponse('/')
    response.delete_cookie(key=config.cookie_name)
    return response
