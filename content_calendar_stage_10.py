# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ContentCalendar
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "channels": channels,
        "authors": authors,
        "posts": posts
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
