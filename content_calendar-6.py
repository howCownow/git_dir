# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ContentCalendar
def filter_posts(status=None, category=None, tags=None):
    filtered = []
    for post in posts:
        if status and post['status'] != status:
            continue
        if category and post.get('category') != category:
            continue
        if tags:
            post_tags = set(post.get('tags', []))
            if not any(tag in post_tags for tag in tags):
                continue
        filtered.append(post)
    return filtered

def get_calendar_view(start_date, end_date, filters=None):
    start_dt = datetime(start_date.year, start_date.month, start_date.day)
    end_dt = datetime(end_date.year, end_date.month, end_date.day) + timedelta(days=1) - timedelta(seconds=1)
    filtered_posts = filter_posts(*filters) if filters else posts[:]
    calendar = {}
    for post in filtered_posts:
        date_key = (post['date'].year, post['date'].month, post['date'].day)
        if start_dt <= post['date'] < end_dt:
            calendar.setdefault(date_key, []).append(post)
    return {str(k): v for k, v in sorted(calendar.items())}
