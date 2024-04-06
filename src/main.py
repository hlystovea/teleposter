import uvicorn
from fastapi import FastAPI

from core.config import config
from routes.v1.posts import router as v1_posts_router


app = FastAPI(title=config.title, redoc_url=None)

app.include_router(v1_posts_router)


@app.get("/")
async def index():
    return {'message': 'Home page'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host=config.host, port=config.api_port, reload=config.debug
    )
