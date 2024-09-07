from aiogram import F, Router
from aiogram.types import Message

from aiogram_dialog import DialogManager

from app.states.states import MainMenu

buy_router = Router()

buy_router.message.filter(F.text.lower().startswith("купить"))

@buy_router.message()
async def buy(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main_menu)
    
    
    

# @buy_router.message()
# async def sale(message: Message):
#     await message.answer("Неправильно введена руда")