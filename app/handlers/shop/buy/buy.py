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


@buy_router.callback_query(F.data.startswith(("cars_", "real_estate_", "gadgets_", "aircraft_", "yachts_", "helicopters_")))
async def show_items(callback_query: CallbackQuery):
    # Разделяем callback_data на части и проверяем, что данные корректны
    data = callback_query.data.split("_")
    category = data[0]  # Категория (cars, real_estate и т.д.)
    user_id = int(data[1])  # ID пользователя, который создавал кнопку

    if callback_query.from_user.id == user_id:
        # Если user_id совпадают, продолжаем обработку
        await send_page(callback_query, 0, category)
    else:
        # Если user_id не совпадают, выводим предупреждение
        await callback_query.answer('Это кнопка не для вас', show_alert=True)

@buy_router.callback_query(F.data.startswith("page_"))
async def handle_pagination(callback_query: CallbackQuery):
    _, page, user_id, category = callback_query.data.split("_")
    if callback_query.from_user.id == int(user_id):
        await send_page(callback_query, int(page), category)
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)

@buy_router.callback_query(F.data.startswith("menu_"))
async def back_to_menu(callback_query: CallbackQuery):
    user_id = int(callback_query.data.split("_")[1])
    if callback_query.from_user.id == user_id:
        keyboard = create_main_shop_keyboard(callback_query.from_user.id)
        await callback_query.message.edit_text('📦 Выберите категорию:', reply_markup=keyboard.as_markup())
    else:
        await callback_query.answer('Это кнопка не для вас', show_alert=True)

async def send_page(callback_query: CallbackQuery, page: int, category: str):
    properties = await get_property_all()
    user_id = callback_query.from_user.id
    keyboard = create_pagination_keyboard(properties, page, user_id, category)
    await callback_query.message.edit_text('🛍 Выберите товар:', reply_markup=keyboard.as_markup())


# Обработчик для кнопок с товарами

@buy_router.callback_query(F.data.regexp(r"^(cars|real_estate|gadgets|aircraft|yachts|helicopters)_\d+_\d+$"))
async def handle_item_callback(callback_query: CallbackQuery):
    data = callback_query.data.split("_")

    if len(data) == 3:  # Убедитесь, что формат корректный: category_item_id_user_id
        category = data[0]
        user_id = int(data[1])
        item_id = int(data[2])

        if callback_query.from_user.id == user_id:
            # Здесь можно извлечь информацию о товаре из базы данных
            await callback_query.answer(f"Вы выбрали товар {item_id} из категории {category}", show_alert=True)
        else:
            await callback_query.answer("Это кнопка не для вас", show_alert=True)
    else:
        await callback_query.answer("Ошибка в формате данных.", show_alert=True)
