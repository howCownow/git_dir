# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ContentCalendar
def archive_old_records(db, days=365):
    cutoff = datetime.now() - timedelta(days=days)
    archived_count = 0
    for channel in db.channels.values():
        if not channel.archived:
            channel.archived = True
            archived_count += 1
    return archived_count
