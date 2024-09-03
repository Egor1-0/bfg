import enum
from datetime import datetime

from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Status(enum.Enum):
    usual = "ОбычныйЫ"
    standart_vip = 'Standart VIP'
    gold_vip = "Gold VIP"
    platinum_vip = "Platinum VIP"
    administration = "Администратор"

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    status: Mapped[Status] = mapped_column(default=Status.usual)
    money: Mapped[int] = mapped_column(BigInteger, default=50000)
    games_played: Mapped[int] = mapped_column(default=0)
    registered: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())