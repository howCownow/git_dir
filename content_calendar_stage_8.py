# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ContentCalendar
def show_menu():
    print("\n--- Меню действий ---")
    print("1. Показать все материалы")
    print("2. Добавить новый материал")
    print("3. Изменить статус материала")
    print("4. Выйти из программы")
    choice = input("Выберите действие (1-4): ")
    if choice == "1":
        for item in materials:
            print(f"\n[Канал: {item['channel']}] Автор: {item['author']} | Дедлайн: {item['deadline']} | Статус: {item['status']}")
    elif choice == "2":
        channel = input("Название канала: ")
        author = input("Имя автора: ")
        deadline = input("Дата дедлайна (ДД.ММ): ")
        status = input("Статус (Черновик/В работе/Опубликовано): ")
        materials.append({"channel": channel, "author": author, "deadline": deadline, "status": status})
        print("Материал добавлен.")
    elif choice == "3":
        idx = int(input("Индекс материала для изменения (0-N): "))
        if 0 <= idx < len(materials):
            new_status = input("Новый статус: ")
            materials[idx]["status"] = new_status
            print("Статус обновлен.")
    elif choice == "4":
        exit()
