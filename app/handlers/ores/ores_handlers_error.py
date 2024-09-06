from aiogram import Router, F
from aiogram.types import Message
from app.filters import CheckOres, CheckEnergy

ores_error = Router()

ores_error.message.filter(F.text.lower().startswith('копать'))


@ores_error.message(~CheckOres())
async def error(message: Message):
    await message.answer('❌ | Не найден такой тип руды.')


@ores_error.message(~CheckEnergy())
async def error(message: Message):
    await message.answer('❌ | Недастоточно энергии для добычи руды.')

