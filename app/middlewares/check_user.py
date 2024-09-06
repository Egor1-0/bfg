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
        """
        Промежуточное ПО для проверки наличия пользователя в базе данных и его регистрации.
        Если пользователь уже зарегистрирован, вызывает обработчик сообщения.
        Если пользователь не зарегистрирован, добавляет его в базу данных,
        отправляет сообщение о регистрации и затем вызывает обработчик сообщения.

        :param handler: Обработчик сообщения.
        :param event: Сообщение, которое требуется обработать.
        :param data: Дополнительные данные.
        :return: Результат выполнения обработчика.
        """
        if await get_user(event.from_user.id):
            return await handler(event, data)

        await push_user(event.from_user.id)
        await event.answer("🎉 Вы зарегистрированы. 🎉 \n 🖊 Напишите /help для получения помощи")
        return await handler(event, data)
