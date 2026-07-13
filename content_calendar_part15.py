# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ContentCalendar
def weekly_stats(published, channels):
    """Return dict: channel -> {week_start_date: count} for published items."""
    stats = {}
    now = datetime.now()
    for ch in channels:
        if not ch.is_active:
            continue
        stats[ch.name] = {}
        for pub in published:
            if pub.status != "published":
                continue
            dt = pub.date_published or pub.created_at
            if dt is None:
                continue
            week_start = (dt - timedelta(days=dt.weekday())).date()
            stats[ch.name].setdefault(week_start, 0)
            stats[ch.name][week_start] += 1
    return stats
