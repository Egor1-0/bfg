from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_ore

class CheckOres(BaseFilter):
    async def filter(self, message: Message) -> bool:
        ore = await get_ore(message.text.lower)

