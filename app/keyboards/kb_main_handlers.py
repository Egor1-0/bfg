from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🤩 Добавить в беседу', url="https://t.me/bfg_sursbot?startgroup=new"), InlineKeyboardButton(text='👥 Наша беседа', url='https://t.me/BFG_surs')]
])

help_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💡 Основное', callback_data='base'), InlineKeyboardButton(text='🎲 Игры', callback_data='game')],
    [InlineKeyboardButton(text='💥 Развлекательное', callback_data='entertainment'), InlineKeyboardButton(text='🏰 Кланы', callback_data='clan')]
])

back_help = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])
