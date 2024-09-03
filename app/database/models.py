from datetime import datetime

from sqlalchemy import String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    money: Mapped[int] = mapped_column(BigInteger, default=50000)
    games_played: Mapped[int] = mapped_column(default=0)
    registered: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())