from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

from app.database.queries import get_user_energy
from app.middlewares import CheckEnergy

class CheckEnergy(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        energy = await get_user_energy(event.from_user.id)

        if energy is not None and energy < 0:
            await event.answer("Недостаточно энергии")
            return None

        return await handler(event, data)