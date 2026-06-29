# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ContentCalendar
def sort_posts(posts, key='date'):
    if not posts: return []
    reverse = {'date': True, 'priority': False, 'name': False}.get(key, True)
    def get_sort_key(p):
        val = p.get('deadline', None) or p.get('publish_date', None)
        if key == 'priority': return -p['priority']
        if key == 'name': return (0, p['name'])
        return (1 if val else 2, val or '')
    return sorted(posts, key=get_sort_key, reverse=reverse)
