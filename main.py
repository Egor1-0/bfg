import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.database.session import create_session
from app.handlers import main_router_
from app.handlers.profile import profile_router_

load_dotenv()

async def main():
    await create_session()
    bot = Bot(token=os.getenv("TOKEN")) 
    dp = Dispatcher()

    dp.include_routers(main_router_, profile_router_)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass