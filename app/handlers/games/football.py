from aiogram import Router, F, Bot
from aiogram.types import Message

from app.filters import LenInputGame, RateValue
from app.database.queries import increanse

football_router = Router()

football_router.message.filter(F.text.lower().startswith('футбол'))

@football_router.message(~LenInputGame())
async def uncorrect_input(message: Message):
    await message.answer('Введите: футбол <цифра, на которую ставите> <ваша ставка>')


@football_router.message(~RateValue())
async def uncorrect_input(message: Message):
    await message.answer('Ставка должна быть целым числом от 10')


@football_router.message(LenInputGame(), RateValue())
async def cube(message: Message, bot: Bot): 
        mes = await bot.send_dice(chat_id=message.chat.id, emoji='⚽')
        # await message.answer(str(mes.dice.value))
        if mes.dice.value in [3, 4, 5, 6]:
            winning = int(message.text.split(' ')[1]) * (mes.dice.value - 3)
            await increanse(winning, message.from_user.id)
            await message.answer(f"Вы попали. ваш выигрыш: {winning}")
        else:
            await message.answer("Вы промахнулись")