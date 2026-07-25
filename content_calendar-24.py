# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ContentCalendar
def print_post(post):
    """Compact single-post display."""
    if not post:
        return "No data."
    status_colors = {
        'draft': '\033[94m',     # blue
        'published': '\033[92m',  # green
        'scheduled': '\033[33m',  # yellow
        'failed': '\033[1;31m',   # bold red
    }
    color = status_colors.get(post.status, '')
    reset = '\033[0m'
    deadline = post.deadline.strftime('%d.%m') if isinstance(post.deadline, datetime) else str(post.deadline)
    print(f"{color}Status: {post.status}{reset}")
    print(f"Channel: {post.channel.name}")
    print(f"Author:   {post.author.full_name}")
    print(f"Title:    {post.title or '(unnamed)'}")
    print(f"Deadline: {deadline}")
    if post.body:
        body_preview = post.body[:120] + '...' if len(post.body) > 120 else post.body
        print(f"Body:     {body_preview}")
