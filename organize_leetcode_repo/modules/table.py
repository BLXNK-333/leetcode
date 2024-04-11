from os.path import basename, splitext
from re import findall, sub
from urllib.parse import quote, unquote
from collections import defaultdict
from typing import Dict, List, Any, Tuple


def get_real_map(all_files: List[str]) -> Dict[str, Dict[str, str]]:
    """Генерирует словарь, сопоставляющий имена задач с путями к файлам в каталоге.

    :param all_files: Список с путями к файлам.
    :return: Возвращает отображение имен задач на пути к файлам.
    """
    real = defaultdict(dict)
    for path in all_files:
        task_w_ext = basename(path)
        task = splitext(task_w_ext)[0]
        real[task][task_w_ext] = path
    return real


def get_table_map(rows_array: List[str]) -> Dict[str, Dict[str, Any]]:
    """Генерирует словарь, сопоставляющий имена задач с деталями задач на основе списка строк
    из файла README.md.

    :param rows_array: Список строк из файла README.md.
    :return: Словарь, где ключи это названия задач, а значения, их атрибуты.
    """

    table = defaultdict(dict)
    for row in rows_array:
        if row.startswith("\n"):
            continue
        _, front_id, title, files, difficulty, _ = row.split("|")
        paths = findall(r"/blob/[^/]+/(.+?(?=\)))", files)
        tasks_w_ext = [basename(path) for path in paths]
        task = splitext(tasks_w_ext[0])[0]

        table[task]["questionFrontendId"] = front_id
        table[task]["title"] = title
        table[task]["difficulty"] = difficulty
        table[task]["files"] = {}

        for i in range(len(paths)):
            table[task]["files"][tasks_w_ext[i]] = unquote(paths[i])
    return table


def get_tasks_for_query(table: Dict[str, Dict[str, Any]],
                        real: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, Any]]:
    """Определяет задачи, присутствующие в реальном каталоге, но не в таблице.

    :param table: Словарь, представляющий таблицу из README.md.
    :param real: Словарь, представляющий задачи в реальном каталоге.
    :return: Возвращает словарь, содержащий задачи, присутствующие в реальном каталоге,
            но отсутствующие в таблице.
    """
    queries_map = defaultdict(dict)
    for task in real:
        if task not in table:
            queries_map[task]["files"] = real[task]
            continue
        for task_ext, path in real[task].items():
            if task_ext not in table[task]["files"]:
                if "files" not in queries_map[task]:
                    queries_map[task]["files"] = {}
                queries_map[task]["files"][task_ext] = path
    return queries_map


def remove_non_existing_entries(table: Dict[str, Dict[str, Any]],
                                real: Dict[str, Dict[str, str]]) -> None:
    """Удаляет записи из таблицы, которых нет в реальном каталоге.

    :param table: Словарь, представляющий таблицу из README.md.
    :param real: Словарь, представляющий задачи в реальном каталоге.
    :return: None
    """
    tasks_to_remove = []

    for task, task_data in table.items():
        if task not in real:
            tasks_to_remove.append(task)
            continue
        files_to_remove = []

        for task_ext, path in task_data["files"].items():
            if task_ext not in real[task]:
                files_to_remove.append(task_ext)
            elif table[task]["files"][task_ext] != real[task][task_ext]:
                table[task]["files"][task_ext] = real[task][task_ext]

        for task_ext in files_to_remove:
            del table[task]["files"][task_ext]

        if not table[task]["files"]:
            tasks_to_remove.append(task)

    for task in tasks_to_remove:
        del table[task]


def merge_tables(queries_map: Dict[str, Any],
                 table: Dict[str, Dict[str, Any]]) -> None:
    """Сливает таблицу с запросами к базе данных LeetCode и таблицу из файла README.md.

    :param queries_map: Словарь с ответом от LeetCode.
    :param table: Словарь, представляющий таблицу из README.md.
    :return: None
    """
    colors = {"Easy": "green", "Medium": "orange", "Hard": "red"}

    for task in queries_map:
        r = queries_map[task]

        if task in table:
            table[task]["files"] |= r["files"]
            continue

        table[task]["questionFrontendId"] = fr" {r["questionFrontendId"]} "
        table[task]["title"] = fr" [{r["title"]}](https://leetcode.com/problems/{task}/description/) "
        table[task]["files"] = r["files"]
        table[task]["difficulty"] = (r" $${\color{" + colors[r["difficulty"]] +
                                     r"}\textnormal{" + r["difficulty"] + r"}}$$ ")


def convert_table(table: Dict[str, Dict[str, Any]],
                  git_attrs: Tuple[str, ...]) -> List[str]:
    """Конвертирует словарь таблицы в список строк.

    :param table: Словарь, представляющий таблицу из README.md.
    :param git_attrs: Кортеж (Имя пользователя на git, Название репозитория на git, Название ветки на git).
    :return: Возвращает список строк.
    """
    user_name, repo_name, git_branch_name = git_attrs
    array = []
    for task in table:
        files = {}
        for task_ext, rel_path in table[task]["files"].items():
            ext = task_ext[task_ext.rfind(".") + 1:]
            files[ext] = (fr"[{ext}](https://github.com/{user_name}/{repo_name}/blob/{git_branch_name}/"
                          fr"{quote(sub(r"\\", r"/", rel_path))})")
        keys = sorted(files.keys())
        table[task]["files"] = " " + ", ".join([files[ext] for ext in keys]) + " "

    sorted_dict = sorted(table.items(), key=lambda item: int(item[1]["questionFrontendId"].strip()))
    for task, items in sorted_dict:
        new_row = "|" + "|".join([items["questionFrontendId"],
                                  items["title"],
                                  items["files"],
                                  items["difficulty"]]) + "|" + "\n"
        array.append(new_row)
    return array
