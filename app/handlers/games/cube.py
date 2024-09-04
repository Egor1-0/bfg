import random
from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import CubeValue, LenInputCube, RateValueCube
from app.database.queries import increanse, loss

cubes_router = Router()

cubes_router.message.filter(F.text.lower().startswith('кубик'))

emoji = ('😂', '😣', '🫢', '🤧')

@cubes_router.message(~LenInputCube())
async def uncorrect_input(message: Message):
    await message.answer('Введите: кубик <цифра, на которую ставите> <ваша ставка>')


@cubes_router.message(~CubeValue())
async def uncorrect_input(message: Message):
    await message.answer('Цифра кубика должна быть целым числом от 1 до 6')


@cubes_router.message(~RateValueCube())
async def uncorrect_input(message: Message):
    await message.answer('Ставка должна быть целым числом от 10')


@cubes_router.message(CubeValue(), LenInputCube(), RateValueCube())
async def cube(message: Message, bot: Bot): 
        mes = await bot.send_dice(chat_id=message.chat.id, emoji='🎲')
        # money = int(message.text.split(' ')[1])
        # user = await get_user(message.from_user.id)
        # if user.money < money:
        #     await message.answer(
        #         f"❌ | У вас недостаточно средств для ставки {money}$. Ваш баланс: {user.money}$.")
        #     return
        if str(mes.dice.value) == message.text.split(' ')[1]:
            winning = int(message.text.split(' ')[2]) * 2
            await increanse(winning, message.from_user.id)
            await message.answer(f"🎁 | {message.from_user.first_name} Вы выиграли! \n  💰 Вы получили +{winning}$")
        else:
            losser = int(message.text.split(' ')[2])
            await loss(losser, message.from_user.id)
            randoms = random.choice(emoji)
            await message.answer(f"{randoms} | Вы проиграли {losser}$")