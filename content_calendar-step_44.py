# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ContentCalendar
def backup_data(data_path, backup_dir=None):
    import shutil, os
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_path), 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}.json')
    shutil.copy2(data_path, backup_path)
    return backup_path

if __name__ == '__main__':
    print(backup_data('calendar.json'))
