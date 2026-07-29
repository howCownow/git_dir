# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ContentCalendar
def reset_demo_data():
    """Заполняет все структуры проекта тестовыми данными, затем сбрасывает их."""
    import random
    channels = ["TechNews", "DesignDaily", "CodeCraft"]
    authors = [f"Author_{i}" for i in range(1, 20)]
    statuses = ["Draft", "Scheduled", "Published", "Cancelled"]
    
    # Сброс каналов
    channel_store.clear()
    for ch in channels:
        channel_store[ch] = {"name": ch, "created_at": "2024-01-01", "post_count": 0}
    
    # Сброс авторов
    author_store.clear()
    for a in authors:
        author_store[a] = {"name": a, "email": f"{a.lower()}@example.com"}
    
    # Сброс статусов
    status_store.clear()
    for s in statuses:
        status_store[s] = {"label": s, "color": random.choice(["#00ff00", "#ffff00", "#ffffff", "#ff0000"])}
    
    # Сброс публикаций
    post_store.clear()
    today = datetime.now().date()
    for i in range(1, 51):
        date_offset = random.randint(-7, 30)
        deadline = (today + timedelta(days=date_offset)).isoformat() if date_offset >= 0 else today.isoformat()
        status = random.choice(statuses)
        post_store[f"post_{i:03d}"] = {
            "title": f"Article #{i}",
            "channel": random.choice(channels),
            "author": random.choice(authors),
            "deadline": deadline,
            "status": status,
            "created_at": (today - timedelta(days=random.randint(1, 60))).isoformat(),
            "content": f"Lorem ipsum dolor sit amet, section {i}."
        }

def clear_all_state():
    """Полностью очищает все хранилища проекта."""
    channel_store.clear()
    author_store.clear()
    status_store.clear()
    post_store.clear()
