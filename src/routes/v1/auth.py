from fastapi import APIRouter, HTTPException, status
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from joserfc import jwt

from core.config import config
from core.logger import logger
from schema.telegram import TelegramAuthData
from services.telegram import check_auth_data


router = APIRouter(prefix='/auth')


@router.get(
    '/telegram-auth',
    response_class=RedirectResponse,
    summary='authorize user',
    description='User authorization using telegram',
    name='v1:auth:telegram-auth',
)
async def telegram_auth(
    request: Request,
    auth_data: TelegramAuthData,
    next: str = '/'
):
    is_correct = check_auth_data(auth_data)

    if not is_correct:
        logger.warning(f'AuthData is incorrect: {auth_data}')
        return HTTPException(
            status_code=status.HTTP_401_Unauthorized,
            detail='Authorization failed. Please try again'
        )

    token = jwt.encode(
        {'alg': 'HS256'},
        {'k': auth_data.id},
        config.jwt_secret_key.get_secret_value
    )
    response = RedirectResponse(next)
    response.set_cookie(key=config.cookie_name, value=token)

    return response


@router.get('/logout')
async def logout():
    response = RedirectResponse('/')
    response.delete_cookie(key=config.cookie_name)
    return response
