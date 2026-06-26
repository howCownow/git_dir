# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ContentCalendar
def delete_post(channel_id: int, post_id: int) -> bool:
    if channel_id not in channels or post_id not in channels[channel_id].posts:
        print(f"Ошибка: запись с ID {post_id} в канале {channel_id} не найдена")
        return False
    
    del channels[channel_id].posts[post_id]
    
    # Удаляем автора из списка, если он больше не имеет активных постов
    if not any(post_id in p for p in channels[channel_id].posts.values()):
        author_ids = [p.author_id for p in channels[channel_id].posts.values()]
        if channel_id in authors and post_id in authors[channel_id]:
            del authors[channel_id]

def delete_channel(channel_id: int) -> bool:
    if channel_id not in channels:
        print(f"Ошибка: канал с ID {channel_id} не найден")
        return False
    
    # Удаляем все посты канала из авторов перед удалением самого канала
    for post_id, post_data in channels[channel_id].posts.items():
        author_ids = [p.author_id for p in channels[channel_id].posts.values()]
        if channel_id in authors:
            del authors[channel_id]

def delete_author(author_id: int) -> bool:
    if author_id not in authors:
        print(f"Ошибка: автор с ID {author_id} не найден")
        return False
    
    # Удаляем автора из всех каналов, где у него есть посты
    for channel_id, channel_data in channels.items():
        posts_to_remove = [pid for pid, p in channel_data.posts.items() if p.author_id == author_id]
        for pid in posts_to_remove:
            del channel_data.posts[pid]
    
    # Удаляем автора из списка авторов в канале
    if author_id in authors and len(authors[author_id].posts) == 0:
        del authors[author_id]
