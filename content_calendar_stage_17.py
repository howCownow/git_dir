# === Stage 17: Добавь группировку записей по категориям ===
# Project: ContentCalendar
class Category:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Category {self.name}>"


def categorize_record(record, categories=None):
    if not categories:
        return record.get("category", "Uncategorized")
    for cat in categories:
        if cat and cat.lower() == record.get("category", "").lower():
            return cat
    return "Uncategorized"


class ContentCalendar:
    def __init__(self):
        self.channels = []
        self.authors = []
        self.records = []
        self.categories = [Category("General"), Category("News")]

    def add_channel(self, name):
        self.channels.append(name)

    def add_author(self, name):
        self.authors.append(name)

    def add_record(self, title, channel=None, author=None, deadline=None, status="Draft", category=None):
        record = {
            "title": title,
            "channel": channel or self.channels[0] if self.channels else None,
            "author": author or self.authors[0] if self.authors else None,
            "deadline": deadline,
            "status": status,
            "category": category or Category("General").name
        }
        self.records.append(record)

    def get_records_by_category(self):
        grouped = {}
        for record in self.records:
            cat_name = categorize_record(record, [c.name for c in self.categories])
            grouped.setdefault(cat_name, []).append(record)
        return grouped

    def print_calendar(self):
        grouped = self.get_records_by_category()
        for category, records in grouped.items():
            print(f"\n--- {category} ---")
            for r in records:
                deadline_str = str(r["deadline"]) if r["deadline"] else "no-deadline"
                print(f"  [{r['status']}] {r['title']} | by {r['author']} | channel: {r['channel']} | deadline: {deadline_str}")
