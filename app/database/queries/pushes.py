from sqlalchemy import select

from app.database.models import User
from app.database.session import async_session

async def push_user(user_id: int):
    async with async_session() as session:
        session.add(User(tg_id=user_id))
        await session.commit()
