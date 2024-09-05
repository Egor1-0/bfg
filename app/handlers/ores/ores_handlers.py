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

ores = {
    'железо': {'field': 'iron', 'experience': 0},
    'золото': {'field': 'gold', 'experience': 500},
    'алмаз': {'field': 'diamond', 'experience': 2000},
    'аметист': {'field': 'amethyst', 'experience': 10000},
    'аквамарин': {'field': 'aquamarine', 'experience': 25000},
    'изумруд': {'field': 'emerald', 'experience': 60000},
    'материя': {'field': 'matter', 'experience': 100000},
    'плазма': {'field': 'plasma', 'experience': 500000},
    'никель': {'field': 'nickel', 'experience': 950000},
    'титан': {'field': 'titanium', 'experience': 5000000},
    'кобальт': {'field': 'cobalt', 'experience': 20000000},
    'эктоплазма': {'field': 'ectoplasm', 'experience': 10000000000}
}

