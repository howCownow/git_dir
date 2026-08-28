# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ContentCalendar
TEMPLATES = {
    "tweet": {"channel": "Twitter", "status": "Draft", "deadline": None},
    "blog": {"channel": "Blog", "status": "Draft", "deadline": None},
    "post": {"channel": "Telegram", "status": "Draft", "deadline": None},
    "linkedin": {"channel": "LinkedIn", "status": "Draft", "deadline": None},
    "medium": {"channel": "Medium", "status": "Draft", "deadline": None},
    "instagram": {"channel": "Instagram", "status": "Draft", "deadline": None},
}

def create_from_template(template_name, author, title, body, **overrides):
    if template_name not in TEMPLATES:
        raise ValueError(f"Template '{template_name}' not found")
    entry = {
        "title": title,
        "body": body,
        "author": author,
        **TEMPLATES[template_name],
        **overrides,
    }
    entry["created_at"] = datetime.datetime.now(datetime.timezone.utc)
    return entry
