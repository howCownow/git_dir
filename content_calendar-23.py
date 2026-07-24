# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ContentCalendar
def print_calendar_table():
    if not channels:
        print("Таблица пуста. Добавьте каналы.")
        return
    headers = ["ID", "Канал", "Заголовок", "Автор", "Дедлайн", "Статус"]
    widths = [5, 12, 30, 12, 12, 12]
    row = []
    for ch in channels:
        items = {
            "ID": str(ch.id),
            "Канал": ch.name,
            "Заголовок": (ch.title or "Без заголовка")[:30],
            "Автор": (ch.author or "Не указан")[:12],
            "Дедлайн": (ch.deadline.strftime("%d.%m") if ch.deadline else "Нет"),
            "Статус": ch.status.value,
        }
        row = [items[h] for h in headers]
    separator = "-" * sum(widths) + "+"
    print(separator)
    print("| " + "| ".join(h.ljust(w) for h, w in zip(headers, widths)) + " |")
    print(separator)
    for r in row:
        print("| " + " | ".join(r[j].ljust(widths[j]) for j in range(len(headers))) + " |")
    print(separator)
