from aiogram import Router

from app.handlers.main_handlers import main_router

main_router_ = Router()

main_router_.include_routers(main_router)