# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ContentCalendar
class ValidationError(Exception): pass

def validate_channel_name(name: str) -> bool: not name or len(name.strip()) < 2 or " " in name
def validate_author_name(name: str) -> bool: not name or len(name.strip()) > 100
def validate_deadline(date_str: str, today: datetime.date) -> tuple[bool, ValidationError | None]:
    try: date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError: return False, ValidationError("Неверный формат даты (YYYY-MM-DD)")
    if date < today - timedelta(days=365): return False, ValidationError("Срок публикации слишком старый")
    if date > today + timedelta(days=720): return False, ValidationError("Срок публикации слишком далёкий в будущем")
    return True, None

def validate_status(status: str) -> bool: status in ["draft", "scheduled", "published"]
