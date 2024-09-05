from sqlalchemy import select

from app.database.models import User, Finance, Characteristic
from app.database.session import async_session
from app.database.queries import get_user_money, get_user_id


async def push_user(user_id: int):
    async with async_session() as session:
        session.add(User(tg_id=user_id))
        await session.commit()
        session.add(Finance(user=await get_user_id(user_id)))
        session.add(Characteristic(user=await get_user_id(user_id)))
        await session.commit()


async def increanse(bit: int, user_id: int):
    async with async_session() as session:
        user_finance = await get_user_money(user_id)
        user_finance.money += bit
        await session.commit()

async def deincreanse(bit: int, user_id: int):
    async with async_session() as session:
        user_finance = await get_user_money(user_id)
        user_finance.money -= bit
        await session.commit()