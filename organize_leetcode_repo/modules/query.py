from os import environ
from sys import stdout
from requests import post
from requests.exceptions import ConnectionError
from typing import Any, Dict, Union


environ["ALL_PROXY"] = ""
environ["NO_PROXY"] = ""
environ["all_proxy"] = ""
environ["no_proxy"] = ""


def database_query(name: str) -> Union[Dict[str, Any], None]:
    """Запрашивает данные из базы LeetCode для получения информации о конкретной задаче.

    :param name: Название задачи на LeetCode.
    :return: Словарь, содержащий информацию о вопросе.
    """

    data = {
        "operationName": "questionData",
        "variables": {"titleSlug": name},
        "query": (
            "query questionData($titleSlug: String!) "
            "{\n  question(titleSlug: $titleSlug) "
            "{\n    questionFrontendId\n    title\n    content\n    difficulty\n }  \n}\n"
        ),
    }
    try:
        response = post("https://leetcode.com/graphql", json=data)
        return response.json()["data"]["question"] if response.ok else {}
    except ConnectionError:
        print("Connection error occurred:")
        return None


def execute_queries(queries_map: Dict[str, Dict[str, str]]) -> None:
    """Итерируется по таблице подготовленных задач для запроса

    :param queries_map: Таблица с задачами для запроса.
    :return: None
    """
    cnt = 0
    n = get_query_length(queries_map)
    tasks_to_remove = []
    for task, files in queries_map.items():
        response = database_query(task)
        if response:
            existing_data = queries_map.get(task) or {}
            queries_map[task] = {**existing_data, **response}
            cnt += len(files["files"])
            print(f"[{cnt}/{n}]", "Done", "...", ", ".join(files["files"]))
        else:
            tasks_to_remove.append(task)
            print(f"[{cnt}/{n}]", "Fail", "...", ", ".join(files["files"]))
    for task in tasks_to_remove:
        del queries_map[task]


def show_invalid_queries(
    queries_map: Dict[str, Dict[str, str]], total_files: int
) -> None:
    """Итерируется по таблице подготовленных задач и выводит в stdout, не валидные имена

    :param queries_map: Таблица с задачами для запроса.
    :param total_files: Количество файлов в директории с задачами
    :return: None
    """
    good_names = total_files - get_query_length(queries_map)
    if not queries_map:
        print(f"[{total_files}/{total_files}]")
    else:
        bad_names = []
        for task, files in queries_map.items():
            good_names += len(files["files"])
            stdout.write(f"\r[{good_names}/{total_files}]")
            stdout.flush()
            response = database_query(task)
            if not response:
                bad_names.extend(files["files"])
        print()
        print(*bad_names, sep="\n")


def get_query_length(queries_map: dict) -> int:
    """Вычисляет суммарную длину списка файлов для каждой задачи в словаре queries_map.

    :param queries_map: Словарь, содержащий задачи в качестве ключей
                        и списки файлов в качестве значений.
    :return: Суммарная длина всех списков файлов в queries_map.
    """
    return sum((len(queries_map[task]["files"]) for task in queries_map))
