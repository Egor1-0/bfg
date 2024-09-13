import random
from aiogram import Router, F
from aiogram.types import Message

from app.database.queries import deincreanse, increanse
from app.filters import CheckBankMoney
from app.keyboards.kb_case import *

case_router = Router()

@case_router.message(F.text.lower() == 'кейсы')
async def case_handlers(message: Message):
    keyboard = create_main_case_keyboard(message.from_user.id)
    await message.answer('🗃 Выберите кейс', reply_markup=keyboard)

@case_router.callback_query(F.data == 'case_one_')
async def case_one_handler(message: Message):
    await message.answer('')