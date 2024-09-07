from aiogram.fsm.state import State, StatesGroup

from aiogram import Router
from aiogram.types import Message

from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Start

from app.states.states import MainMenu, Car





main_menu = Window(
    Const('Выберите категорию'),
    Start(text=Const("Машины"), id="layout", state=Car.main_menu),
    state=MainMenu.main_menu
)

main_menu_dialog = Dialog(main_menu)
