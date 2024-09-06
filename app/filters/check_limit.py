from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user

class CheckLimit(BaseFilter):
    async def __call__(self, message: Message):
        user = await get_user(message.from_user.id)
        if user.limit > 0:
            return True
        else:
            await message.answer('❌ | У вас закончился лимит')
