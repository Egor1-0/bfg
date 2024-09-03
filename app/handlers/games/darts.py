from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue

darts_router = Router()

darts_router.message.filter(F.text.lower().startswith('дартс'))

@darts_router.message(~LenInputGame())
async def uncorrect_input(message: Message):
    await message.answer('Введите: дартс <цифра, на которую ставите> <ваша ставка>')


@darts_router.message(~RateValue())
async def uncorrect_input(message: Message):
    await message.answer('Ставка должна быть целым числом от 10')


@darts_router.message(LenInputGame(), RateValue())
async def cube(message: Message, bot: Bot): 
        mes = await bot.send_dice(chat_id=message.chat.id, emoji='🎯')
        if str(mes.dice.value) in [2, 3, 4, 5, 6]:
            await message.answer("Вы попали")
        else:
            await message.answer("Вы промахнулись")