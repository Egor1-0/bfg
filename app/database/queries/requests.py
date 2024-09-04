from sqlalchemy import select

from app.database.models import User, Finance, Characteristic
from app.database.session import async_session

async def get_user(user_id: int):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == user_id))


async def get_user_tg_id(user_id: int) -> int:
    async with async_session() as session:
        return (await session.scalar(select(User).where(User.id == user_id))).tg_id
    

async def get_user_id(user_id: int) -> int:
    async with async_session() as session:
        return (await session.scalar(select(User).where(User.tg_id == user_id))).id
    

async def get_user_money(user_id: int):
    async with async_session() as session:
        # print(await get_user_id(user_id), await session.scalar(select(Finance).where(Finance.user == await get_user_id(user_id))))
        return await session.scalar(select(Finance).where(Finance.user == await get_user_id(user_id)))


async def get_user_characteristic(user_id: int):
    async with async_session() as session:
        return await session.scalar(select(Characteristic).where(Characteristic.user == await get_user_id(user_id)))

