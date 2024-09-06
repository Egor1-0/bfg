import random
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f

from app.filters import LenInputData, DateValue
from app.database.queries import increanse, deincreanse
from app.filters import CheckMoney, CheckLimit

gift_router_no_money = Router()

gift_router_no_money.message.filter(F.text.lower().startswith('дать'))



@gift_router_no_money.message(~CheckMoney())
async def error(message: Message):
    await message.answer('Недостаточно средств')


@gift_router_no_money.message(~CheckLimit())
async def error(message: Message):
    await message.answer('❌ | У вас закончился лимит')