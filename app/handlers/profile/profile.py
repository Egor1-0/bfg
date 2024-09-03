from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.database.queries import push_user, get_user
from app.handlers.profile.kb_profile import main_profile

profile_router = Router()

@profile_router.message(Command("profile"))
@profile_router.message(F.text.lower() == "профиль")
async def cmd_profile(message: Message):
    profile = await get_user(message.from_user.id)
    if not profile:
        await push_user(message.from_user.id)
    else:
        profile_text = (
            f"🪪 ID: {profile.id} \n"
            f"🏆 Статус: {profile.status.value}\n"
            f"💰 Денег: {profile.money}$ \n"
            f"🏦 В банке: {profile.bank}$ \n"
            f"💽 Биткоины: {profile.bitcoin}฿ \n"
            f"🏋️ Энергия: {profile.energy} \n"
            f"👑 Рейтинг: {profile.rating} \n"
            f"🌟 Опыт: {profile.experience} \n"
            f"🎲 Всего сыграно игр: {profile.games_played}"
        )
        await message.answer(profile_text, reply_markup=main_profile)
