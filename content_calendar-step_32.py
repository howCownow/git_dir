# === Stage 32: Добавь журнал действий пользователя ===
# Project: ContentCalendar
class ActionLog:
    def __init__(self):
        self.actions = []

    def log(self, user, action, details=""):
        self.actions.append({
            "user": user,
            "action": action,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })

    def get_log(self):
        return self.actions

    def clear(self):
        self.actions.clear()
