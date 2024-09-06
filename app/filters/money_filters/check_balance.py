from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user_money

class CheckMoney(BaseFilter):
    async def __call__(self, message: Message):
        """
        Фильтр для проверки наличия достаточного количества денег у пользователя.
        Разделяет сообщение на слова и проверяет, что количество денег
        у пользователя (из базы данных) больше или равно значению во втором слове.
        Возвращает True, если условие выполнено, и False в противном случае.
        """
        input_data = message.text.lower().split(' ')
        if len(input_data) >= 2:
            # Получает данные о деньгах пользователя из базы данных
            user = await get_user_money(message.from_user.id)
            try:
                # Проверяет, достаточно ли денег у пользователя
                if user.money >= int(input_data[1]):
                    return True
                else:
                    return False
            except:
                return False
