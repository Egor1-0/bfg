import random
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f

from app.filters import LenInputData, DateValue
from app.database.queries import increanse, deincreanse
from app.filters import CheckMoney

gift_router = Router()

gift_router.message.filter(CheckMoney())

gift_router.message.filter(F.text.lower().startswith('дать'))


@gift_router.message(or_f(~LenInputData(), ~DateValue()))
async def error(message: Message):
    await message.answer('Необходимо ввести сумму: целое число больше 10')


@gift_router.message(LenInputData(), DateValue())
async def give_money_handler(message: Message):
    if message.reply_to_message is None:
        await message.answer("Чтобы передать деньги, нужно ответить на сообщение пользователя 😞")
        return
    amount = int(message.text.split(" ")[1])
    await increanse(amount, message.reply_to_message.from_user.id)
    await deincreanse(amount, message.from_user.id)


    await message.reply_to_message.answer(
        f"✅ | {amount} успешно передано пользователю {message.reply_to_message.from_user.full_name}!"
    )
