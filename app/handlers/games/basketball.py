from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue

basketball_router = Router()

basketball_router.message.filter(F.text.lower().startswith('баскетбол'))

@basketball_router.message(~LenInputGame())
async def uncorrect_input(message: Message):
    await message.answer('Введите: кубик <цифра, на которую ставите> <ваша ставка>')


@basketball_router.message(~RateValue())
async def uncorrect_input(message: Message):
    await message.answer('Ставка должна быть целым числом от 10')


@basketball_router.message(LenInputGame(), RateValue())
async def cube(message: Message, bot: Bot): 
        mes = await bot.send_dice(chat_id=message.chat.id, emoji='🏀')
        if mes.dice.value in [4, 5]:
            await message.answer("Вы победили")
        else:
            await message.answer("Вы проиграли")