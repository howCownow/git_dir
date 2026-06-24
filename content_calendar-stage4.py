# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ContentCalendar
def edit_post(post_id: int, updates: dict) -> Optional[Post]:
    if post_id not in posts_by_id:
        raise ValueError(f"Запись с ID {post_id} не найдена")
    
    existing = posts_by_id[post_id]
    for key, value in updates.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
        else:
            raise AttributeError(f"Атрибут '{key}' недоступен для редактирования записи {post_id}")
    
    return existing
