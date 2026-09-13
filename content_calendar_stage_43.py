# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ContentCalendar
def paginate_list(items, page_size=10):
    pages = [items[i:i+page_size] for i in range(0, len(items), page_size)]
    return pages, len(items), page_size
