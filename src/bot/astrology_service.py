import requests
from typing import Dict, List


class AstrologyService:
    """Сервис для получения астрологических данных"""
    
    # Бесплатный open-source API астрологии
    ASTROLOGIZE_API_URL = "https://astrologize.ru/api/v1/forecast"
    
    ZODIAC_SIGNS = [
        "ovnen",  # овен
        "telec",  # телец
        "bliznetcy",  # близнецы
        "rak",  # рак
        "lev",  # лев
        "deva",  # дева
        "vesy",  # весы
        "skorpion",  # скорпион
        "strelec",  # стрелец
        "kozerog",  # козерог
        "vodoley",  # водолей
        "ryby"  # рыбы
    ]
    
    def get_forecast(self, date: str) -> Dict:
        """
        Получить прогноз на дату
        
        Args:
            date: Дата в формате YYYY-MM-DD
            
        Returns:
            Словарь с прогнозами для всех знаков зодиака
        """
        try:
            params = {
                "date": date,
                "lang": "ru"
            }
            
            response = requests.get(
                self.ASTROLOGIZE_API_URL,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "success": True,
                    "data": data
                }
            else:
                return {
                    "success": False,
                    "error": f"API returned status {response.status_code}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_sign_forecast(self, sign_name: str, date: str) -> Dict:
        """
        Получить прогноз для конкретного знака зодиака
        
        Args:
            sign_name: Название знака (на русском)
            date: Дата в формате YYYY-MM-DD
            
        Returns:
            Словарь с прогнозом для указанного знака
        """
        try:
            params = {
                "date": date,
                "lang": "ru"
            }
            
            response = requests.get(
                self.ASTROLOGIZE_API_URL,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Ищем прогноз для указанного знака
                forecast = None
                for sign_data in data.get("forecasts", []):
                    if self._sign_match(sign_name, sign_data.get("name", "")):
                        forecast = sign_data
                        break
                
                return {
                    "success": True,
                    "data": forecast or {"text": f"Прогноз для {sign_name} не найден"}
                }
            else:
                return {
                    "success": False,
                    "error": f"API returned status {response.status_code}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _sign_match(self, user_sign: str, api_sign: str) -> bool:
        """Сопоставление названий знаков"""
        # Нормализация названий
        user_normalized = user_sign.lower().strip()
        api_normalized = api_sign.lower().strip()
        
        # Мappings для разных вариантов названий
        mappings = {
            "овен": ["ovnen", "aries"],
            "телец": ["telec", "taurus"],
            "близнецы": ["bliznetcy", "gemini"],
            "рак": ["rak", "cancer"],
            "лев": ["lev", "leo"],
            "дева": ["deva", "virgo"],
            "весы": ["vesy", "libra"],
            "скорпион": ["skorpion", "scorpio"],
            "стрелец": ["strelec", "sagittarius"],
            "козерог": ["kozerog", "capricorn"],
            "водолей": ["vodoley", "aquarius"],
            "рыбы": ["ryby", "pisces"]
        }
        
        if user_normalized in mappings:
            return api_normalized in mappings[user_normalized]
        
        return user_normalized == api_normalized
