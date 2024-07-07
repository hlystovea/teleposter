from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from joserfc import jwt

from core.config import config
from core.logger import logger
from schema.auth import Token
from schema.telegram import TelegramAuthData
from services.telegram import check_auth_data


router = APIRouter(prefix='/api/v1/auth')


@router.post(
    '/telegram-auth',
    response_model=Token,
    summary='authorize user',
    description='User authorization using telegram',
    name='v1:auth:telegram-auth',
)
async def telegram_auth(auth_data: TelegramAuthData):
    is_correct = check_auth_data(auth_data)

    if not is_correct:
        logger.warning(f'Invalid authorization data: {auth_data}')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Authorization failed. Please try again'
        )

    token = jwt.encode(
        {'alg': 'HS256'},
        {'k': auth_data.id},
        config.jwt_secret_key.get_secret_value()
    )
    response = JSONResponse({'token': token})
    response.set_cookie(key=config.cookie_name, value=token)

    return response
