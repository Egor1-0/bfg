from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

ITEMS_PER_PAGE = 5



def create_main_shop_keyboard(user_id: int):
    builder = InlineKeyboardBuilder()
    categories = [
        ("🚗 Машины", "cars"),
        ("🏠 Недвижимость", "real_estate"),
        ("📱 Гаджеты", "gadgets"),
        ("✈️ Самолеты", "aircraft"),
        ("🛥 Яхты", "yachts"),
        ("🚁 Вертолеты", "helicopters"),
    ]

    for name, key in categories:
        builder.button(text=name, callback_data=f"{key}_{user_id}")

    builder.adjust(1)
    return builder


def create_pagination_keyboard(items, page: int, user_id: int, category: str):
    builder = InlineKeyboardBuilder()
    filtered_items = [item for item in items if item.category == category]

    start_index = page * ITEMS_PER_PAGE
    end_index = min(start_index + ITEMS_PER_PAGE, len(filtered_items))

    # Создание кнопок для элементов
    for item in filtered_items[start_index:end_index]:
        builder.button(
            text=item.name,
            callback_data=f"{category}_{user_id}_{item.id}"  # Убедитесь, что item.id используется корректно
        )
        builder.adjust(1)

    # Навигационные кнопки
    navigation_builder = InlineKeyboardBuilder()
    if page > 0:
        navigation_builder.button(text="⬅️", callback_data=f"page_{page - 1}_{user_id}_{category}")
    navigation_builder.button(text="Меню", callback_data=f"menu_{user_id}")
    if end_index < len(filtered_items):
        navigation_builder.button(text="➡️", callback_data=f"page_{page + 1}_{user_id}_{category}")

    navigation_builder.adjust(3)
    builder.row(*navigation_builder.buttons)

    return builder
