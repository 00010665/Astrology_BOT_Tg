# 🔮 Astrology Bot - Астролог без фильтров

Дерзкий, ироничный и трэшовый бот с ежедневными гороскопами в стиле "чёрного юмора".

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/yourusername/Astrology.git
cd Astrology
```

### 2. Установите зависимости
```bash
pip install -r requirements.txt
```

### 3. Настройте окружение
Создайте файл `.env` в корне проекта:
```bash
cp .env.example .env
```

Откройте `.env` и вставьте токен бота от BotFather:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 4. Запустите бота
```bash
python src/bot/main.py
```

## 📅 Планирование гороскопов

Бот автоматически отправляет ежедневные гороскопы в **9:00 AM по UTC** (или можно настроить под ваш часовой пояс).

### Настройка времени отправки
Измените значение `SCHEDULE_HOUR` в конфигурации на нужное время.

## 🧪 Тестирование API

Проверьте работу API командой `/test` в боте:
```
/test
```

Бот вернёт пример данных для знака Овен на сегодня.

## 📡 API интеграция

Используется бесплатный API астрологии (open-source, не требует ключа):
- URL: `https://astrologize.ru/api/v1`
- Метод: GET `/horoscope/{sign}/{date}`
- Пример: `GET https://astrologize.ru/api/v1/horoscope/овен/20260807`

## 🛠️ Структура проекта

```
AstrologyBot/
├── src/
│   └── bot/
│       ├── __init__.py
│       ├── main.py          # Основной файл запуска
│       ├── handlers.py      # Обработчики команд (/start, /test)
│       └── services.py      # Сервисы (API астрологии, трансформация текста)
├── config/                  # Конфигурация
├── tests/                   # Тесты
├── .env.example             # Шаблон переменных окружения
├── requirements.txt         # Зависимости Python
└── README.md                # Эта файл
```

## 📝 Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Приветствие и инструкции по использованию |
| `/test` | Проверка работы API (вернёт пример гороскопа) |

## 🔐 Безопасность

- Никогда не делитесь токеном бота в публичных местах!
- Храните `.env` файл вне контроля Git (добавьте в `.gitignore`)
- Используйте только официальные токены от BotFather

## 🌐 Деплой на GitHub Pages / Heroku

### GitHub Actions CI/CD
1. Добавьте workflow `deploy.yml` в корень репозитория
2. Настройте секреты в GitHub Settings: `TELEGRAM_BOT_TOKEN`
3. Коммит изменений и деплой автоматически

### Heroku
```bash
heroku create your-bot-name
heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
git push heroku main
```

## 🐛 Отладка

Если бот не отвечает:
1. Проверьте токен в `.env`
2. Убедитесь, что API доступен (проверьте `/test`)
3. Посмотрите логи запуска бота

## 📜 Лицензия

MIT License - дерзкая и свободная!

---

**🔥 Сделано с любовью к чёрному юмору и трэшу!**
