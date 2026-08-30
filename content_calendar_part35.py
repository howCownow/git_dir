# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ContentCalendar
import datetime

def next_actions(items: list[dict]) -> list[str]:
    """Составляет рекомендации следующего действия по текущим публикациям."""
    now = datetime.datetime.now().date()
    urgent = []
    planned = []
    for it in items:
        deadline = datetime.datetime.strptime(it["deadline"], "%Y-%m-%d").date()
        status = it["status"].lower()
        if status == "draft" and deadline <= now + datetime.timedelta(days=3):
            urgent.append(f"{'Срочно'}: {it['title']} — дедлайн {deadline} близок")
        elif status == "planned":
            planned.append(f"Запланировано: {it['title']} на {deadline}")
        elif status == "pending_review":
            urgent.append(f"Ожидает проверки: {it['title']}")
    recs = urgent + planned
    if not recs:
        recs.append("Все публикации в порядке — можно отдыхать")
    return recs
