import random
from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue
from app.database.queries import increanse, loss, update_user
from app.database.queries.requests import get_user

base_router = Router()


@base_router.message(F.text.lower().startswith('дать'))
async def give_money_handler(message: Message):
    if message.reply_to_message is None:
        await message.answer("Чтобы передать деньги, нужно ответить на сообщение пользователя 😞")
        return
    try:
        amount = int(message.text.split()[1])
        user = await get_user(message.from_user.id)
        recipient_id = message.reply_to_message.from_user.id
        recipient = await get_user(recipient_id)

        if user.money < amount:
            await message.reply_to_message.answer(
                f"❌ | У вас недостаточно денег на балансе \n💰 Текущий баланс: {user.money}"
            )
            return

        user.money -= amount
        recipient.money += amount


        await update_user(user)
        await update_user(recipient)

        await message.reply_to_message.answer(
            f"✅ | {amount} успешно передано пользователю {message.reply_to_message.from_user.full_name}!"
        )

    except (IndexError, ValueError):
        await message.answer("Пожалуйста, укажите сумму после команды 'дать'. Например: 'дать 100'.")