from aiogram import Router

from app.handlers.base_command.base_command import base_router

base_router_ = Router()

base_router_.include_routers(base_router)
