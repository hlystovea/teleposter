import urllib.parse

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from joserfc import jwt
from joserfc.errors import JoseError

from core.config import config
from routes.v1.auth import router as v1_auth_router
from routes.v1.posts import router as v1_posts_router


app = FastAPI(title=config.title, redoc_url=None)

app.include_router(v1_auth_router)
app.include_router(v1_posts_router)

templates = Jinja2Templates(directory='./src/templates')


@app.middleware('http')
async def middleware(request: Request, call_next):
    response = await call_next(request)
    if request.url.path.startswith('/auth/'):
        return response

    url_safe_path = urllib.parse.quote(request.url.path, safe='')
    template_context = {'request': request, 'next_path': url_safe_path}
    login_wall = templates.TemplateResponse('login.html', template_context)

    token = request.cookies.get(config.cookie_name)
    if not token:
        return login_wall

    try:
        token_parts = jwt.decode(token, config.jwt_secret_key.get_secret_value)
    except JoseError:
        return login_wall

    user_id = token_parts.claims['k']
    if user_id not in [490603652]:
        return login_wall

    return response


@app.get('/', name='index', response_class=HTMLResponse)
async def index(request: Request):
    context = {'title': config.title}
    return templates.TemplateResponse(request, 'index.html', context)


if __name__ == '__main__':
    uvicorn.run('main:app', host=config.host, reload=config.debug)
