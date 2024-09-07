from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f

from app.filters import LenInputData, DateValue
from app.database.queries import increanse, deincreanse, limit_user, get_user, push_transferred
from app.filters import CheckMoney, CheckLimit

gift_router_enough = Router()


gift_router_enough.message.filter(F.text.lower().startswith('дать'))

gift_router_enough.message.filter(CheckMoney())
gift_router_enough.message.filter(CheckLimit())

@gift_router_enough.message(or_f(~LenInputData(), ~DateValue()))
async def error(message: Message):
    await message.answer('Необходимо ввести сумму: целое число больше 10')


@gift_router_enough.message(LenInputData(), DateValue())
async def give_money_handler(message: Message):
    if message.reply_to_message is None: #дать деньги можно только ответив на сообщение человека, с которым хотите поделиться
        await message.answer("Чтобы передать деньги, нужно ответить на сообщение пользователя 😞")
        return
    user = await get_user(message.from_user.id)
    amount = int(message.text.split(" ")[1])
    if user.limit >= amount: #проверка, не перевел ли человек больше денег чем может
        await increanse(amount, message.reply_to_message.from_user.id)
        await deincreanse(amount, message.from_user.id)
        await limit_user(message.from_user.id, amount)
        await push_transferred(message.from_user.id, amount)
        await message.reply_to_message.answer(
            f"✅ | {amount} успешно передано пользователю {message.reply_to_message.from_user.full_name}!"
        )
    else:
        await message.answer(f"⚠️ | Ваш лимит : {user.limit}")
