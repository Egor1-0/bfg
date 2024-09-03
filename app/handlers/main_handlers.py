from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.database.queries import push_user, get_user
from app.keyboards.kb_main_handlers import main, help_main, back_help

main_router = Router()

@main_router.message(CommandStart())
async def start(message: Message):
    stickers = 'CAACAgUAAxkBAALea2bXYdgBVHgOum6pvnaezKo6Z68TAAIsBAACeb6RVXoJmzEnw-S5NQQ'
    await message.bot.send_sticker(chat_id=message.chat.id, sticker=stickers)
    await message.answer(f"🤖 Добро пожаловать на борт, {message.from_user.first_name} ! Меня зовут BFG, твой верный игровой бот.\n\n"
                         f" 🎮 У меня есть множество интересных команд и игр, чтобы\n"
                         f" скрасить твоё время, будь ты один или в компании друзей!\n"
                         f"(Кстати, вместе всегда веселее) 💙\n"
                         f"🔍 Познакомиться со всеми моими возможностями ты\n"
                         f" можешь, введя команду «помощь».", reply_markup=main)
    if not (await get_user(message.from_user.id)):
        await push_user(message.from_user.id)

@main_router.message(Command("help"))
@main_router.message(F.text.lower() == "помощь")
async def help(message: Message):
    await message.answer(f"{message.from_user.first_name}, выберите категорию:"
                         f"\n 1️⃣ Основное"
                         f"\n 2️⃣ Игры"
                         f"\n 3️⃣ Развлекательное"
                         f"\n 4️⃣ Кланы"
                         f"\n\n 💬 Так же у нас есть", reply_markup=help_main)

@main_router.callback_query(F.data == 'base')
async def base_command(callback: CallbackQuery):
    await callback.message.edit_text(
        "💡 Разное:\n"
        "📒 Профиль\n"
        "💫 Мой лимит\n"
        "👑 Рейтинг\n"
        "👑 Продать рейтинг\n"
        "⚡️ Энергия\n"
        "⛏ Шахта\n"
        "🚗 Машины\n"
        "📱 Телефоны\n"
        "✈️ Самолёты\n"
        "🛥 Яхты\n"
        "🚁 Вертолёты\n"
        "🏠 Дома\n"
        "💸 Б/Баланс\n"
        "📦 Инвентарь\n"
        "📊 Курс руды\n"
        "🏢 Ограбить мэрию\n"
        "💰 Банк [положить/снять] [сумма/всё]\n"
        "💵 Депозит [положить/снять] [сумма/всё]\n"
        "🤝 Дать [сумма]\n"
        "🌐 Биткоин курс/купить/продать [кол-во]\n"
        "⚱️ Биткоины\n"
        "💈 Ежедневный бонус\n"
        "💷 Казна\n"
        "💢 Сменить ник [новый ник]\n"
        "👨 Мой ник - узнать ник\n"
        "⚖️ РП Команды - узнать РП команды\n"
        "🏆 Мой статус\n"
        "🔱 Статусы️\n"
        "💭 !Беседа - беседа бота", reply_markup=back_help
    )

@main_router.callback_query(F.data == 'game')
async def game_command(callback: CallbackQuery):
    await callback.message.edit_text(
        "🚀 Игры:\n"
        "🎮 Спин [ставка]\n"
        "🎲 Кубик [число] [ставка]\n"
        "🏀 Баскетбол [ставка]\n"
        "🎯 Дартс [ставка]\n"
        "🎳️ Боулинг [ставка]\n"
        "📉 Трейд [вверх/вниз] [ставка]\n"
        "🎰 Казино [ставка]", reply_markup=back_help
    )

@main_router.callback_query(F.data == 'entertainment')
async def entertainment_command(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎉 Развлечения:\n"
        "🔮 Шар [фраза]\n"
        "💬 Выбери [фраза] или [фраза2]\n"
        "📊 Инфа [фраза]\n\n"

        "💒 Браки:\n"
        "💖 Свадьба [ID пользователя]\n"
        "💖 Развод\n"
        "💌 Мой брак\n\n"

        "📦 Кейсы:\n"
        "🛒 Купить кейс [номер] [количество]\n"
        "🔐 Открыть кейс [номер] [количество]\n\n"

        "🗄 Бизнес:\n"
        "💰 Мой бизнес/бизнес\n"
        "💸 Продать бизнес (временно недоступно)\n\n"

        "🏭 Генератор:\n"
        "🏭 Мой генератор/генератор\n"
        "💷 Продать генератор (временно недоступно)\n\n"

        "🧰 Майнинг ферма:\n"
        "🔋 Моя ферма/ферма\n"
        "💰 Продать ферму (временно недоступно)\n\n"

        "⚠️ Карьер:\n"
        "🏗 Мой карьер/карьер\n"
        "💰 Продать карьер (временно недоступно)\n\n"

        "🏡 Денежное дерево:\n"
        "🌳 Моё дерево\n"
        "💰 Продать участок (временно недоступно)\n\n"

        "🌳 Сады:\n"
        "🪧 Мой сад/сад\n"
        "💰 Продать сад (временно недоступно)\n"
        "💦 Сад полить\n"
        "🍸 Зелья\n"
        "🔮 Создать зелье [номер]", reply_markup=back_help
    )

@main_router.callback_query(F.data == 'clan')
async def clan_command(callback: CallbackQuery):
    await callback.message.edit_text(
        "🗂 **Общие команды**:\n"
        "💡 Мой клан - общая информация\n"
        "🏆 Клан топ - общий рейтинг кланов\n"
        "✅ Клан пригласить [ID] - пригласить игрока в клан\n"
        "🙋‍♂ Клан вступить [ID клана] - вступить в клан\n"
        "📛 Клан исключить [ID] - исключает игрока\n"
        "🚷 Клан выйти - выйти из клана\n"
        "💰 Клан казна - состояние казны\n"
        "💵 Клан казна [сумма] - положить деньги в казну\n\n"

        "⚙️ **Создание и настройка кланов**:\n"
        "⚙️ Клан создать [название] - стоимость 250.000.000.000$\n"
        "⤴️ Клан настройки - информация о настройках\n"
        "📥 Клан настройки приглашение [1-4]\n"
        "💢 Клан настройки кик [1-4]\n"
        "🔰 Клан настройки ранги [1-4]\n"
        "💵 Клан настройки казна [1-4]\n"
        "💰 Клан настройки ограбление [1-4]\n"
        "⚔️ Клан настройки война [1-4]\n"
        "✏️ Клан настройки название [1-4]\n"
        "🔐 Клан настройки тип [закрытый/открытый]\n\n"

        "🔎 **Управление кланом**:\n"
        "✏️ Клан название [название] - изменить название клана\n"
        "⤴️ Клан повысить [ID] - повысить игрока\n"
        "⤵️ Клан понизить [ID] - понизить игрока\n"
        "👑 Клан передать [ID] - передать главу клана\n"
        "📛 Клан удалить - удалить клан\n\n"

        "🛡 **Клановые захваты**:\n"
        "👮‍♀ Клан ограбление (недоступно) - ограбление казны штата\n\n"

        "📜 Будьте осторожнее с командами повышения и понижения, "
        "повысив игрока до определенного статуса, он сможет изменять название клана и управлять им.", reply_markup=back_help
    )

@main_router.callback_query(F.data == 'back')
async def back_help_command(callback: CallbackQuery):
    await callback.message.edit_text(f"{callback.from_user.first_name}, выберите категорию:"
                         f"\n 1️⃣ Основное"
                         f"\n 2️⃣ Игры"
                         f"\n 3️⃣ Развлекательное"
                         f"\n 4️⃣ Кланы"
                         f"\n\n 💬 Так же у нас есть", reply_markup=help_main)

