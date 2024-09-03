from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue
from app.database.queries import increanse

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
        if mes.dice.value in [2, 3, 4, 5, 6]:
            winning = (0 if mes.dice.value in [2, 3] else int(message.text.split(' ')[1])*(mes.dice.value - 3))
            await increanse(winning, message.from_user.id)
            await message.answer(f"Вы попали. ваш выигрыш: {winning}")
        else:
            await message.answer("Вы промахнулись")