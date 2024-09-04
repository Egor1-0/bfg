from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

from app.database.queries import get_user_money

class CheckMoney(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        input_data = event.text.lower().split(' ')
        if len(input_data) >= 2:       
            user = await get_user_money(event.from_user.id)
            if user.money >= int(input_data[1]):
                return await handler(event, data)
            await event.answer("Недостаточно средств")
            return None
        return await handler(event, data)