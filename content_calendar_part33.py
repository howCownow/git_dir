# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ContentCalendar
def undo_last():
    """Откат последнего действия, если оно было добавлено/изменено."""
    if not _undo_stack:
        print("Нет откатываемых действий.")
        return
    action = _undo_stack.pop()
    action.undo()
    print(f"Откат: {action.description} — восстановлено.")


class UndoAction:
    def __init__(self, description):
        self.description = description

    def undo(self):
        raise NotImplementedError("Подклассы должны реализовать undo()")


class UndoAddChannel(UndoAction):
    def undo(self):
        if self.channel:
            self.channels.remove(self.channel)
            self.channel = None


class UndoAddAuthor(UndoAction):
    def undo(self):
        if self.author:
            self.authors.remove(self.author)
            self.author = None


class UndoAddDeadline(UndoAction):
    def undo(self):
        if self.deadline:
            self.deadlines.remove(self.deadline)
            self.deadline = None


class UndoAddStatus(UndoAction):
    def undo(self):
        if self.status:
            self.statuses.remove(self.status)
            self.status = None


class UndoAddContent(UndoAction):
    def undo(self):
        if self.content:
            self.contents.remove(self.content)
            self.content = None


class UndoAddPost(UndoAction):
    def undo(self):
        if self.post:
            self.posts.remove(self.post)
            self.post = None
