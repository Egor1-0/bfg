from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user

class CheckLimit(BaseFilter):
    async def __call__(self, message: Message):
        """
        Фильтр для проверки лимита пользователя.
        Получает данные о пользователе из базы данных и проверяет,
        что его лимит больше нуля.
        Возвращает True, если лимит положительный, и False в противном случае.
        """
        user = await get_user(message.from_user.id)
        if user.limit > 0:
            return True
        else:
            return False
