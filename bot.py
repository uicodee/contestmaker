import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from tgbot.config import load_config
from tgbot.filters.role import RoleFilter, AdminFilter
from tgbot.handlers.buttons import register_buttons
from tgbot.handlers.commands import register_admin
from tgbot.handlers.commands import register_user
from tgbot.handlers.content import register_content
from tgbot.handlers.query_handlers import register_query_handler
from tgbot.middlewares.db import DbSessionMiddleware
from tgbot.middlewares.role import RoleMiddleware
from tgbot.middlewares.subscription import Subscription
from tgbot.misc.req_func import make_connection_string

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    config = load_config("bot.ini")
    engine = create_async_engine(
        make_connection_string(config.db), future=True, echo=False
    )


    session_fabric = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    if config.tg_bot.use_redis:
        storage = RedisStorage()
    else:
        storage = MemoryStorage()

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)
    bot["config"] = config
    dp.middleware.setup(DbSessionMiddleware(session_fabric))
    dp.middleware.setup(RoleMiddleware(config.tg_bot.admin_id))
    dp.middleware.setup(Subscription())
    dp.filters_factory.bind(RoleFilter)
    dp.filters_factory.bind(AdminFilter)

    register_user(dp)
    register_admin(dp)
    register_buttons(dp)
    register_query_handler(dp)
    register_content(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
