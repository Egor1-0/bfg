import random
from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue
from app.database.queries import increanse, loss
from app.database.queries.requests import get_user

football_router = Router()

football_router.message.filter(F.text.lower().startswith('футбол'))

emoji = ('😂', '😣', '🫢', '🤧')

@football_router.message(~LenInputGame())
async def uncorrect_input(message: Message):
    await message.answer('Введите: футбол <цифра, на которую ставите> <ваша ставка>')


@football_router.message(~RateValue())
async def uncorrect_input(message: Message):
    await message.answer('Ставка должна быть целым числом от 10')


@football_router.message(LenInputGame(), RateValue())
async def cube(message: Message, bot: Bot): 
        mes = await bot.send_dice(chat_id=message.chat.id, emoji='⚽')
        money = int(message.text.split(' ')[1])
        user = await get_user(message.from_user.id)
        if user.money < money:
            await message.answer(
                f"❌ | У вас недостаточно средств для ставки {money}$. Ваш баланс: {user.money}$.")
            return
        # await message.answer(str(mes.dice.value))
        if mes.dice.value in [3, 4, 5, 6]:
            winning = int(message.text.split(' ')[1]) * (mes.dice.value - 3)
            await increanse(winning, message.from_user.id)
            await message.answer(f"🎁 | {message.from_user.first_name} Вы попали! \n  💰 Вы получили +{winning}$")
        else:
            losser = int(message.text.split(' ')[1])
            await loss(losser, message.from_user.id)
            randoms = random.choice(emoji)
            await message.answer(f"{randoms} | Вы проиграли {losser}$")