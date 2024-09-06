from aiogram.types import Message
from aiogram.filters import BaseFilter


class LenInputCube(BaseFilter):
    """
        Фильтр для проверки количества входных данных.
        Разделяет сообщение на слова и проверяет, что их ровно три.
        Возвращает True, если условие выполнено.
    """
    async def __call__(self, message: Message):

        input_data = message.text.lower().split(' ')
        return len(input_data) == 3


class CubeValue(BaseFilter):
    """
        Фильтр для проверки значения кубика.
        Преобразует третье слово в число и проверяет,
        входит ли оно в диапазон от 1 до 6.
        Возвращает True, если условие выполнено.
    """
    async def __call__(self, message: Message):
        input_data = message.text.lower().split(' ')
        try:
            input_data[2] = int(input_data[2])
        except:
            return False
        if input_data[2] in [1, 2, 3, 4, 5, 6]:
            return True
        return False


class RateValueCube(BaseFilter):
    """
    Фильтр для проверки ставки.
    Преобразует второе слово в число и проверяет,
    что ставка не меньше 10.
    Возвращает True, если условие выполнено.
    """
    async def __call__(self, message: Message):
        input_data = message.text.lower().split(' ')
        try:
            input_data[1] = int(input_data[1])
        except:
            return False

        return input_data[1] >= 10
