import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from dotenv import load_dotenv

from app.database.models import *
from app.database.base import Base

load_dotenv()

engine = create_async_engine(os.getenv("URL"))

async_session = async_sessionmaker(engine)

async def create_session():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)