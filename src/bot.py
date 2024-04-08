import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from core.config import config
from bot.handlers import admin, errors, posts


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(admin.router)
    dp.include_router(posts.router)
    dp.include_router(errors.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info('Start bot')
    asyncio.run(main())
