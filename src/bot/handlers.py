from aiogram import types, Dispatcher
from aiogram.filters import Command


async def start_command_handler(event: types.Message):
    """Обработчик команды /start"""
    welcome_text = (
        "🔮 Привет! Я — Астролог без фильтров!\n\n"
        "Я буду присылать тебе дерзкие, ироничные и трэшовые гороскопы каждый день в 9:00 утра.\n\n"
        "Что делать:\n"
        "1. Нажми /start чтобы активировать бота\n"
        "2. Жди утренние прогнозы (9:00 AM)\n"
        "3. Получай чёрный юмор и провокационные предсказания\n\n"
        "🔥 Твой астролог без фильтров готов! 🔥\n\n"
        "P.S. Не жди серьёзных советов — здесь только дерзкий треш-юмор 😈"
    )
    await event.answer(welcome_text, parse_mode="Markdown")


async def test_command_handler(event: types.Message):
    """Обработчик команды /test для проверки API"""
    from src.bot.services import AstrologizeService
    
    service = AstrologizeService()
    result = await service.get_horoscope("овен", 7)  # Сегодня 7 августа
    
    if "error" in result:
        await event.answer(f"Ошибка API: {result['error']}", parse_mode="Markdown")
    else:
        await event.answer(f"API работает! Получил данные для овена на сегодня:\n{result}", parse_mode="Markdown")


def register_handlers(dp: Dispatcher):
    """Регистрация обработчиков команд"""
    dp.message_handler(commands=["start"])(start_command_handler)
    dp.message_handler(commands=["test"])(test_command_handler)
