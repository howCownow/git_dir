# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ContentCalendar
class ContentCalendar:
    def __init__(self):
        self._channels = {}
        self._authors = {}
        self._posts = []

    def add_channel(self, name: str, topic: str) -> None:
        if not name or not topic: raise ValueError("Name and topic required")
        self._channels[name] = {"name": name, "topic": topic}

    def add_author(self, name: str, role: str) -> None:
        if not name or not role: raise ValueError("Name and role required")
        self._authors[name] = {"name": name, "role": role}

    def create_post(self, channel_name: str, author_name: str, title: str, deadline: datetime.datetime, status: str) -> int:
        if not all([channel_name, author_name, title, deadline]): raise ValueError("All fields required")
        valid_statuses = ["draft", "scheduled", "published"]
        if status not in valid_statuses: raise ValueError(f"Status must be one of {valid_statuses}")
        
        channel_data = self._channels.get(channel_name)
        author_data = self._authors.get(author_name)
        if not channel_data or not author_data: raise KeyError("Channel or Author not found")

        post_id = len(self._posts) + 1
        post = {
            "id": post_id,
            "channel": channel_name,
            "author": author_name,
            "title": title,
            "deadline": deadline,
            "status": status
        }
        self._posts.append(post)
        return post_id

    def get_posts_by_channel(self, channel_name: str) -> list[dict]:
        if not channel_name in self._channels: raise KeyError("Channel not found")
        return [p for p in self._posts if p["channel"] == channel_name]
