import random
from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue
from app.database.queries import increanse, loss


basketball_router = Router()

basketball_router.message.filter(F.text.lower().startswith('баскетбол'))

emoji = ('😂', '😣', '🫢', '🤧')

@basketball_router.message(~LenInputGame())
async def uncorrect_input(message: Message):
    await message.answer('Введите: кубик <цифра, на которую ставите> <ваша ставка>')


@basketball_router.message(~RateValue())
async def uncorrect_input(message: Message):
    await message.answer('Ставка должна быть целым числом от 10')


@basketball_router.message(LenInputGame(), RateValue())
async def cube(message: Message, bot: Bot): 
        mes = await bot.send_dice(chat_id=message.chat.id, emoji='🏀')
        # money = int(message.text.split(' ')[1])
        # user = await get_user(message.from_user.id)
        # if user.money < money:
        #     await message.answer(
        #         f"❌ | У вас недостаточно средств для ставки {money}$. Ваш баланс: {user.money}$.")
        #     return
        if mes.dice.value in [4, 5]:
            winning = int(message.text.split(' ')[1]) * (mes.dice.value - 3)
            await increanse(winning, message.from_user.id)
            await message.answer(f"🎁 | {message.from_user.first_name} Вы попали! \n  💰 Вы получили {winning}$")
        else:
            losser = int(message.text.split(' ')[1])
            await loss(losser, message.from_user.id)
            randoms = random.choice(emoji)
            await message.answer(f"{randoms} | Вы проиграли {losser}$")