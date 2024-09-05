import random
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f

from app.filters import LenInputData, DateValue
from app.database.queries import (increanse, deincreanse, get_user_inventory,
                                  increanse_ores, deincreanse_energy, get_user_characteristic, get_ores, update_user_experience)
from app.filters import CheckEnergy, CheckOres
from app.src.ores_list import ore_icon, experience_ranges

ores_router = Router()

# ores_router.message.filter(CheckEnergy(), CheckOres())

ores_router.message.filter(F.text.lower().startswith('копать'))


@ores_router.message(CheckEnergy(), CheckOres())
async def ores_get(message: Message):
    ore_name = message.text.lower().split(' ')[1]
    random_ores = random.randint(1, 100)

    user_characteristic = await get_user_characteristic(message.from_user.id)
    if not user_characteristic:
        await message.answer('Ошибка получения характеристик пользователя.')
        return

    ores = await get_ores()

    ore_info = next((ore for ore in ores if ore.ore == ore_name), None)
    if not ore_info:
        await message.answer('Ошибка получения информации о руде.')
        return

    if user_characteristic.experience >= ore_info.experience:
        min_exp, max_exp = experience_ranges.get(ore_name, (0, 0))
        earned_experience = random.randint(min_exp, max_exp)

        await update_user_experience(message.from_user.id, earned_experience)

        await increanse_ores(message.from_user.id, ore_name, random_ores)
        await deincreanse_energy(message.from_user.id)

        ore_icons = ore_icon.get(ore_name)
        await message.answer(
            f'{ore_icons} | +{random_ores} {ore_name} \n ⚡️ Энергия: {user_characteristic.energy} 🌟 Опыт: {user_characteristic.experience + earned_experience}'
        )
    else:
        await message.answer(
            f'❌ | У вас недостаточно опыта для добычи {ore_name}. \n⚠️ | Требуется {ore_info.experience} опыта.'
        )

