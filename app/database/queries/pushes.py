from sqlalchemy import update

from app.database.models import User, Finance, Characteristic, Ore
from app.database.session import async_session
from app.database.queries import get_user_id


async def push_ore():
    async with async_session() as session:
        session.add(Ore(ore="iron", experience=0))
        session.add(Ore(ore="gold", experience=500))
        session.add(Ore(ore="diamond", experience=2000))
        session.add(Ore(ore="amethyst", experience=10000))
        session.add(Ore(ore="aquamarine", experience=25000))
        session.add(Ore(ore="emerald", experience=60000))
        session.add(Ore(ore="matter", experience=100000))
        session.add(Ore(ore="plasma", experience=500000))
        session.add(Ore(ore="nickel", experience=950000))
        session.add(Ore(ore="titanium", experience=5000000))
        session.add(Ore(ore="cobalt", experience=20000000))
        session.add(Ore(ore="ectoplasm", experience=10000000000))
        await session.commit()


async def push_user(user_id: int):
    async with async_session() as session:
        session.add(User(tg_id=user_id))
        await session.commit()
        session.add(Finance(user=await get_user_id(user_id)))
        session.add(Characteristic(user=await get_user_id(user_id)))
        await session.commit()


async def increanse(bit: int, user_id: int):
    async with async_session() as session:
        await session.execute(update(Finance).values(money = Finance.money + bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()


async def deincreanse(bit: int, user_id: int):
    async with async_session() as session:
        await session.execute(update(Finance).values(money = Finance.money - bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()