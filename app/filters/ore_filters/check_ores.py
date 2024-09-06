from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_ores

class CheckOres(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        ores = await get_ores()
        ore_name = message.text.lower().split(' ')[1]
        for ore in ores:
            if ore.ore == ore_name:
                return True


