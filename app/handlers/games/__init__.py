from aiogram import Router

from app.handlers.games.cube import cubes_router
from app.handlers.games.basketball import basketball_router
from app.handlers.games.darts import darts_router
from app.handlers.games.football import football_router

games_router = Router()

games_router.include_routers(cubes_router, basketball_router, darts_router, football_router)