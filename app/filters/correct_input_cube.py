from aiogram.types import Message
from aiogram.filters import BaseFilter

class LenInputCube(BaseFilter):
    async def __call__(self, message: Message):  
        input_data = message.text.lower().split(' ')
        return len(input_data) == 3
    

class CubeValue(BaseFilter):
    async def __call__(self, message: Message):  
        input_data = message.text.lower().split(' ')
        try:
            input_data[1] = int(input_data[1])
        except:
            return False
        if input_data[1] in [1, 2, 3, 4, 5, 6]:
            return True
        return False
        

class RateValueCube(BaseFilter):
    async def __call__(self, message: Message):  
        input_data = message.text.lower().split(' ')
        try:
            input_data[2] = int(input_data[2])
        except:
            return False
        
        return input_data[2] >= 10