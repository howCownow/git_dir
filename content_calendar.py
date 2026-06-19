# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ContentCalendar
import json, datetime as dt
from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class Author:
    id: int
    name: str

@dataclass
class Channel:
    id: int
    name: str

@dataclass
class PostStatus:
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"

@dataclass
class ContentPost:
    id: int
    title: str
    content: str
    channel_id: int
    author_id: int
    deadline: dt.datetime
    status: PostStatus

def init_calendar_db(db_path: str = "calendar.db.json") -> Dict[str, List]:
    posts: List[ContentPost] = [
        ContentPost(1, "Введение в Python", "Базовые типы данных...", 1, 2, dt.datetime.now() + dt.timedelta(days=1), PostStatus.SCHEDULED),
        ContentPost(2, "ООП на практике", "Классы и наследование...", 1, 3, dt.datetime.now() + dt.timedelta(days=5), PostStatus.DRAFT),
    ]
    channels: List[Channel] = [
        Channel(1, "Tech News"),
        Channel(2, "Python Tips"),
    ]
    authors: List[Author] = [
        Author(2, "Alice Dev"),
        Author(3, "Bob Senior"),
    ]
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump({"posts": posts, "channels": channels, "authors": authors}, f, ensure_ascii=False)
    return {"posts": posts, "channels": channels, "authors": authors}

def load_calendar() -> Dict[str, List]:
    try:
        with open("calendar.db.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        init_calendar_db()
        return {"posts": [], "channels": [], "authors": []}

if __name__ == "__main__":
    db = load_calendar()
    print(f"Загружено {len(db['posts'])} постов, {len(db['channels'])} каналов и {len(db['authors'])} авторов.")
