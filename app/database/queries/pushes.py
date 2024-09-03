from sqlalchemy import select

from app.database.models import User
from app.database.session import async_session

async def push_user(user_id: int):
    async with async_session() as session:
        session.add(User(tg_id=user_id))
        await session.commit()


async def increanse(bit: int, user_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == user_id))
        user.money += bit
        await session.commit()

async def loss(bit: int, user_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == user_id))
        user.money -= bit
        await session.commit()

