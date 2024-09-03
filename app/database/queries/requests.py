from sqlalchemy import select

from app.database.models import User
from app.database.session import async_session

async def get_user(user_id: int):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == user_id))