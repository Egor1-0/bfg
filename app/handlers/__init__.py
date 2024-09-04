from aiogram import Router

from app.handlers.main_handlers import main_router
from app.handlers.profile import profile_router_
from app.handlers.games import games_router
from app.handlers.base_command.___init__ import base_router_

main_router_ = Router()

main_router_.include_routers(main_router, profile_router_, games_router, base_router_)