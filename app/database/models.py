import enum
from datetime import datetime

from sqlalchemy import String, BigInteger, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Status(enum.Enum):
    usual = "Обычный"
    standart_vip = 'Standart VIP'
    gold_vip = "Gold VIP"
    platinum_vip = "Platinum VIP"
    administration = "Администратор"


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    status: Mapped[Status] = mapped_column(default=Status.usual)
    games_played: Mapped[int] = mapped_column(default=0)
    registered: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


class Finance(Base):
    __tablename__ = 'finances'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id))
    money: Mapped[int] = mapped_column(BigInteger, default=50000)
    bank: Mapped[int] = mapped_column(BigInteger, default=0)
    bitcoin: Mapped[int] = mapped_column(BigInteger, default=0)


class Characteristic(Base):
    __tablename__ = "characteristics"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id))
    energy: Mapped[int] = mapped_column(Integer, default=0)
    rating: Mapped[int] = mapped_column(BigInteger, default=0)
    experience: Mapped[int] = mapped_column(BigInteger, default=0)


class Ore(Base):
    __tablename__ = 'ores'

    id: Mapped[int] = mapped_column(primary_key=True)
    ore: Mapped[str] = mapped_column(String(20))
    experience: Mapped[int] = mapped_column(BigInteger)


class Inventory(Base):
    __tablename__ = 'inventory'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id))
    iron: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    gold: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    diamond: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    amethyst: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    aquamarine: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    emerald: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    matter: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    plasma: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    nickel: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    titanium: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    cobalt: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    ectoplasm: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)
    palladium: Mapped[int] = mapped_column(ForeignKey(Ore.id), default=0)


    # iron: Mapped[int] = mapped_column(BigInteger, default=0)
    # gold: Mapped[int] = mapped_column(BigInteger, default=0)
    # diamond: Mapped[int] = mapped_column(BigInteger, default=0)
    # amethyst: Mapped[int] = mapped_column(BigInteger, default=0)
    # aquamarine: Mapped[int] = mapped_column(BigInteger, default=0)
    # emerald: Mapped[int] = mapped_column(BigInteger, default=0)
    # matter: Mapped[int] = mapped_column(BigInteger, default=0)
    # plasma: Mapped[int] = mapped_column(BigInteger, default=0)
    # nickel: Mapped[int] = mapped_column(BigInteger, default=0)
    # titanium: Mapped[int] = mapped_column(BigInteger, default=0)
    # cobalt: Mapped[int] = mapped_column(BigInteger, default=0)
    # ectoplasm: Mapped[int] = mapped_column(BigInteger, default=0)
    # palladium: Mapped[int] = mapped_column(BigInteger, default=0)
#     ores = {
#     'железо': {'field': 'iron', 'experience': 0},
#     'золото': {'field': 'gold', 'experience': 500},
#     'алмаз': {'field': 'diamond', 'experience': 2000},
#     'аметист': {'field': 'amethyst', 'experience': 10000},
#     'аквамарин': {'field': 'aquamarine', 'experience': 25000},
#     'изумруд': {'field': 'emerald', 'experience': 60000},
#     'материя': {'field': 'matter', 'experience': 100000},
#     'плазма': {'field': 'plasma', 'experience': 500000},
#     'никель': {'field': 'nickel', 'experience': 950000},
#     'титан': {'field': 'titanium', 'experience': 5000000},
#     'кобальт': {'field': 'cobalt', 'experience': 20000000},
#     'эктоплазма': {'field': 'ectoplasm', 'experience': 10000000000}
# }
