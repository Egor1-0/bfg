from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.states.states import MainMenu
from app.keyboards.kb_shops import *
from app.database.queries.requests import get_property_all
from app.database.queries import *

buy_router = Router()

ITEMS_PER_PAGE = 5

def create_pagination_keyboard(items, page, user_id):
    builder = InlineKeyboardBuilder()

    start_index = page * ITEMS_PER_PAGE
    end_index = min(start_index + ITEMS_PER_PAGE, len(items))

    # Добавляем кнопки автомобилей в вертикальный столбец
    for item in items[start_index:end_index]:
        builder.button(text=item.name, callback_data=f"car_{item.id}")
        builder.adjust(1)  # Выравнивание кнопок автомобилей в столбик

    # Создаем клавиатуру для навигационных кнопок
    navigation_builder = InlineKeyboardBuilder()

    # Добавляем кнопки навигации
    if page > 0:
        navigation_builder.button(text="⬅️", callback_data=f"page_{page - 1}_{user_id}")
    navigation_builder.button(text="Меню", callback_data=f"menu_{user_id}")
    if end_index < len(items):
        navigation_builder.button(text="➡️", callback_data=f"page_{page + 1}_{user_id}")

    # Выравнивание навигационных кнопок в одну строку
    navigation_builder.adjust(3)

    # Добавляем навигационные кнопки на отдельной строке после кнопок автомобилей
    builder.row(*navigation_builder.buttons)  # Добавляем навигационные кнопки отдельно
    return builder

@buy_router.message(F.text.lower().startswith("магазин"))
async def category_shop(message: Message):
    keyboard = create_main_shop_keyboard(message.from_user.id)
    await message.answer('📦 Выберите категорию:', reply_markup=keyboard.as_markup())


@buy_router.callback_query(F.data.startswith("cars_"))
async def show_cars(callback_query: CallbackQuery):
    user_id = int(callback_query.data.split("_")[1])

    if callback_query.from_user.id == user_id:
        page = 0  # Начинаем с первой страницы
        await send_car_page(callback_query.message, page)
    else:
        await callback_query.answer('это кнопка не для вас', show_alert=True)

async def send_car_page(message, page):
    properties = await get_property_all()  # Получаем список автомобилей
    user_id = message.from_user.id
    keyboard = create_pagination_keyboard(properties, page, user_id)
    await message.edit_text('🚗 Выберите машину:', reply_markup=keyboard.as_markup())

@buy_router.callback_query(F.data.startswith("page_"))
async def handle_pagination(callback_query: CallbackQuery):
    user_id = int(callback_query.data.split("_")[2])
    if callback_query.from_user.id == user_id:
        page = int(callback_query.data.split("_")[1])
        await send_car_page(callback_query.message, page)
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)

@buy_router.callback_query(F.data == "menu")
async def back_to_menu(callback_query: CallbackQuery):
    user_id = int(callback_query.data.split("_")[1])
    if callback_query.from_user.id == user_id:
        keyboard = create_main_shop_keyboard(callback_query.from_user.id)  # Возвращаемся в главное меню магазина
        await callback_query.message.edit_text('📦 Выберите категорию:', reply_markup=keyboard.as_markup())
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)