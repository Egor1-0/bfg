from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_ores

class CheckOres(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        """
        Фильтр для проверки наличия указанного руды в базе данных.
        Получает список всех руд из базы данных и проверяет,
        что рудное название, указанное во втором слове сообщения, присутствует в этом списке.
        Возвращает True, если руда найдена, и False в противном случае.
        """
        ores = await get_ores()
        ore_name = message.text.lower().split(' ')[1]
        for ore in ores:
            if ore.ore == ore_name:
                return True
        return False
