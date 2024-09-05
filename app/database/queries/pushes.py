from sqlalchemy import select, update

from app.database.models import User, Finance, Characteristic, Ore, Inventory
from app.database.session import async_session
from app.database.queries import get_ores, get_user_id, get_ore_id


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
        for ore in await get_ores():
            session.add(Inventory(user=await get_user_id(user_id), ore = ore.id))
        await session.commit()


async def increanse(bit: int, user_id: int):
    async with async_session() as session:
        await session.execute(update(Finance).values(money=Finance.money + bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()


async def deincreanse(bit: int, user_id: int):
    async with async_session() as session:
        await session.execute(update(Finance).values(money=Finance.money - bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()

async def increanse_ores(user_tg_id, name_ore, amount_ore):
    async with async_session() as session:
        user_id = await get_user_id(user_tg_id)
        ore_id = await get_ore_id(name_ore)
        await session.execute(update(Inventory).values(ammount_ore=Inventory.ammount_ore + amount_ore).where(Inventory.user == user_id, Inventory.ore == ore_id))
        await session.commit()

async def deincreanse_energy(user_id: int):
    async with async_session() as session:
        await session.execute(update(Characteristic).values(energy=Characteristic.energy - 1).where(Characteristic.user == await get_user_id(user_id)))
        await session.commit()