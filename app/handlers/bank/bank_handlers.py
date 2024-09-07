from aiogram import Router, F
from aiogram.types import Message

from app.database.queries import increanse_bank, deincreanse, increanse, deincreanse_bank, get_bank
from app.filters import CheckBankMoney

bank_router = Router()


bank_router.message.filter(F.text.lower().startswith('банк'))

bank_router.message.filter(CheckBankMoney())
# bank_router.message.filter(CheckLimit())

@bank_router.message(F.text.lower().contains('положить'))
async def error(message: Message):
    await increanse_bank(message.from_user.id, int(message.text.split(" ")[2]))
    await deincreanse(int(message.text.split(" ")[2]), message.from_user.id)
    await message.answer("Положено в банк")


@bank_router.message(F.text.lower().contains('снять'))
async def error(message: Message):
    bank_comission = (await get_bank(message.from_user.id)).comission 
    await deincreanse_bank(message.from_user.id, int(message.text.split(" ")[2]))
    await increanse(int(message.text.split(" ")[2]) * (100 - bank_comission) / 100, 
                    message.from_user.id)
    await message.answer("Положено в вам на счет")


# @bank_router.message(LenInputData(), DateValue())
# async def give_money_handler(message: Message):
#     if message.reply_to_message is None: #дать деньги можно только ответив на сообщение человека, с которым хотите поделиться
#         await message.answer("Чтобы передать деньги, нужно ответить на сообщение пользователя 😞")
#         return
#     user = await get_user(message.from_user.id)
#     amount = int(message.text.split(" ")[1])
#     if user.limit >= amount: #проверка, не перевел ли человек больше денег чем может
#         await increanse(amount, message.reply_to_message.from_user.id)
#         await deincreanse(amount, message.from_user.id)
#         await limit_user(message.from_user.id, amount)
#         await push_transferred(message.from_user.id, amount)
#         await message.reply_to_message.answer(
#             f"✅ | {amount} успешно передано пользователю {message.reply_to_message.from_user.full_name}!"
#         )
#     else:
#         await message.answer(f"⚠️ | Ваш лимит : {user.limit}")
