# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ContentCalendar
import datetime

class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def is_overdue(self):
        return self.due_date < datetime.datetime.now()

    def __str__(self):
        status = "⚠️ ПЕРЕДВИНУТО" if self.is_overdue() else "✅ В срок"
        return f"{status}: {self.title} (до: {self.due_date.strftime('%d.%m.%Y')})"

    def __repr__(self):
        return f"<Reminder '{self.title}' due={self.due_date.date()}>"
