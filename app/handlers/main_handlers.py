from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.database.queries import push_user, get_user

main_router = Router()

@main_router.message(CommandStart())
async def start(message: Message):
    await message.answer("траляляля текст крч")
    if not (await get_user(message.from_user.id)):
        await push_user(message.from_user.id)


@main_router.message(Command("help"))
@main_router.message(F.text.lower() == "помощь")
async def help(message: Message):
    await message.answer("Текст помощи")

