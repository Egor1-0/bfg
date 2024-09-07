from aiogram import Router

from app.dialog.main_menu import main_menu_dialog
from app.dialog.car import car_dialog

dialog_router = Router()

dialog_router.include_routers(main_menu_dialog, car_dialog)