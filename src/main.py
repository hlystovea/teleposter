import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import config
from routes.v1.auth import router as v1_auth_router
from routes.v1.files import router as v1_files_router
from routes.v1.posts import router as v1_posts_router


origins = [
    'http://localhost',
    'http://localhost:3000',
]

app = FastAPI(title=config.title, redoc_url=None)

app.include_router(v1_auth_router)
app.include_router(v1_files_router)
app.include_router(v1_posts_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run('main:app', host=config.host, reload=config.debug)
