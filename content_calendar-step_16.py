# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ContentCalendar
def monthly_stats(self) -> dict:
        """Return per-month statistics for all articles."""
        stats = {}
        now = datetime.now()
        month_start = now.replace(day=1)
        year, month = now.year, now.month
        while True:
            if (year, month) not in stats:
                stats[(year, month)] = {"total": 0, "published": 0, "scheduled": 0, "drafted": 0}
            for article in self.articles.values():
                pub_date = article.published or datetime(1970, 1, 1) if article.published else None
                if pub_date and (pub_date.year > year or (pub_date.year == year and pub_date.month >= month)):
                    stats[(year, month)]["total"] += 1
            for article in self.articles.values():
                deadline = article.deadline
                if deadline:
                    if (deadline.year > year or (deadline.year == year and deadline.month >= month)):
                        status_map = {"published": "published", "scheduled": "scheduled", "drafted": "drafted"}
                        stat_key = status_map.get(article.status, "drafted")
                        stats[(year, month)][stat_key] += 1
            if (year, month) == (now.year, now.month):
                break
            month_start = month_start.replace(month=(month + 1) % 12)
            year += (month + 1) % 12 // 12
            month = (month + 1) % 12
        return stats
