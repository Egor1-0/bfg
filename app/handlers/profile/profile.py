from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.queries import push_user, get_user, get_user_money, get_user_characteristic
from app.keyboards.kb_profile import main_profile

profile_router = Router()


@profile_router.message(Command("profile"))
@profile_router.message(F.text.lower() == "профиль")
async def cmd_profile(message: Message):
    profile = await get_user(message.from_user.id)
    finance = await get_user_money(message.from_user.id)
    ch = await get_user_characteristic(message.from_user.id)
    if not profile:
        await push_user(message.from_user.id)
    else:
        profile_text = (
            f"🪪 ID: {profile.id} \n"
            f"🏆 Статус: {profile.status.value}\n"
            f"💰 Денег: {finance.money}$ \n"
            f"🏦 В банке: {finance.bank}$ \n"
            f"💽 Биткоины: {finance.bitcoin}฿ \n"
            f"🏋️ Энергия: {ch.energy} \n"
            f"👑 Рейтинг: {ch.rating} \n"
            f"🌟 Опыт: {ch.experience} \n"
            f"🎲 Всего сыграно игр: {profile.games_played}"
        )
        await message.answer(profile_text, reply_markup=main_profile)