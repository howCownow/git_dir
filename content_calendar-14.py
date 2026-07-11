# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ContentCalendar
def generate_summary(data):
    """Генерирует краткую сводку по текущим данным проекта."""
    channels = data.get("channels", [])
    authors = data.get("authors", [])
    articles = data.get("articles", [])
    
    if not (channels or authors or articles):
        return "Данные отсутствуют."

    parts = []
    parts.append(f"Каналов: {len(channels)}")
    parts.append(f"Авторов: {len(authors)}")
    
    statuses = {}
    for article in articles:
        status = article.get("status", "unknown")
        statuses[status] = statuses.get(status, 0) + 1
    
    if statuses:
        parts.append(f"Статусы статей: {', '.join(f'{k}: {v}' for k, v in sorted(statuses.items()))}")

    return "\n".join(parts)
