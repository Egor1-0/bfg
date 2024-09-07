from sqlalchemy import update, select

from app.database.models import User, Finance, Characteristic, Ore, Inventory, Property, Bank
from app.database.session import async_session
from app.database.queries import get_ores, get_user_id, get_ore

async def push_ore() -> None:
    """
    Push all ores into the database if they don't exist yet.

    This function takes no arguments and returns None.
    """
    async with async_session() as session:
        existing_ores = await session.execute(select(Ore).limit(1))
        if existing_ores.scalars().first() is not None:  # check if ores already exist
            return

        session.add_all([
            Ore(ore="железо", experience=0, price=230000),
            Ore(ore="золото", experience=500, price=1000000),
            Ore(ore="алмаз", experience=2000, price=116000000),
            Ore(ore="аметист", experience=10000, price=217000000),
            Ore(ore="аквамарин", experience=25000, price=461000000),
            Ore(ore="изумруд", experience=60000, price=792000000),
            Ore(ore="материя", experience=100000, price=8000000000),
            Ore(ore="плазма", experience=500000, price=12000000000),
            Ore(ore="никель", experience=950000, price=30000000000),
            Ore(ore="титан", experience=5000000, price=70000000000000),
            Ore(ore="кобальт", experience=20000000, price=120000000000000),
            Ore(ore="эктоплазма", experience=10000000000, price=20000000000000000)
        ])
        await session.commit()

async def push_car():
    async with async_session() as session:
        existing_property = await session.execute(select(Property).limit(1))
        if existing_property.scalars().first() is not None:
            return

        session.add_all([
            Property(
                name="Dacia Sandero",
                price=10000000,
                description="🚗 Максимальная скорость: 158 км/ч\n🐎 Лошадиных сил: 67\n⏱ Разгон до 100: 14,2 сек",
            ),
            Property(
                name="Kia Picanto",
                price=15000000,
                description="🚗 Максимальная скорость: 161 км/ч\n🐎 Лошадиных сил: 67\n⏱ Разгон до 100: 14,1 сек",
            ),
            Property(
                name="Hyundai i10",
                price=30000000,
                description="🚗 Максимальная скорость: 170 км/ч\n🐎 Лошадиных сил: 83\n⏱ Разгон до 100: 12,6 сек",
            ),
            Property(
                name="Ford Fiesta",
                price=50000000,
                description="🚗 Максимальная скорость: 183 км/ч\n🐎 Лошадиных сил: 100\n⏱ Разгон до 100: 10,5 сек",
            ),
            Property(
                name="Renault Clio",
                price=90000000,
                description="🚗 Максимальная скорость: 185 км/ч\n🐎 Лошадиных сил: 100\n⏱ Разгон до 100: 10,4 сек",
            ),
            Property(
                name="Volkswagen Polo",
                price=100000000,
                description="🚗 Максимальная скорость: 187 км/ч\n🐎 Лошадиных сил: 110\n⏱ Разгон до 100: 9,9 сек",
            ),
            Property(
                name="Mazda 3",
                price=250000000,
                description="🚗 Максимальная скорость: 204 км/ч\n🐎 Лошадиных сил: 122\n⏱ Разгон до 100: 9,1 сек",
            ),
            Property(
                name="Toyota Corolla",
                price=400000000,
                description="🚗 Максимальная скорость: 195 км/ч\n🐎 Лошадиных сил: 132\n⏱ Разгон до 100: 8,9 сек",
            ),
            Property(
                name="Honda Civic",
                price=600000000,
                description="🚗 Максимальная скорость: 200 км/ч\n🐎 Лошадиных сил: 158\n⏱ Разгон до 100: 8,5 сек",
            ),
            Property(
                name="BMW 3 Series",
                price=90000000,
                description="🚗 Максимальная скорость: 235 км/ч\n🐎 Лошадиных сил: 255\n⏱ Разгон до 100: 5,8 сек",
            ),
            Property(
                name="Audi A4",
                price=1400000000,
                description="🚗 Максимальная скорость: 250 км/ч\n🐎 Лошадиных сил: 261\n⏱ Разгон до 100: 5,6 сек",
            ),
            Property(
                name="Mercedes-Benz C-Class",
                price=2500000000,
                description="🚗 Максимальная скорость: 250 км/ч\n🐎 Лошадиных сил: 255\n⏱ Разгон до 100: 5,7 сек",
            ),
            Property(
                name="Tesla Model 3 Performance",
                price=6000000000,
                description="🚗 Максимальная скорость: 261 км/ч\n🐎 Лошадиных сил: 450\n⏱ Разгон до 100: 3,3 сек",
            ),
            Property(
                name="Porsche 718 Cayman",
                price=8000000000,
                description="🚗 Максимальная скорость: 275 км/ч\n🐎 Лошадиных сил: 300\n⏱ Разгон до 100: 4,9 сек",
            ),
            Property(
                name="BMW M4",
                price=10000000000,
                description="🚗 Максимальная скорость: 290 км/ч\n🐎 Лошадиных сил: 473\n⏱ Разгон до 100: 3,8 сек",
            ),
            Property(
                name="Audi RS5",
                price=40000000000,
                description="🚗 Максимальная скорость: 280 км/ч\n🐎 Лошадиных сил: 444\n⏱ Разгон до 100: 3,9 сек",
            ),
            Property(
                name="Nissan GT-R",
                price=100000000000,
                description="🚗 Максимальная скорость: 315 км/ч\n🐎 Лошадиных сил: 565\n⏱ Разгон до 100: 2,9 сек",
            ),
            Property(
                name="Porsche 911 Turbo",
                price=300000000000,
                description="🚗 Максимальная скорость: 320 км/ч\n🐎 Лошадиных сил: 572\n⏱ Разгон до 100: 2,7 сек",
            ),
            Property(
                name="Ferrari F8 Tributo",
                price=500000000000,
                description="🚗 Максимальная скорость: 340 км/ч\n🐎 Лошадиных сил: 710\n⏱ Разгон до 100: 2,9 сек",
            ),
            Property(
                name="Bugatti Chiron",
                price=700000000000,
                description="🚗 Максимальная скорость: 420 км/ч\n🐎 Лошадиных сил: 1500\n⏱ Разгон до 100: 2,4 сек",
            )
        ])
        await session.commit()

async def push_user(user_id: int):
    """РЕГИСТРИРУЕТ ПОЛЬЗОВАТЕЛЯ В БД"""
    async with async_session() as session:
        session.add(User(tg_id=user_id)) #пуш юзера
        await session.commit()
        session.add(Finance(user=await get_user_id(user_id)))#пуш финансов и тд
        session.add(Characteristic(user=await get_user_id(user_id)))
        session.add(Bank(user=await get_user_id(user_id)))
        for ore in await get_ores(): #проходит по всем рудам и добавляет в инвентарь
            session.add(Inventory(user=await get_user_id(user_id), ore = ore.id))
        await session.commit()


async def increanse(bit: int, user_id: int):
    """УВЕЛИЧИВАЕТ КОЛВО ДЕНЕГ НА ЗАДАННОЕ ЧИСЛО"""
    async with async_session() as session:
        await session.execute(update(Finance).values(money = Finance.money + bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()


async def deincreanse(bit: int, user_id: int):
    """УМЕНЬШАЕТ КОЛВО ДЕНЕГ НА ЗАДАННОЕ ЧИСЛО"""
    async with async_session() as session:
        await session.execute(update(Finance).values(money = Finance.money - bit).where(Finance.user == await get_user_id(user_id)))
        await session.commit()


async def increanse_ores(user_tg_id: int, name_ore: str, amount_ore: int):
    """УВЕЛИЧИВАЕТ КОЛВО РУДЫ НА ЗАДАННОЕ ЧИСЛО ПРИ ДОБЫЧЕ"""
    async with async_session() as session:
        user_id = await get_user_id(user_tg_id) #получение айди юзера по тг айди
        ore_id = (await get_ore(name_ore)).id #получение айди по имени руды
        await session.execute(update(Inventory).values(ammount_ore=Inventory.ammount_ore + amount_ore).where(Inventory.user == user_id, Inventory.ore == ore_id))
        await session.commit()


async def deincreanse_energy(user_id: int):
    """УМЕНЬШАЕТ ЭНЕРГИЮ ПРИ ДОБЫЧЕ РУДЫ НА ОДНУ"""
    async with async_session() as session:
        await session.execute(update(Characteristic).values(energy=Characteristic.energy - 1).where(Characteristic.user == await get_user_id(user_id)))
        await session.commit()


async def update_user_experience(user_id: int, experiences: int):
    """УВЕЛИЧЕНИЕ ОПЫТА ЮЗЕРА ПРИ ДОБЫЧЕ РУДЫ"""
    async with async_session() as session:
        await session.execute(update(Characteristic).values(experience=Characteristic.experience + experiences).where(Characteristic.user == await get_user_id(user_id)))
        await session.commit()

async def limit_user(user_id: int, amount: int):
    """УМЕНЬШЕНИЕ ЛИМИТА ПЕРЕВОДОВ С КАЖДЫМ ПЕРЕВОДОМ"""
    async with async_session() as session:
        await session.execute(update(User).values(limit=User.limit - amount).where(User.id == await get_user_id(user_id)))
        await session.commit()


async def reset_ammoint_ore(user_id: int, ore_name: int):
    """СБРАСЫВАЕТ КОЛВО РУДЫ ПРИ ПРОДАЖЕ"""
    async with async_session() as session:
        await session.execute(update(Inventory).values(ammount_ore = 0).where((Inventory.user == await get_user_id(user_id)) & (Inventory.ore == (await get_ore(ore_name)).id)))
        await session.commit()

        
async def push_transferred(user_id: int, amount):
    """ОБНОВЯЛЕТ КОЛВО ПЕРЕВОДОВ ЗА МЕСЯЦ"""
    async with async_session() as session:
        await session.execute(update(User).values(transferred=User.transferred + amount).where(User.id == await get_user_id(user_id)))
        await session.commit()


async def increanse_bank(tg_id: int, money_ammount: int):
    """
    Updates bank balance of a user with tg_id by adding money_ammount to it

    Args:
        tg_id (int): Telegram ID of the user
        money_ammount (int): Amount of money to add to the balance

    Returns:
        None
    """
    async with async_session() as session:
        # Update bank balance by adding money_ammount to it
        await session.execute(update(Bank)
                             .values(money_ammount=Bank.money_ammount + money_ammount)
                             .where(Bank.user == await get_user_id(tg_id)))
        # Commit the changes
        await session.commit()

async def deincreanse_bank(tg_id: int, money_ammount: int):
    """
    Decreases bank balance of a user with tg_id by subtracting money_ammount from it

    Args:
        tg_id (int): Telegram ID of the user
        money_ammount (int): Amount of money to subtract from the balance

    Returns:
        None
    """
    async with async_session() as session:
        # Update bank balance by subtracting money_ammount from it
        # We subtract money_ammount because we want to decrease the balance
        await session.execute(update(Bank)
                             .values(money_ammount=Bank.money_ammount - money_ammount)
                             # We update the Bank row where user if is equal to the user id
                             .where(Bank.user == await get_user_id(tg_id)))
        # Commit the changes
        await session.commit()
