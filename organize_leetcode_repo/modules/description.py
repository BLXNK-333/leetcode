import os.path
from os.path import join as join_paths, splitext
from bs4 import BeautifulSoup
from re import sub, escape, match, search
from textwrap import wrap
from typing import List, Dict, Any, Union


multi_line_comments = {
    "py": ('"""', '"""'),  # Python
    "cpp": ("/*", "*/"),  # C++
    "java": ("/*", "*/"),  # Java
    "csharp": ("/*", "*/"),  # C#
    "js": ("/*", "*/"),  # JavaScript
    "html": ("<!--", "-->"),  # HTML
    "css": ("/*", "*/"),  # CSS
    "kt": ("/*", "*/"),  # Kotlin
    "swift": ("/*", "*/"),  # Swift
    "rs": ("/*", "*/"),  # Rust
    "php": ("/*", "*/"),  # PHP
    "go": ("/*", "*/"),  # Go
    "ruby": ("=begin", "=end"),  # Ruby
    "lua": ("--[[", "--]]"),  # Lua
    "sh": (": <<'COMMENT'", "COMMENT"),  # Shell
    "sql": ("/*", "*/"),  # SQL
}


def read_file(path: str) -> List[str]:
    """Читает файл с задачей

    :param path: Абсолютный путь к файлу.
    :return: Список строк из файла, без пустых строк в начале
    """
    with open(path, "r") as file:
        lines = []
        while True:
            line = file.readline()
            if not line:
                break
            text = search(r"\S", line)
            if not text:
                continue
            lines.append(line)
            break
        lines.extend(file.readlines())
        return lines


def add_description_to_file(path: str, description: str) -> None:
    """Добавляет описание к файлу. Описание это многострочный комментарий вначале файла.

    :param path: Абсолютный путь к файлу.
    :param description: Описание.
    :return: None
    """
    old = read_file(path)
    if find_old_description(old):
        return

    ext = check_extension_validity(path)
    if ext:
        start = multi_line_comments[ext][0]
        end = multi_line_comments[ext][1]
        content = start + "\n" + parse_html_content(description) + "\n" + end + "\n\n"

        with open(path, "w") as file:
            file.write(content)
            for row in old:
                file.write(row)


def check_extension_validity(path: str) -> Union[str, None]:
    """Проверяет на валидность расширение файла.

    :param path: Путь к файлу.
    :return: Расширение файла или None.
    """
    name, ext = splitext(path)
    if ext and (ext := ext.lstrip(".")) in multi_line_comments:
        return ext


def add_all_descriptions(
    directory: str, queries_map: Dict[str, Dict[str, Any]]
) -> None:
    """Добавляет описание ко всем файлам из tasks.

    :param directory: Путь к каталогу с файлами.
    :param queries_map: Словарь задач с описаниями.
    :return: None
    """
    for task in queries_map:
        for _, path in queries_map[task]["files"].items():
            if "content" in queries_map[task]:
                add_description_to_file(
                    join_paths(directory, path), queries_map[task]["content"]
                )


def parse_html_content(content: str) -> str:
    """Обрабатывает содержимое HTML из ответа LeetCode.

    :param content: HTML-контент.
    :return: Обработанный текст.
    """
    soup = BeautifulSoup(content, "lxml")
    question = soup.get_text()
    return format_description(question)


def find_old_description(old: List[str]) -> bool:
    """Проверяет наличие старого описания.

    :param old: Строки файла.
    :return: True, если старое описание найдено, в противном случае - False.
    """
    if old:
        pattern = r"""^\s*?(\"\"\"|/\*|<!--|=begin|--\[\[|: <<'COMMENT')"""
        return bool(match(pattern, old[0]))
    return False


def find_missing_descriptions(directory: str, all_files: List[str]) -> List[str]:
    """

    :param directory: Путь к корневой директории.
    :param all_files: Список всех файлов.
    :return:
    """
    missing = []
    for path in all_files:
        old = read_file(os.path.join(directory, path))
        if not find_old_description(old):
            missing.append(path)
    return missing


def remove_description_from_file(path: str) -> None:
    """Удаляет описание, из файла, шаблон берет из multi_line_comments.

    :param path: Абсолютный путь к файлу.
    :return: None
    """
    with open(path, "r") as file:
        content = file.read()

    ext = check_extension_validity(path)
    if ext:
        start = escape(multi_line_comments[ext][0])
        end = escape(multi_line_comments[ext][1])
        content = sub(rf"{start}[\s\S]+?{end}", "", content).lstrip("\n")

        with open(path, "w") as file:
            file.write(content)


def remove_all_descriptions(directory: str, paths: List[str]) -> None:
    """Удаляет описания из всех файлов

    :param directory: Строка для формирования абсолютного пути к файлу.
    :param paths: Список с путями к файлам.
    :return: None
    """
    for path in paths:
        remove_description_from_file(join_paths(directory, path))


def format_description(input_string: str, max_length: int = 79) -> str:
    """Форматирует строку так, чтобы она вписывалась в максимальную длину строки.

    :param input_string: Входная строка для форматирования.
    :param max_length: Максимальная длина строки. По умолчанию 96.
    :return: Отформатированная строка.
    """
    lines = input_string.split("\n")
    formatted_lines = []
    for line in lines:
        if line.startswith(("Example", "Constraints")):
            formatted_lines.append("")
        if line.strip():
            formatted_lines.extend(wrap(line, width=max_length))
    return "\n".join(formatted_lines)
