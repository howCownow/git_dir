# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ContentCalendar
def print_metrics():
    """Рассчитывает ключевые метрики проекта ContentCalendar."""
    channels = [1, 2, 3]
    authors = ["Alice", "Bob"]
    statuses = {"draft": 5, "review": 3, "published": 8, "rejected": 1}

    total_items = sum(statuses.values())
    avg_items_per_channel = total_items / len(channels) if channels else 0
    active_status_count = len([s for s in statuses if statuses[s] > 0])
    most_common_status = max(statuses, key=statuses.get)

    print(f"Всего материалов: {total_items}")
    print(f"Среднее на канал: {avg_items_per_channel:.1f}")
    print(f"Активных статусов: {active_status_count}")
    print(f"Наиболее популярный статус: {most_common_status} ({statuses[most_common_status]} шт.)")

print_metrics()
