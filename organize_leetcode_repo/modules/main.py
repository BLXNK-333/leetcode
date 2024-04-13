import sys
from manager import OrganizeRepoManager


def main():
    manager = OrganizeRepoManager()
    actions = {
        "1": manager.run_update_script,
        "2": manager.run_rewrite_script,
        "3": manager.add_missing_descriptions,
        "4": manager.remove_all_descriptions,
        "5": manager.show_invalid_task_names,
    }
    args = sys.argv[1:]

    if not args:
        manager.run_update_script()
        return

    elif len(args) == 1 and args[0] == "--interface":
        try:
            choice = input(
                "organize_leetcode_repo\n"
                "-------------------------------\n"
                "Выберите действие:\n"
                "1 - обновить таблицу README.md и добавить описания к новым файлам с задачами\n"
                "2 - принудительно перезаписать все описания задач и таблицу README.md\n"
                "3 - добавить описание только к тем файлам, у которых его нет\n"
                "4 - удалить все описания из файлов с задачами\n"
                "5 - показать неверные имена задач\n\n"
                "q - выход из программы\n"
                "-------------------------------\n"
                "Ваш выбор: "
            )

            if choice == "q":
                return

            func = actions.get(choice, None)
            if func:
                func()
        except KeyboardInterrupt:
            sys.exit(1)

    else:
        print("Неверный ключ запуска, для доступа к интерфейсу используйте ключ --interface")

    print("\nDone")


if __name__ == '__main__':
    main()
