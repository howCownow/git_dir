# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ContentCalendar
import json, os

DATA_FILE = "calendar_data.json"

def save_calendar(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_calendar():
    if not os.path.exists(DATA_FILE):
        return {"channels": [], "posts": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"channels": [], "posts": []}

def update_calendar(data):
    save_calendar(data)
    print("Данные успешно сохранены.")
