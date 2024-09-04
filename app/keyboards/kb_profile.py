from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

main_profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏠 Имущество', callback_data='property')],
    [InlineKeyboardButton(text='🏭 Бизнесы', callback_data='business')]
])