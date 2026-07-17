# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ContentCalendar
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


class Article:
    def __init__(self, title="", author=None, deadline=None, status="draft", tags=None):
        self.title = title
        self.author = author
        self.deadline = deadline
        self.status = status
        self.tags = set(tags) if tags else set()

    def add_tag(self, tag):
        if not isinstance(tag, Tag):
            raise TypeError("Tag expected")
        self.tags.add(tag)

    def remove_tag(self, tag):
        try:
            self.tags.remove(tag)
        except KeyError:
            raise ValueError(f"Tag {tag!r} not found")

    def has_tag(self, name):
        return any(t.name == name for t in self.tags)


class Channel:
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.articles = []


class ContentCalendar:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        if not isinstance(channel, Channel):
            raise TypeError("Channel expected")
        self.channels.append(channel)

    def get_channels(self):
        return list(self.channels)

    def find_article_by_title(self, title):
        for ch in self.channels:
            for article in ch.articles:
                if article.title == title:
                    return article
        return None


calendar = ContentCalendar()
ch = Channel("TechNews")
cal.add_channel(ch)
a1 = Article("Python 3.12", author="Alice", deadline="2025-06-01", status="published", tags=[Tag("python"), Tag("release")])
ch.articles.append(a1)

print(calendar.get_channels())          # [Channel('TechNews')]
print(calendar.find_article_by_title("Python 3.12"))  # Article('Python 3.12', ...)
print(a1.has_tag("python"))            # True
a1.add_tag(Tag("ai"))
print(a1.tags)                         # {Tag('python'), Tag('release'), Tag('ai')}
a1.remove_tag(Tag("release"))
print(a1.tags)                         # {Tag('python'), Tag('ai')}
