import json
import os
from typing import List, Dict, Any, Optional
import re

class OKVEDSearcher:
    _instance = None
    _flat_data = []
    _code_to_item = {}
    
    # Обновлённый словарь СТРОГИХ соответствий
    STRICT_MATCH = {
        # IT и разработка - ТОЛЬКО IT!
        'разработка по': ['62.01'],
        'разработка программ': ['62.01'],
        'разработка мобильных': ['62.01'],
        'разработка приложений': ['62.01'],
        'программирование': ['62.01', '62.02'],
        'программист': ['62.01', '62.02'],
        'софт': ['62.01', '62.02'],
        'сайт': ['62.01', '62.02', '63.12'],
        'веб': ['62.01', '62.02', '63.12'],
        'приложение': ['62.01', '62.02'],
        'мобильное приложение': ['62.01'],
        'it': ['62.01', '62.02', '62.03', '63.11'],
        'информационные технологии': ['62.01', '62.02', '62.03', '63.11'],
        'компьютер': ['62.01', '62.02', '62.03', '95.11'],
        'тестирование по': ['62.02'],
        'тестировщик': ['62.02'],
        
        # Кофейня и общепит
        'кофейня': ['56.10'],
        'кофе': ['56.10', '47.29.35'],
        'ресторан': ['56.10'],
        'кафе': ['56.10'],
        'бар': ['56.30'],
        'столовая': ['56.29'],
        'общепит': ['56.10', '56.29'],
        'пекарня': ['10.71', '47.24'],
        'кондитерская': ['10.72', '47.24'],
        
        # Красота
        'маникюр': ['96.02'],
        'педикюр': ['96.02'],
        'ногти': ['96.02'],
        'парикмахер': ['96.02'],
        'барбершоп': ['96.02'],
        'косметолог': ['96.02', '86.90'],
        'брови': ['96.02'],
        'ресницы': ['96.02'],
        'салон красоты': ['96.02'],
        
        # Ремонт квартир - ТОЛЬКО строительный ремонт
        'ремонт квартир': ['43.3', '43.2'],
        'ремонт квартиры': ['43.3', '43.2'],
        'отделка квартир': ['43.3'],
        'отделка помещений': ['43.3'],
        'ремонт под ключ': ['43.3', '43.2'],
        'строительство домов': ['41.20'],
        'строительство коттеджей': ['41.20'],
        'сантехник': ['43.22'],
        'электрик': ['43.21'],
        'плиточник': ['43.33'],
        'штукатур': ['43.31'],
        'маляр': ['43.34'],
        
        # Автомойка и автосервис
        'автомойка': ['45.20'],
        'мойка авто': ['45.20'],
        'мойка машин': ['45.20'],
        'автосервис': ['45.20'],
        'сто': ['45.20'],
        'шиномонтаж': ['45.20'],
        'авторемонт': ['45.20'],
        'кузовной ремонт': ['45.20'],
        
        # Репетитор и обучение
        'репетитор': ['85.41'],
        'репетитор по английскому': ['85.41', '74.30'],
        'репетитор по языкам': ['85.41', '74.30'],
        'английский язык': ['85.41', '74.30'],
        'иностранные языки': ['85.41', '74.30'],
        'переводчик': ['74.30'],
        'курсы': ['85.41', '85.42'],
        'обучение': ['85.41', '85.42', '85.59'],
        'школа': ['85.41'],
        'тренинг': ['85.59'],
        
        # Доставка
        'доставка продуктов': ['53.20', '47.11', '47.29'],
        'доставка еды': ['56.10', '53.20'],
        'доставка на дом': ['53.20'],
        'курьер': ['53.20'],
        'курьерская доставка': ['53.20'],
        
        # Интернет-магазин
        'интернет магазин': ['47.91'],
        'интернет-магазин': ['47.91'],
        'онлайн магазин': ['47.91'],
        'маркетплейс': ['47.91'],
        'торговля через интернет': ['47.91'],
        'интернет торговля': ['47.91'],
        
        # Одежда
        'магазин одежды': ['47.71'],
        'одежда': ['47.71', '14.13', '14.19'],
        'интернет магазин одежды': ['47.91', '47.71'],
        
        # Торговля
        'магазин': ['47'],
        'розница': ['47'],
        'розничная торговля': ['47'],
        'опт': ['46'],
        'оптовая торговля': ['46'],
        'продажа': ['47', '46'],
        'торговля': ['47', '46'],
        
        # Гриль
        'гриль': ['56.10', '47.81', '10.13', '47.22'],
        'шашлык': ['56.10', '10.13'],
        'мангал': ['56.10', '47.81'],
        
        # Табак
        'сигареты': ['47.26', '46.35'],
        'табак': ['47.26', '46.35'],
        'табачные изделия': ['47.26', '46.35'],
        
        # Грузоперевозки
        'грузоперевозки': ['49.41'],
        'перевозка грузов': ['49.41'],
        'такси': ['49.32'],
        'логистика': ['52.10', '49.41'],
        
        # Клининг
        'уборка': ['81.21', '81.22'],
        'клининг': ['81.21', '81.22'],
        'химчистка': ['96.01'],
        
        # Фото и видео
        'фотограф': ['74.20'],
        'видеосъемка': ['74.20', '59.11'],
        'видеомонтаж': ['59.12'],
        
        # Дизайн
        'дизайн': ['74.10'],
        'дизайнер': ['74.10'],
        'графический дизайн': ['74.10'],
        'веб-дизайн': ['74.10', '62.01'],
        
        # Юридические и бухгалтерские
        'юрист': ['69.10'],
        'адвокат': ['69.10'],
        'бухгалтер': ['69.20'],
        'бухгалтерия': ['69.20'],
        'консалтинг': ['70.22'],
        
        # Реклама и маркетинг
        'реклама': ['73.11', '73.12'],
        'маркетинг': ['73.11', '73.12', '70.22'],
        'smm': ['73.11'],
        'таргет': ['73.11'],
        'продвижение': ['73.11'],
        
        # Недвижимость
        'риэлтор': ['68.31'],
        'недвижимость': ['68'],
        'аренда квартир': ['68.20'],
        
        # Медицина
        'врач': ['86.21', '86.22', '86.23'],
        'стоматолог': ['86.23'],
        'клиника': ['86.10', '86.21'],
        'массаж': ['86.90', '96.04'],
        
        # Спорт
        'фитнес': ['93.13'],
        'спортзал': ['93.13'],
        'йога': ['93.13'],
        'тренер': ['85.51', '93.13'],
        
        # Производство
        'производство мебели': ['31.01', '31.02', '31.09'],
        'мебель': ['31.01', '31.02', '31.09', '47.59'],
        'пошив одежды': ['14.13', '14.19'],
    }
    
    # Стоп-слова
    STOP_WORDS = {
        'хочу', 'могу', 'буду', 'стану', 'есть', 'быть', 'мой', 'твой', 'наш', 
        'ваш', 'этот', 'тот', 'такой', 'какой', 'очень', 'самый', 'более',
        'менее', 'весь', 'вся', 'все', 'для', 'без', 'при', 'под', 'над',
        'перед', 'через', 'между', 'среди', 'около', 'вокруг', 'мимо',
        'в', 'на', 'с', 'по', 'к', 'о', 'об', 'от', 'до', 'из', 'за',
        'и', 'а', 'но', 'или', 'либо', 'что', 'чтобы', 'как', 'когда',
        'где', 'куда', 'откуда', 'почему', 'зачем', 'сколько', 'который',
        'мне', 'меня', 'тебя', 'тебе', 'ему', 'ей', 'им', 'их', 'его',
        'она', 'они', 'мы', 'вы', 'ты', 'он', 'я', 'бы', 'же', 'ли',
        'уже', 'ещё', 'тоже', 'также', 'ведь', 'вот', 'там', 'тут', 'здесь',
        'открыть', 'открываю', 'планирую', 'создать', 'создаю', 'начать',
        'начинаю', 'заниматься', 'занимаюсь', 'делать', 'делаю'
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OKVEDSearcher, cls).__new__(cls)
            cls._instance._load_and_flatten()
        return cls._instance

    def _clean_query(self, query: str) -> List[str]:
        """Очищает запрос от стоп-слов."""
        words = re.findall(r'[а-яёa-z0-9]+', query.lower())
        meaningful = []
        for word in words:
            if word not in self.STOP_WORDS and len(word) >= 2:
                meaningful.append(word)
        return meaningful

    def _find_strict_matches(self, query: str) -> List[str]:
        """Находит строгие соответствия по словарю."""
        query_lower = query.lower()
        matched_codes = set()
        
        # Проверяем фразы из словаря (сначала длинные)
        sorted_phrases = sorted(self.STRICT_MATCH.keys(), key=len, reverse=True)
        for phrase in sorted_phrases:
            if phrase in query_lower:
                matched_codes.update(self.STRICT_MATCH[phrase])
        
        return list(matched_codes)

    def _flatten_tree(self, items: List[Dict], path: str = "") -> List[Dict]:
        """Рекурсивно превращает дерево в плоский список."""
        result = []
        for item in items:
            code = item.get('code', '')
            name = item.get('name', '')
            full_path = f"{path} > {name}" if path else name
            
            if 'items' in item and item['items']:
                result.extend(self._flatten_tree(item['items'], full_path))
            else:
                flat_item = {
                    'code': code,
                    'name': name,
                    'full_path': full_path
                }
                result.append(flat_item)
                self._code_to_item[code] = flat_item
        return result

    def _load_and_flatten(self):
        possible_paths = [
            os.path.join(os.path.dirname(__file__), 'OKVED', 'okved.json'),
            os.path.join(os.path.dirname(__file__), 'okved.json'),
        ]
        
        for file_path in possible_paths:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        raw_data = json.load(f)
                        self._flat_data = self._flatten_tree(raw_data)
                        print(f"OKVED loaded: {len(self._flat_data)} items")
                        return
                except Exception as e:
                    print(f"Error loading OKVED: {e}")
                    continue
        
        print("WARNING: OKVED data not found!")
        self._flat_data = []

    def search(self, query: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Умный поиск с приоритетом строгих соответствий."""
        if not query or len(query) < 2:
            return []
        
        query_lower = query.lower()
        clean_words = self._clean_query(query_lower)
        
        if not clean_words:
            return []
        
        strict_codes = self._find_strict_matches(query_lower)
        results = []
        seen_codes = set()
        
        # 1. СТРОГИЕ СООТВЕТСТВИЯ
        if strict_codes:
            for item in self._flat_data:
                item_code = item['code']
                for prefix in strict_codes:
                    if item_code.startswith(prefix) and len(item_code) <= len(prefix) + 5:
                        if item_code not in seen_codes:
                            seen_codes.add(item_code)
                            score = 1000
                            
                            name_lower = item['name'].lower()
                            for word in clean_words:
                                if word in name_lower:
                                    score += 50
                            
                            results.append({
                                'code': item_code,
                                'name': item['name'],
                                'full_path': item['full_path'],
                                'score': score
                            })
        
        # 2. ПОИСК ПО КЛЮЧЕВЫМ СЛОВАМ (только если строгих мало)
        if len(results) < 5:
            for item in self._flat_data:
                if item['code'] in seen_codes:
                    continue
                    
                name_lower = item['name'].lower()
                score = 0
                words_matched = 0
                
                for word in clean_words:
                    if word in name_lower:
                        words_matched += 1
                        score += 30
                
                if words_matched >= 2:
                    score += 200
                elif words_matched == 1 and len(clean_words) == 1:
                    score += 100
                
                # Фильтр - не показывать ремонт обуви/часов при запросе "ремонт квартир"
                if 'ремонт квартир' in query_lower or 'отделка' in query_lower:
                    if 'квартир' not in name_lower and 'отделк' not in name_lower and 'строительн' not in name_lower and 'штукатур' not in name_lower and 'маляр' not in name_lower and 'плиточн' not in name_lower and 'сантехни' not in name_lower and 'электромонтаж' not in name_lower:
                        continue
                
                # Фильтр для IT - только компьютерное
                if 'разработка' in query_lower and ('приложени' in query_lower or 'по' in query_lower or 'мобильн' in query_lower):
                    if 'компьютерн' not in name_lower and 'программн' not in name_lower:
                        continue
                
                if score >= 60:
                    results.append({
                        'code': item['code'],
                        'name': item['name'],
                        'full_path': item['full_path'],
                        'score': score
                    })
        
        # Сортировка
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # Убираем дубликаты
        filtered = []
        seen = set()
        for r in results:
            if r['code'] not in seen:
                filtered.append(r)
                seen.add(r['code'])
        
        return filtered[:limit]

    def get_by_code(self, code: str) -> Optional[Dict]:
        return self._code_to_item.get(code)


searcher = OKVEDSearcher()