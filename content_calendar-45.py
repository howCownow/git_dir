# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ContentCalendar
import json, os

def restore_backup(backup_path, target_path):
    if not os.path.isfile(backup_path):
        print(f"[WARN] Не найдена резервная копия: {backup_path}")
        return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Резервная копия восстановлена: {backup_path} -> {target_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Восстановление резервной копии провалилось: {e}")
        return False
