from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Start

from app.states.states import MainMenu

TO_MAIN = Start(text=Const("Main menu"), id="main_menu", state=MainMenu.main_menu)