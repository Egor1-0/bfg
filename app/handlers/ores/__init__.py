from aiogram import Router

from app.handlers.ores.ores_handlers import ores_router
from app.handlers.ores.ores_handlers_error import ores_error

ores_router_ = Router()

ores_router_.include_routers(ores_router, ores_error)
