# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ContentCalendar
def verify_integrity():
    errors = []
    channels = data.get("channels", {})
    authors = data.get("authors", {})
    posts = data.get("posts", [])
    for i, post in enumerate(posts):
        cid = post.get("channel_id")
        aid = post.get("author_id")
        if cid not in channels:
            errors.append(f"Post {i}: channel_id {cid} not in channels")
        if aid not in authors:
            errors.append(f"Post {i}: author_id {aid} not in authors")
        if post.get("deadline") and post["deadline"] < post.get("created_at"):
            errors.append(f"Post {i}: deadline before created_at")
    if errors:
        print("Integrity errors:", errors)
        return False
    return True
