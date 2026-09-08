# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ContentCalendar
def main():
    import argparse
    parser = argparse.ArgumentParser(description="ContentCalendar CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_new = sub.add_parser("new", help="Создать новый материал")
    p_new.add_argument("--title", required=True)
    p_new.add_argument("--channel", default="default")
    p_new.add_argument("--author", default="unknown")
    p_new.add_argument("--deadline", default="")
    p_new.add_argument("--status", default="draft")

    p_edit = sub.add_parser("edit", help="Изменить материал")
    p_edit.add_argument("--id", required=True)
    p_edit.add_argument("--title", default=None)
    p_edit.add_argument("--status", default=None)
    p_edit.add_argument("--author", default=None)

    p_list = sub.add_parser("list", help="Список материалов")

    p_show = sub.add_parser("show", help="Показать материал")
    p_show.add_argument("--id", required=True)

    args = parser.parse_args()

    if args.cmd == "new":
        if not materials:
            materials = []
        materials.append({
            "id": len(materials) + 1,
            "title": args.title,
            "channel": args.channel,
            "author": args.author,
            "deadline": args.deadline,
            "status": args.status,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })
        print(f"Создан материал #{args.id}")
    elif args.cmd == "edit":
        for m in materials:
            if m["id"] == int(args.id):
                if args.title: m["title"] = args.title
                if args.status: m["status"] = args.status
                if args.author: m["author"] = args.author
                print(f"Обновлен материал #{args.id}")
                break
        else:
            print("Материал не найден")
    elif args.cmd == "list":
        for m in materials:
            print(f"#{m['id']} | {m['title']} | {m['status']} | {m['author']} | {m['deadline']}")
    elif args.cmd == "show":
        for m in materials:
            if m["id"] == int(args.id):
                print(f"#{m['id']} | {m['title']} | {m['status']} | {m['author']} | {m['deadline']}")
                break
        else:
            print("Материал не найден")

if __name__ == "__main__":
    main()
