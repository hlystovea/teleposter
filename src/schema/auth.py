from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class Token(BaseModel):
    token: str
