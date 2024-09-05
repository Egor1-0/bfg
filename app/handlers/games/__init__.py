from aiogram import Router

from app.handlers.games.cube import cubes_router
from app.handlers.games.basketball import basketball_router
from app.handlers.games.darts import darts_router
from app.handlers.games.football import football_router
from app.filters import CheckMoney


games_router = Router()

games_router.message.filter(CheckMoney())

games_router.include_routers(basketball_router, darts_router, football_router, cubes_router)