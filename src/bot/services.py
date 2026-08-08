import aiohttp
import random


class AstrologizeService:
    """Сервис для получения астрологических данных через бесплатный API"""
    
    ZODIAC_SIGNS = [
        "овен", "телец", "близнецы", "рак", "лев", "дева", 
        "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"
    ]
    
    def __init__(self, api_url="https://astrologize.ru/api/v1"):
        self.api_url = api_url
    
    async def get_horoscope(self, sign: str, date: int) -> dict:
        """Получить гороскоп для знака зодиака на указанную дату"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.api_url}/horoscope/{sign}/{date}",
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        return {"error": f"HTTP {response.status}"}
        except Exception as e:
            print(f"Ошибка при получении гороскопа: {e}")
            return {"error": str(e)}


class TextTransformService:
    """Сервис для трансформации текста в стиле 'Астролог без фильтров'"""
    
    def __init__(self):
        self.emojis = ["🔪", "💐", "🍓", "🤍", "❤️", "😓", "🌷"]
    
    def transform_horoscope(self, raw_text: str) -> list:
        """
        Трансформировать сырой текст гороскопа в стиль 'Астролог без фильтров'
        
        Стиль: дерзкий, ироничный, трэшовый, абсурдный юмор
        Формат: короткие фразы (2-8 слов), чёрный юмор, провокация
        """
        # Если текст уже короткий и дерзкий - оставляем как есть
        if len(raw_text.split()) <= 8 and self._is_witty(raw_text):
            return [raw_text]
        
        # Для длинных текстов создаём короткие дерзкие фразы
        short_phrases = self._make_short_witty(raw_text)
        
        # Добавляем случайный эмодзи
        emoji = random.choice(self.emojis)
        
        return short_phrases
    
    def _is_witty(self, text: str) -> bool:
        """Проверить, является ли текст коротким и дерзким"""
        words = text.split()
        # Короткие фразы (2-8 слов) с провокационным содержанием
        if len(words) < 2 or len(words) > 8:
            return False
        
        # Проверяем на провокационный/дерзкий контент
        provocative_words = [
            "бомж", "порчи", "секс", "наркотик", "мышьяк", 
            "вебкамщица", "застрелиться", "набухайся", "трусы",
            "касса", "манипулятор", "сплетница", "взять", "скинь"
        ]
        
        text_lower = text.lower()
        return any(word in text_lower for word in provocative_words)
    
    def _make_short_witty(self, raw_text: str) -> list:
        """Создать короткие дерзкие фразы из сырого текста"""
        # Извлекаем ключевые идеи и перефразируем в дерзком стиле
        ideas = raw_text.lower().split(".")
        
        witty_phrases = []
        for idea in ideas:
            if len(idea.strip()) > 10:
                # Берём первые несколько слов или создаём короткую фразу
                words = idea.strip().split()[:6]
                phrase = " ".join(words)
                if len(phrase.split()) <= 8:
                    witty_phrases.append(phrase)
        
        return witty_phrases
