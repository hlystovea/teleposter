from motor.motor_asyncio import AsyncIOMotorClient

from core.config import config


def posts():
    client = AsyncIOMotorClient(config.mongo_url)
    coll = client.teleposter.posts
    yield coll
