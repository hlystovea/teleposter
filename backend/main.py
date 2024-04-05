from fastapi import FastAPI, Request


app = FastAPI(redoc_url=None, docs_url=None)


@app.get('/')
async def index(request: Request):
    return {'Hello': 'world'}
