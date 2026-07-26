# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ContentCalendar
def parse_date_with_errors(date_str, fmt=None):
    """Parse a date string and return (datetime.date, None) or (None, error_msg)."""
    if not isinstance(date_str, str) or not date_str.strip():
        return None, "Дата должна быть строкой и не может быть пустой"
    
    import datetime as dt
    
    formats = [fmt] if fmt else ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"]
    for f in formats:
        try:
            return dt.date.fromisoformat(date_str.replace(".", "-").replace("/", "-")), None
        except ValueError:
            continue
    
    # Fallback: try common patterns
    import re
    cleaned = date_str.strip()
    if re.match(r"^\d{4}-\d{2}(\.\d{2})?$", cleaned):
        parts = cleaned.split(".")
        year, month = int(parts[0]), int(parts[1]) if len(parts) > 1 else dt.date.today().month
        return dt.date(year, month, 1), None
    
    return None, f"Не удалось распарсить дату: '{date_str}' (поддерживаются форматы: YYYY-MM-DD или DD.MM.YYYY)"
