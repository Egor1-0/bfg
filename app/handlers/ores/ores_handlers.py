import random
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import or_f

from app.filters import LenInputData, DateValue
from app.database.queries import increanse, deincreanse, get_user_inventory
from app.filters import CheckEnergy, CheckOres

ores_router = Router()

# ores_router.message.filter(CheckEnergy(), CheckOres())

ores_router.message.filter(F.text.lower().startswith('копать'))


@ores_router.message(CheckEnergy(), CheckOres())
async def ores_get(message: Message):
    random_ores = random.randint(1, 100)
