from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user_characteristic

class CheckEnergy(BaseFilter):
    async def __call__(self, message: Message):
        """
        Фильтр для проверки энергии пользователя.
        Получает данные о характеристиках пользователя из базы данных
        и проверяет, что уровень энергии больше нуля.
        Возвращает True, если энергия положительна и существует,
        и False в противном случае.
        """
        energy = (await get_user_characteristic(message.from_user.id)).energy

        if (not energy) or energy <= 0:
            return False
        return True
