# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ContentCalendar
def check_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for pub in calendar.published:
        if pub.status == 'scheduled' and pub.deadline < today:
            overdue.append((pub.title, pub.channel.name, (today - pub.deadline).days))
    return overdue
