from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.states.states import MainMenu
from app.keyboards.kb_shops import create_main_shop_keyboard, create_pagination_keyboard
from app.database.queries.requests import get_property_all

buy_router = Router()


@buy_router.message(F.text.lower().startswith("магазин"))
async def category_shop(message: Message):
    keyboard = create_main_shop_keyboard(message.from_user.id)
    await message.answer('📦 Выберите категорию:', reply_markup=keyboard.as_markup())

async def send_page(callback_query: CallbackQuery, page: int, category: str):
    properties = await get_property_all()  # Получаем список всех свойств
    user_id = callback_query.from_user.id
    keyboard = create_pagination_keyboard(properties, page, user_id, category)
    await callback_query.message.edit_text(f'🛍 Выберите товар:', reply_markup=keyboard.as_markup())

@buy_router.callback_query(F.data.startswith("cars_"))
@buy_router.callback_query(F.data.startswith("real_estate_"))
@buy_router.callback_query(F.data.startswith("gadgets_"))
@buy_router.callback_query(F.data.startswith("aircraft_"))
@buy_router.callback_query(F.data.startswith("yachts_"))
@buy_router.callback_query(F.data.startswith("helicopters_"))
async def show_items(callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    category = data[0]  # category like "cars", "real_estate", etc.
    user_id = int(data[1])

    if callback_query.from_user.id == user_id:
        page = 0  # Начинаем с первой страницы
        await send_page(callback_query, page, category)  # Передаем callback_query вместо message
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)

@buy_router.callback_query(F.data.startswith("page_"))
async def handle_pagination(callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    page = int(data[1])
    user_id = int(data[2])
    category = data[3]  # category should be included in pagination

    if callback_query.from_user.id == user_id:
        await send_page(callback_query, page, category)
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)

@buy_router.callback_query(F.data.startswith("menu_"))
async def back_to_menu(callback_query: CallbackQuery):
    user_id = int(callback_query.data.split("_")[1])

    if callback_query.from_user.id == user_id:
        keyboard = create_main_shop_keyboard(callback_query.from_user.id)  # Возвращаемся в главное меню магазина
        await callback_query.message.edit_text('📦 Выберите категорию:', reply_markup=keyboard.as_markup())
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)