from aiogram import F, Router
from aiogram.types import Message

from app.database.queries import get_ore, increanse, get_user_ore_count, reset_ammoint_ore
from app.filters import CheckOres

sale_router = Router()

sale_router.message.filter(F.text.lower().startswith("продать"))

@sale_router.message(CheckOres())
async def sale(message: Message):
    ore_name = message.text.lower().split(' ')[1]
    ore_price = (await get_ore(ore_name)).price
    user = message.from_user.id
    ammount_ore = (await get_user_ore_count(user, ore_name))
    await increanse(ore_price * ammount_ore, user)
    await reset_ammoint_ore(user, ore_name)
    await message.answer((f"✨ Вы получили {ore_price * ammount_ore}$"))
    

@sale_router.message(~CheckOres())
async def sale(message: Message):
    await message.answer("Неправильно введена руда")

