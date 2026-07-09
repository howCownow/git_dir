# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ContentCalendar
def search_contents(query: str, contents: list) -> list:
    query_lower = query.lower()
    results = []
    for c in contents:
        if (query_lower in c["title"].lower() or
            query_lower in c["body"].lower() or
            query_lower in c["author_name"].lower()):
            results.append(c)
    return results
