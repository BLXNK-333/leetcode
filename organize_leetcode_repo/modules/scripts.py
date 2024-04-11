from typing import Dict, Any

from git_info import get_info_sh
from file import (get_root_directory,
                  join_paths,
                  read_README_MD,
                  get_all_files_in_dir,
                  write_new_table,
                  parse_config_options)
from table import (get_table_map,
                   get_real_map,
                   remove_non_existing_entries,
                   get_tasks_for_query,
                   merge_tables,
                   convert_table)
from description import remove_all_descriptions, add_all_descriptions
from query import execute_queries, show_invalid_queries
from utils import print_LOG


class ScriptController:
    def __init__(self, rewrite: bool = False):
        self.rewrite = rewrite
        self.directory = get_root_directory()
        options = parse_config_options()
        self.add_descriptions = options["add_descriptions"]
        self.SOL_PATH = options["solutions_path"]
        self.MD_PATH = join_paths(self.directory, "README.md")

        self.git_attr = get_info_sh()
        self.readme_table = self.get_readme_table()
        self.all_files = get_all_files_in_dir(self.SOL_PATH)
        self.queries_map = self.get_queries_map()

    def get_readme_table(self) -> Dict[str, Dict[str, Any]]:
        """
        :return: Словарь с таблицей из README.md
        """
        readme = []
        if not self.rewrite:
            readme = read_README_MD(self.MD_PATH)
        return get_table_map(readme)

    def get_queries_map(self) -> Dict[str, Dict[str, Any]]:
        """
        :return: Словарь с таблицей запросов к БД
        """
        real = get_real_map(self.all_files)
        remove_non_existing_entries(self.readme_table, real)
        return get_tasks_for_query(self.readme_table, real)

    def update_README_MD(self) -> None:
        """Записывает изменения в таблицу.

        :return: None
        """
        to_write = convert_table(self.readme_table, self.git_attr)
        write_new_table(self.MD_PATH, to_write)

    def description_rewriter(self) -> None:
        """Запускает логику обработки описаний в файлах, в зависимости от переданных параметров.

        :return: None
        """
        if self.add_descriptions:
            if self.rewrite:
                remove_all_descriptions(self.directory, self.all_files)
            add_all_descriptions(self.directory, self.queries_map)

    def run_update_script(self) -> None:
        """
        Этот скрипт предназначен для обычного использования. Если вы добавили новые файлы,
        запустите скрипт, и он автоматически внесет соответствующие изменения.

        Если хотите принудительно перезаписать описание для всех файлов с задачами, передайте
        параметр rewrite=True. После его выполнения в каждом файле останется только один
        многострочный комментарий, также он обновит таблицу README.md.

        :return: None
        """
        if not self.git_attr:
            return

        if self.rewrite:
            print_LOG("Rewrite all descriptions and README.md")
            self.rewrite = True
            self.add_descriptions = True
        else:
            print_LOG("Update")

        if self.queries_map:
            execute_queries(self.queries_map)
            merge_tables(self.queries_map, self.readme_table)
            self.description_rewriter()

        self.update_README_MD()
        print("Complete.")

    def show_invalid_task_names(self) -> None:
        """
        Используйте этот скрипт, если хотите убедиться, что все файлы задач имеют правильные
        имена. Во время выполнения выводит в stdout имена файлов, для которых не удалось получить
        ответ от LeetCode.

        :return: None
        """
        if not self.git_attr:
            return
        print_LOG("Show invalid task names")
        show_invalid_queries(self.queries_map, len(self.all_files))

    def remove_all_descriptions(self) -> None:
        """
        Используйте этот скрипт, если хотите удалить описания из всех файлов с задачами.

        :return: None
        """
        print_LOG("Remove all descriptions")
        remove_all_descriptions(self.directory, self.all_files)
        self.update_README_MD()
