from aiogram.types import Message
from aiogram.filters import BaseFilter

class LenInputGame(BaseFilter):
    async def __call__(self, message: Message):  
        input_data = message.text.lower().split(' ')
        return len(input_data) == 2
        

class RateValue(BaseFilter):
    async def __call__(self, message: Message):  
        input_data = message.text.lower().split(' ')
        try:
            input_data[1] = int(input_data[1])
        except:
            return False
        
        return input_data[1] >= 10