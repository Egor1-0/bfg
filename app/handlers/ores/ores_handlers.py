import random
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f

from app.filters import LenInputData, DateValue
from app.database.queries import increanse, deincreanse
from app.middlewares import CheckEnergy

ores_router = Router()

ores_router.message.outer_middleware(CheckEnergy())

ores_router.message.filter(F.text.lower().startswith('копать'))


