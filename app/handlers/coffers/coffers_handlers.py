import random
from aiogram import Router, F
from aiogram.types import Message

from app.database.queries import increanse_bank, deincreanse, increanse, get_user, get_user_money, update_coffers_status
from app.filters import CheckBankMoney

coffers_router = Router()

defult_coffers = 1000000


@coffers_router.message(F.text.lower() == 'ограбить казну')
async def coffers_rob(message: Message):
    coffers_user = await get_user(message.from_user.id)  # Получаем пользователя из базы данных
    user_money = await get_user_money(message.from_user.id)  # Получаем баланс пользователя

    # Проверяем, если пользователь уже грабил казну сегодня
    if coffers_user.coffers:
        await message.answer('Вы уже грабили казну сегодня. Бегите скорее, полиция уже в пути 🚫')
    else:
        # Рандомно выбираем True или False
        success = random.choice([True, False])

        if success:
            await increanse(defult_coffers, message.from_user.id)
            # Обновляем статус ограбления казны на True
            await update_coffers_status(message.from_user.id, True)  # Функция обновления статуса ограбления

            await message.answer(f'Вам повезло! Вы ограбили казну и получили {defult_coffers} 💰')
        else:
            await message.answer('К сожалению, вам не удалось ограбить казну ❎')
