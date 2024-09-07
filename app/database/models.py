import enum
from datetime import datetime

from sqlalchemy import String, BigInteger, DateTime, Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Status(enum.Enum):
    """ТИП ДАННЫХ ДЛЯ СТАТУСА. ПОТОМ НЕ БУДЕТ СУЩЕСТВОВАТЬ"""
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
    limit: Mapped[int] = mapped_column(BigInteger, default=300000000000000) #лимит переводов
    transferred: Mapped[int] = mapped_column(BigInteger, default=0) #сколько перевел

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
    energy: Mapped[int] = mapped_column(Integer, default=10) #для добычи руды
    rating: Mapped[int] = mapped_column(BigInteger, default=0)
    experience: Mapped[int] = mapped_column(BigInteger, default=0) #для добычи определенной руды


class Ore(Base):
    __tablename__ = 'ores'

    id: Mapped[int] = mapped_column(primary_key=True)
    ore: Mapped[str] = mapped_column(String(20))
    experience: Mapped[int] = mapped_column(BigInteger) #необходимый для копания опыт
    price: Mapped[int] = mapped_column(BigInteger) #цена за продажу


class Inventory(Base):
    __tablename__ = 'inventory'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id))
    ore: Mapped[str] = mapped_column(String(20), ForeignKey(Ore.id)) #айди руды
    ammount_ore: Mapped[int] = mapped_column(BigInteger, default=0) #колво этой руды у пользователя

class Property(Base):
    """
    Model for possible property

    :param id: unique identifier
    :param name: property name
    :param price: property price
    :param description: property description
    :param photo: link to property photo
    """
    __tablename__ = 'properties'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(35))  # name
    price: Mapped[int] = mapped_column(BigInteger)  # price
    description: Mapped[str] = mapped_column(String(255))  # description
    photo: Mapped[str] = mapped_column(String(100), default=None)  # photo link