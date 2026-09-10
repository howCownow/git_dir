# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: ContentCalendar
def dry_run(operation, record, before, after):
    """Log an operation change without applying it."""
    logger.info(
        f"[DRY-RUN] {operation}: {before} -> {after}",
        extra={
            "operation": operation,
            "record": record,
            "before": before,
            "after": after,
        },
    )
