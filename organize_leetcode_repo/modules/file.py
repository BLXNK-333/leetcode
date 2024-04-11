import os.path
from typing import List, Dict, Any


def read_README_MD(path: str) -> List[str]:
    """Читает строки из файла README.MD и возвращает их в виде списка, пропуская заголовок.

    :param path: Путь к файлу.
    :return: Возвращает список строк из таблицы README.md.
    """
    try:
        with open(path, "r") as file:
            file.readline()
            file.readline()
            return file.readlines()
    except FileNotFoundError:
        with open(path, "w") as _:
            pass
        return []


def write_new_table(path: str, array: List[str]) -> None:
    """Записывает строки из массива в файл README.MD.

    :param path: Путь к файлу README.MD
    :param array: Массив строк для таблицы.
    :return: None
    """
    with open(path, "w") as file:
        file.write("| # | Title | Solution | Difficulty |" + "\n")
        file.write("| --- | --- | --- | --- |" + "\n")
        for row in array:
            file.write(row)


def get_all_files_in_dir(directory: str) -> List[str]:
    """Рекурсивно получает список всех файлов в каталоге и его подкаталогах.

    :param directory: Каталог для сканирования.
    :return: Возвращает список всех относительных путей файлов в каталоге и его подкаталогах.
    """
    check_directory_path(directory)
    all_files = []
    parent_dir = os.path.abspath(os.path.join(directory, os.pardir))
    for root, _, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), parent_dir)
            all_files.append(relative_path)
    return all_files


def check_directory_path(SOL_PATH: str) -> None:
    """
    Проверяет, существует ли каталог, указанный в SOL_PATH, и создает его, если он не существует.

    :return: None
    """
    if not os.path.isdir(SOL_PATH):
        os.makedirs(SOL_PATH)
        print(f"Directory '{SOL_PATH}' successfully created.\n"
              f"Move the files with tasks to this directory.\n")


def get_root_directory(levels_up=3):
    """Возвращает абсолютный путь корневой директории, корневая директория,
    в данном случае это название репозитория.

    :param levels_up: Количество уровней, на которые нужно подняться вверх от текущей директории.
    :return: Абсолютный путь.
    """
    current_dir = os.path.abspath(__file__)
    for _ in range(levels_up):
        current_dir = os.path.dirname(current_dir)
    return current_dir


def join_paths(root: str, child: str) -> str:
    """Обертка для функции os.path.join.

    :return: Абсолютный путь.
    """
    return os.path.join(root, child)


def parse_config_options() -> Dict[str, Any]:
    """Парсит опции конфигурации из файла и возвращает словарь с параметрами.

    :return: Словарь с параметрами конфигурации.
    """
    options = {
        "add_descriptions": True,
        "solutions_path": join_paths(get_root_directory(), "solutions")
    }
    try:
        ini_path = join_paths(get_root_directory(levels_up=2), "config.ini")
        with open(ini_path, 'r') as f:
            for line in f:
                if line[0] == "#":
                    continue
                array = line.strip().split('=')
                if len(array) != 2:
                    continue
                key, value = map(str.strip, array)
                if key == "solutions_path":
                    options["solutions_path"] = value.rstrip("\\/")
                elif key == "add_description":
                    if value.lower() != "true":
                        options["add_description"] = False
            return options
    except FileNotFoundError:
        pass
    return options
