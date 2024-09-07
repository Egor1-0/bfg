from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user_money, get_bank

class CheckBankMoney(BaseFilter):
    async def __call__(self, message: Message):
        """
        Фильтр для проверки наличия достаточного количества денег у пользователя.
        Разделяет сообщение на слова и проверяет, что количество денег
        у пользователя (из базы данных) больше или равно значению во втором слове.
        Возвращает True, если условие выполнено, и False в противном случае.
        """
        input_data = message.text.lower().split(' ')
        if len(input_data) == 3:
            if input_data[1] == 'положить':
                if int(input_data[2]) <= (await get_user_money(message.from_user.id)).money:
                    return True
                return False
            if input_data[1] == 'снять':
                if int(input_data[2]) >= (await get_bank(message.from_user.id)).money_ammount:
                    return True
                return False
            return False
        return False