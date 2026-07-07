# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ContentCalendar
def load_data(filename="calendar.json"):
    """Загружает данные из JSON-файла с обработкой ошибок."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"[+] Загружено {len(data)} записей из '{filename}'")
        return data
    except FileNotFoundError:
        print(f"[-] Файл '{filename}' не найден. Создайте его или проверьте путь.")
        return []
    except json.JSONDecodeError as e:
        print(f"[-] Ошибка парсинга JSON: {e}")
        return []
    except PermissionError:
        print(f"[-] Нет прав на чтение файла '{filename}'.")
        return []
