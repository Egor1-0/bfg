from aiogram.types import Message
from aiogram.filters import BaseFilter


class LenInputData(BaseFilter):
    async def __call__(self, message: Message):
        """
        Фильтр для проверки количества входных данных.
        Разделяет сообщение на слова и проверяет, что их ровно два.
        Возвращает True, если условие выполнено.
        """
        input_data = message.text.lower().split(' ')
        return len(input_data) == 2


class DateValue(BaseFilter):
    async def __call__(self, message: Message):
        """
        Фильтр для проверки значения числа.
        Преобразует второе слово в число и проверяет,
        что оно не меньше 10.
        Возвращает True, если условие выполнено.
        """
        input_data = message.text.lower().split(' ')
        try:
            input_data[1] = int(input_data[1])
        except:
            return False

        return input_data[1] >= 10
