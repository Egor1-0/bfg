import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


from aiogram_dialog import setup_dialogs


from app.database.queries import push_ore, push_car
from app.database.session import create_session
from app.handlers import main_router_
from app.handlers.shop.buy.buy import buy_router
from app.middlewares import CheckUser
from app.dialog import dialog_router
    

load_dotenv()


async def main():
    """
    Главная функция - точка входа бота.
    Здесь происходит инициализация сессии,
    отправка запросов на создание руд,
    создание бота,
    привязка роутера,
    привязка middleware,
    удаление вебхука,
    запуск поллинга.
    """
    await create_session()
    await push_ore()
    await push_car()
    bot = Bot(token=os.getenv("TOKEN")) 
    dp = Dispatcher()

    dp.include_routers(main_router_, dialog_router)
    dp.message.outer_middleware(CheckUser())
    
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


