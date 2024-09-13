from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

def create_main_case_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🎁 Кейсы №1', callback_data=f'case_one_{user_id}')],
        [InlineKeyboardButton(text='🎁 Кейсы №2', callback_data=f'case_two_{user_id}')],
        [InlineKeyboardButton(text='🎁 Кейсы №3', callback_data=f'case_three_{user_id}')]
    ])
