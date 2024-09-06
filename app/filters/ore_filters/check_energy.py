from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user_characteristic

class CheckEnergy(BaseFilter):
    async def __call__(self, message: Message):
        energy = (await get_user_characteristic(message.from_user.id)).energy

        if (not energy) or energy <= 0:
            return False
        return True
