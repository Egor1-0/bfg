from sqlalchemy import select, update

from app.database.models import User, Finance, Characteristic, Ore, Inventory
from app.database.session import async_session
from app.database.queries import get_user_money, get_user_id


async def push_ore():
    async with async_session() as session:
        session.add(Ore(ore="железо", experience=0))
        session.add(Ore(ore="золото", experience=500))
        session.add(Ore(ore="алмаз", experience=2000))
        session.add(Ore(ore="аметист", experience=10000))
        session.add(Ore(ore="аквамарин", experience=25000))
        session.add(Ore(ore="изумруд", experience=60000))
        session.add(Ore(ore="материя", experience=100000))
        session.add(Ore(ore="плазма", experience=500000))
        session.add(Ore(ore="никель", experience=950000))
        session.add(Ore(ore="титан", experience=5000000))
        session.add(Ore(ore="кобальт", experience=20000000))
        session.add(Ore(ore="эктоплазма", experience=10000000000))
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
        await session.execute(update(Finance).values(money=Finance.money + bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()


async def deincreanse(bit: int, user_id: int):
    async with async_session() as session:
        await session.execute(update(Finance).values(money=Finance.money - bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()

async def increanse_ores(user_id, name_ores, amount_ores):
    async with async_session() as session:
        await session.execute(update(Inventory).values(name_ores=Inventory.name_ores + amount_ores))
