from aiogram.types import Message
from aiogram.filters import BaseFilter

from app.database.queries import get_user_money

class CheckMoney(BaseFilter):
    async def __call__(self, message: Message):
        input_data = message.text.lower().split(' ')
        if len(input_data) >= 2:       
            user = await get_user_money(message.from_user.id)
            try:
                if user.money >= int(input_data[1]):
                    return True
                else:
                    return False
            except:
                return False
