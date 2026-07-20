# === Stage 20: Добавь восстановление записей из архива ===
# Project: ContentCalendar
def load_archive():
    archive_path = "archive.csv"
    if not os.path.exists(archive_path):
        return []
    records = []
    with open(archive_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                record = {
                    "channel": row["channel"],
                    "author": row["author"],
                    "deadline": datetime.fromisoformat(row["deadline"]),
                    "status": row["status"],
                    "title": row["title"] or "",
                    "description": row["description"] or "",
                }
                records.append(record)
            except (KeyError, ValueError):
                continue
    return records

if __name__ == "__main__":
    archived = load_archive()
    print(f"Восстановлено записей из архива: {len(archived)}")
