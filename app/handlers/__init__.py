from aiogram import Router

from app.handlers.main_handlers import main_router
from app.handlers.profile import profile_router_
from app.handlers.games import games_router
from app.handlers.gifts import gift_router
from app.handlers.ores import ores_router_
from app.handlers.shop.sale.sale_ore import sale_router


main_router_ = Router()


main_router_.include_routers(main_router, profile_router_, gift_router, ores_router_, sale_router, games_router)





"""
продажа-покупка

банк

ограбить мэрию

рейтинг

"""




























