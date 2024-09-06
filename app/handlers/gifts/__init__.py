from aiogram import Router

from app.handlers.gifts.gift_handlers import gift_router_enough
from app.handlers.gifts.gift_handler_no_money import gift_router_no_money

gift_router = Router()

gift_router.include_routers(gift_router_enough, gift_router_no_money)