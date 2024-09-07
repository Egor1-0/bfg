from sqlalchemy import select

from app.database.models import User, Finance, Characteristic, Inventory, Ore, Bank, Property
from app.database.session import async_session

async def get_user(user_id: int):
    """ПОЛУЧЕНИЕ ЮЗЕРА ПО ТГ АЙДИ"""
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == user_id))


async def get_user_tg_id(user_id: int) -> int:
    """ПОЛУЧЕНИЕ ТГ АЙДИ ЮЗЕРА ПО АЙДИ ИЗ БД"""
    async with async_session() as session:
        return (await session.scalar(select(User).where(User.id == user_id))).tg_id
    

async def get_user_id(user_id: int) -> int:
    """ПОЛУЧЕНИЕ АЙДИ ЮЗЕРА ПО ТГ АЙДИ"""
    async with async_session() as session:
        return (await session.scalar(select(User).where(User.tg_id == user_id))).id


async def get_user_money(user_id: int):
    """ПОЛУЧЕНИЕ ДЕНЕГ ПОЛЬЗОВАТЕЛЯ ПО ТГ АЙДИ"""
    async with async_session() as session:
        await get_user_id(user_id), await session.scalar(select(Finance).where(Finance.user == await get_user_id(user_id)))
        return await session.scalar(select(Finance).where(Finance.user == await get_user_id(user_id)))


async def get_user_characteristic(user_id: int):
    """ПОЛУЧЕНИЕ ХАРАКТЕРИСТИКИ ПОЛЬЗОВАТЕЛЯ ПО ТГ АЙДИ"""
    async with async_session() as session:
        return await session.scalar(select(Characteristic).where(Characteristic.user == await get_user_id(user_id)))


async def get_user_inventory(user_id: int):
    """ПОЛУЧЕНИЕ ИНВЕНТАРЯ ПОЛЬЗОВАТЕЛЯ ПО ТГ АЙДИ"""
    async with async_session() as session:
        return await session.scalars(select(Inventory).where(Inventory.user == await get_user_id(user_id)))


async def get_ores():
    """ПОЛУЧЕНИЕ ВСЕХ РУД"""
    async with async_session() as session:
        return await session.scalars(select(Ore))


async def get_user_ore_count(user_id: int, ore_name: str):
    """ПОЛУЧЕНИЕ КОЛВА ОПРЕДЕЛЕННОЙ РУДЫ У ПОЛЬЗОВАТЕЛЯ"""
    async with async_session() as session:
        return (await session.scalar(select(Inventory).where((Inventory.user == await get_user_id(user_id)) & (Inventory.ore == (await get_ore(ore_name)).id)))).ammount_ore


async def get_ore(ore_name: str):
    """ПОЛУЧЕНИЕ РУДЫ ПО ИМЕНИ"""
    async with async_session() as session:
        return await session.scalar(select(Ore).where(Ore.ore == ore_name))
    

async def get_ore_by_id(id_: int):
    """ПОЛУЧЕНИЕ РУДЫ ПО АЙДИ"""
    async with async_session() as session:
        return await session.scalar(select(Ore).where(Ore.id == id_))


async def get_bank(user_tg_id: int):
    """ПОЛУЧЕНИЕ БАНКА ПО ТГ АЙДИ ЮЗЕРА"""
    async with async_session() as session:
        return await session.scalar(select(Bank).where(Bank.user == await get_user_id(user_tg_id)))
    

async def get_property_all():
    """ПОЛУЧЕНИЕ ИМУЩЕСТВА"""
    async with async_session() as session:
        return await session.scalars(select(Property))
    

async def get_property_by_id(id_: int):
    """ПОЛУЧЕНИЕ ИМУЩЕСТВА"""
    async with async_session() as session:
        return await session.scalar(select(Property).where(Property.id == id_))

# async def get_ore_id(ore: str) -> int:
#     """ПОЛУЧЕНИЕ АЙДИ АЙДИ РУДЫ ПО ИМЕНИ"""
#     async with async_session() as session:
#         return (await session.scalar(select(Ore).where(Ore.ore == ore))).id

