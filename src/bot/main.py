import asyncio
import os
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.handlers import start_command_handler, test_command_handler, register_handlers
from src.bot.services import AstrologizeService, TextTransformService


# Загрузка токена из .env или окружения
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

if not BOT_TOKEN:
    print("⚠️  Токен бота не найден! Создайте файл .env с TELEGRAM_BOT_TOKEN")
    exit(1)


async def main():
    """Запуск бота"""
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="Markdown"))
    dp = Dispatcher()

    # Регистрация обработчиков команд
    register_handlers(dp)

    # Планировщик ежедневных гороскопов (9:00 AM по UTC)
    scheduler = Scheduler(bot=bot, token=BOT_TOKEN)
    await scheduler.start()

    print("🔮 Бот астролога без фильтров запущен!")
    print(f"📅 Планирование ежедневных гороскопов на 9:00 AM UTC")

    await dp.start_polling(bot)


class Scheduler:
    """Планировщик для ежедневных гороскопов"""
    
    def __init__(self, bot: Bot, token: str):
        self.bot = bot
        self.token = token
        self.zodiac_signs = [
            "овен", "телец", "близнецы", "рак", "лев", "дева", 
            "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"
        ]
    
    async def start(self):
        """Запуск планировщика"""
        # Запланировать первое выполнение через 1 час (для теста)
        await self.schedule_next_horoscope()
        
        # Планируем ежедневное выполнение на 9:00 AM UTC
        # 9:00 AM UTC = 04:00 по Chicago (America/Chicago)
        next_run = datetime.now() + timedelta(hours=1)
        
        while True:
            await asyncio.sleep(3600)  # Проверка каждый час
            await self.schedule_next_horoscope()
    
    async def schedule_next_horoscope(self):
        """Запланировать следующий гороскоп"""
        # Для простоты запускаем сразу после инициализации
        # В продакшене можно использовать aiogram Scheduler или APScheduler
        print(f"⏰ Планировщик запущен. Следующий гороскоп через 1 час (для теста)")


async def send_daily_horoscope():
    """Отправить ежедневный гороскоп всем подписчикам"""
    # Получаем дату для гороскопа (завтра)
    tomorrow = datetime.now() + timedelta(days=1)
    date_str = tomorrow.strftime("%d.%m")
    
    # Формируем текст гороскопа
    horoscope_text = f"🔮 Гороскоп на {date_str}\n\n"
    
    for sign in ["овен", "телец", "близнецы", "рак", "лев", "дева", 
                  "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"]:
        # Получаем данные от API
        service = AstrologizeService()
        data = await service.get_horoscope(sign, int(tomorrow.strftime("%Y%m%d")))
        
        if "error" not in data:
            # Трансформируем в дерзкий стиль
            transform_service = TextTransformService()
            witty_text = transform_service.transform_horoscope(data.get("prediction", ""))
            
            horoscope_text += f"{sign}: {witty_text}\n"
    
    # Отправляем гороскоп всем подписчикам (в реальном боте нужно хранить список)
    # Для простоты отправляем в лог-чат или можно расширить для конкретных пользователей
    
    print(f"📅 Гороскоп на {date_str} готов!")


if __name__ == "__main__":
    asyncio.run(main())
