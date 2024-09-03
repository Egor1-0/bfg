from aiogram import Router

from app.handlers.profile.profile import profile_router

profile_router_ = Router()

profile_router_.include_routers(profile_router)
