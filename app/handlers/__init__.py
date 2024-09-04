from aiogram import Router

from app.handlers.main_handlers import main_router
from app.handlers.profile import profile_router_
from app.handlers.games import games_router
from app.handlers.gifts import base_router

main_router_ = Router()

main_router_.include_routers(main_router, profile_router_, base_router, games_router)