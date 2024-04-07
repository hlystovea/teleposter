import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from core.config import config
from routes.v1.posts import router as v1_posts_router


app = FastAPI(title=config.title, redoc_url=None)

app.include_router(v1_posts_router)

templates = Jinja2Templates(directory='./src/templates')


@app.get('/', name='index', response_class=HTMLResponse)
async def index(request: Request):
    context = {'title': config.title}
    return templates.TemplateResponse(request, 'index.html', context)


if __name__ == '__main__':
    uvicorn.run('main:app', host=config.host, reload=config.debug)
