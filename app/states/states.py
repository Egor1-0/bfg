from aiogram.fsm.state import State, StatesGroup


class MainMenu(StatesGroup):
    main_menu = State()


class Car(StatesGroup):
    main_menu = State()
    car = State()