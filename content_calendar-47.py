# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ContentCalendar
def demo():
    """Показывает основной пользовательский сценарий календаря публикаций."""
    print("Добро пожаловать в ContentCalendar!")
    print("=" * 40)

    # Создаём пару каналов
    channels = {
        "Telegram": {"subscribers": 1200},
        "YouTube": {"subscribers": 5000},
    }
    print(f"Каналы: {', '.join(channels)}")

    # Создаём авторов
    authors = {
        "Алексей": {"level": "Senior"},
        "Мария": {"level": "Junior"},
    }
    print(f"Авторы: {', '.join(authors)}")

    # Создаём материалы с разными статусами
    materials = []
    materials.append({
        "title": "Введение в AI",
        "channel": "Telegram",
        "author": "Алексей",
        "deadline": "2024-06-15",
        "status": "published",
    })
    materials.append({
        "title": "Python для начинающих",
        "channel": "YouTube",
        "author": "Мария",
        "deadline": "2024-07-01",
        "status": "draft",
    })
    materials.append({
        "title": "Машинное обучение",
        "channel": "Telegram",
        "author": "Алексей",
        "deadline": "2024-08-10",
        "status": "planned",
    })
    print(f"\nМатериалы:\n")
    for m in materials:
        print(f"  • {m['title']} [{m['status']}] — канал: {m['channel']}, автор: {m['author']}, дедлайн: {m['deadline']}")

    # Фильтр: только опубликованные
    published = [m for m in materials if m["status"] == "published"]
    print(f"\nОпубликовано: {len(published)} материал(ов)")
    for m in published:
        print(f"  → {m['title']}")

    # Фильтр: материалы с истекающим дедлайном (ближе 30 дней)
    from datetime import datetime, timedelta
    today = datetime.now().date()
    upcoming = [m for m in materials if m["deadline"] <= (today + timedelta(days=30))]
    print(f"\nМатериалы с дедлайном в ближайшие 30 дней: {len(upcoming)}")
    for m in upcoming:
        print(f"  ⚠️ {m['title']} — дедлайн: {m['deadline']}")

    print("\nДемо завершено. Спасибо за использование ContentCalendar!")
