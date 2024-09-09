from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

ITEMS_PER_PAGE = 5

def create_main_shop_keyboard(user_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="🚗 Машины", callback_data=f"cars_{user_id}")
    builder.button(text="🏠 Недвижимость", callback_data=f"real_estate_{user_id}")
    builder.button(text="📱 Гаджеты", callback_data=f"gadgets_{user_id}")
    builder.button(text="✈️ Самолеты", callback_data=f"aircraft_{user_id}")
    builder.button(text="🛥 Яхты", callback_data=f"yachts_{user_id}")
    builder.button(text="🚁 Вертолеты", callback_data=f"helicopters_{user_id}")
    builder.adjust(1)
    return builder

def create_pagination_keyboard(items, page, user_id, category):
    builder = InlineKeyboardBuilder()

    # Фильтруем элементы по категории
    filtered_items = [item for item in items if item.category == category]

    start_index = page * ITEMS_PER_PAGE
    end_index = min(start_index + ITEMS_PER_PAGE, len(filtered_items))

    # Добавляем кнопки элементов в вертикальный столбец
    for item in filtered_items[start_index:end_index]:
        builder.button(text=item.name, callback_data=f"{category}_{item.id}_{user_id}")
        builder.adjust(1)  # Выравнивание кнопок элементов в столбик

    # Создаем клавиатуру для навигационных кнопок
    navigation_builder = InlineKeyboardBuilder()

    # Добавляем кнопки навигации
    if page > 0:
        navigation_builder.button(text="⬅️", callback_data=f"page_{page - 1}_{user_id}_{category}")
    navigation_builder.button(text="Меню", callback_data=f"menu_{user_id}")
    if end_index < len(filtered_items):
        navigation_builder.button(text="➡️", callback_data=f"page_{page + 1}_{user_id}_{category}")

    # Выравнивание навигационных кнопок в одну строку
    navigation_builder.adjust(3)

    # Добавляем навигационные кнопки на отдельной строке после кнопок элементов
    builder.row(*navigation_builder.buttons)  # Добавляем навигационные кнопки отдельно
    return builder
