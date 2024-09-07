from aiogram.fsm.state import State, StatesGroup

from aiogram import Router
from aiogram.types import CallbackQuery

from operator import itemgetter
from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Back

from app.states.states import Car
from app.database.queries import get_property_by_id, get_property_all
from app.dialog.common import TO_MAIN


async def get_products(**kwargs):
    property_list = await get_property_all()
    property_to_get = []
    for property_ in property_list:
        property_to_get.append((property_.name, property_.id))
    # property_list = [(property_list[i], i) for i in range(len(property_list))]
    return {
        "products": property_to_get
    }


async def get_item(callback: CallbackQuery, widget,
                            dialog_manager: DialogManager, item_id: int):
    prop = await get_property_by_id(item_id)
    await dialog_manager.switch_to(state=Car.car)
    dialog_manager.dialog_data["item"] = prop



main_menu = Window(
    Const('Выберите товар'),
    ScrollingGroup(
        Select(
            Format("{item[0]}"),
            id="multiselect",
            items = "products",
            item_id_getter=itemgetter(1),
            on_click=get_item
        ),
        id='def_scrolling_group',
        width=1,
        height=5
    ),
    TO_MAIN,
    getter=get_products,
    preview_data=get_products,
    state=Car.main_menu
)

async def get_product(dialog_manager: DialogManager, **kwargs):
    print(dialog_manager.dialog_data)
    return dialog_manager.dialog_data

card_prop = Window(
    Format("Название: {item.name}"),
    Format("Описание: {item.description}"),   
    Format("Цена: {item.price}"),
    Back(text=Const("Назад")),
    getter=get_product,
    state=Car.car
)

car_dialog = Dialog(main_menu, card_prop)
