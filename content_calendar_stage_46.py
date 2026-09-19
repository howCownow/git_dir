# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ContentCalendar
MIGRATION_V0 = {
    "channels": [
        {"id": 1, "name": "Tech News", "description": "Latest tech industry news"},
        {"id": 2, "name": "Gaming", "description": "Video game updates and reviews"},
    ],
    "authors": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    ],
    "statuses": [
        {"id": 1, "name": "Draft", "color": "#999999"},
        {"id": 2, "name": "In Review", "color": "#FFA726"},
        {"id": 3, "name": "Published", "color": "#4CAF50"},
        {"id": 4, "name": "Archived", "color": "#9E9E9E"},
    ],
    "articles": [
        {
            "id": 1,
            "title": "Python 3.12 Released",
            "channel_id": 1,
            "author_id": 1,
            "deadline": "2024-03-15",
            "status_id": 3,
            "content": "Python 3.12 brings performance improvements...",
            "published_at": "2024-03-15",
        },
        {
            "id": 2,
            "title": "New Game Engine Announced",
            "channel_id": 2,
            "author_id": 2,
            "deadline": "2024-03-20",
            "status_id": 2,
            "content": "A revolutionary new game engine...",
            "published_at": None,
        },
        {
            "id": 3,
            "title": "Open Source Tools Roundup",
            "channel_id": 1,
            "author_id": 3,
            "deadline": "2024-04-01",
            "status_id": 1,
            "content": "Best open source tools for developers...",
            "published_at": None,
        },
    ],
}
