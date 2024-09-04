from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

from app.database.queries import get_user, push_user

class CheckUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if await get_user(event.from_user.id):
            return await handler(event, data)
        
        await push_user(event.from_user.id)
        await event.answer("Вы зарегестрированы. Напишите /help для получения помощи")
        return await handler(event, data)