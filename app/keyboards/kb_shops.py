from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_main_shop_keyboard(user_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="🚗 Машины", callback_data=f"cars_{user_id}")
    builder.button(text="🏠 Недвижимость", callback_data="real_estate")
    builder.button(text="📱 Гаджеты", callback_data="gadgets")
    builder.button(text="✈️ Самолеты", callback_data="aircraft")
    builder.button(text="🛥 Яхты", callback_data="yachts")
    builder.button(text="🚁 Вертолеты", callback_data="helicopters")
    builder.adjust(1)
    return builder
