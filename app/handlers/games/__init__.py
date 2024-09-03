from aiogram import Router

from app.handlers.games.cube import cubes_router

games_router = Router()

games_router.include_routers(cubes_router)