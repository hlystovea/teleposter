from fastapi import Depends, HTTPException, status
from joserfc import jwt
from joserfc.errors import JoseError

from core.config import config
from schema.auth import oauth2_scheme
from services.telegram import get_admin_ids


async def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        token_parts = jwt.decode(
            token, config.jwt_secret_key.get_secret_value()
        )
    except JoseError:
        raise credentials_exception

    user_id = token_parts.claims['k']
    admin_ids = await get_admin_ids()

    if user_id not in admin_ids:
        raise credentials_exception

    return user_id
