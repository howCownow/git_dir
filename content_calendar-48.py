# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ContentCalendar
def _status_color_map(status):
    return {
        "planned": "#888888",
        "in_progress": "#4488ff",
        "completed": "#00cc44",
        "rejected": "#cc2222",
        "draft": "#ffaa00",
    }.get(status, "#aaaaaa")


def format_calendar_row(entry, max_title=60):
    title = entry["title"] if "title" in entry else ""
    if len(title) > max_title:
        title = title[:max_title] + "..."
    deadline = entry.get("deadline", "")
    status = entry.get("status", "draft")
    channel = entry.get("channel", "")
    author = entry.get("author", "")
    deadline_str = deadline.strftime("%d.%m") if hasattr(deadline, "strftime") else str(deadline)
    return f"{channel:12s} | {title:60s} | {deadline_str:8s} | {status:10s} | {author}"


def print_calendar(entries, max_title=60):
    if not entries:
        print("Календарь пуст.")
        return
    headers = ["Канал", "Материал", "Дедлайн", "Статус", "Автор"]
    header_line = " | ".join(f"{h:^12}" for h in headers)
    print(header_line)
    print("-" * len(header_line))
    for entry in entries:
        print(format_calendar_row(entry, max_title))
