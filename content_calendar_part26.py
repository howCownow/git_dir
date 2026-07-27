# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ContentCalendar
def demo_quick_test():
    """Quick manual test commands."""
    print("=== ContentCalendar Demo ===")
    from datetime import date, timedelta
    for i in range(10):
        d = date.today() + timedelta(days=i)
        print(f"Day {i}: {d} ({'Weekend' if d.weekday()>=5 else 'Workday'})")
