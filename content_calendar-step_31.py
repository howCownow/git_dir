# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ContentCalendar
def switch_active_profile(user_id: int) -> dict:
    """Переключить активный профиль и вернуть обновлённые данные."""
    global active_profile_id
    if user_id not in profiles:
        return {"error": "Профиль не найден", "active_profile_id": active_profile_id}
    active_profile_id = user_id
    return {"active_profile_id": active_profile_id}
