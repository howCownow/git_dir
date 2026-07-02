# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ContentCalendar
import json, sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional

def load_initial_data(json_string: str) -> None:
    """Загружает начальные данные из JSON-строки и заполняет глобальную структуру."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")

        # Инициализация структур данных
        global channels, authors, posts, calendar_view
        
        channels = {item['id']: item for item in data.get('channels', [])}
        authors = {item['id']: item for item in data.get('authors', [])}
        
        posts_data = data.get('posts', [])
        posts: List[Dict] = []
        calendar_view: Dict[str, List[Dict]] = {}

        # Обработка постов и построение календаря
        for post in posts_data:
            if not isinstance(post, dict):
                continue
            
            status_map = {
                'draft': 'Черновик',
                'scheduled': 'Запланировано',
                'published': 'Опубликовано',
                'rejected': 'Отклонено'
            }
            
            post['status_display'] = status_map.get(post.get('status'), 'Неизвестно')
            posts.append(post)

            # Группировка по дате публикации (YYYY-MM-DD)
            pub_date_str = post.get('publish_at', '')
            if pub_date_str:
                try:
                    pub_date = datetime.strptime(pub_date_str, '%Y-%m-%d').date()
                    key = f"{pub_date.year}-{pub_date.month:02d}"
                    calendar_view.setdefault(key, []).append(post)
                except ValueError:
                    pass

        # Сортировка постов по дате публикации и статусу (публикации первыми)
        posts.sort(key=lambda p: (p.get('publish_at', ''), 1 if p.get('status') == 'published' else 0))
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
