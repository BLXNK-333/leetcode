from scripts import ScriptController


class OrganizeRepoManager:
    """Класс предоставляет интерфейс взаимодействия с программой. Класс обертка"""

    def __init__(self):
        pass

    @staticmethod
    def run_update_script() -> None:
        """Скрипт штатного обновления.

        :return: None
        """
        controller = ScriptController()
        controller.run_update_script()

    @staticmethod
    def run_rewrite_script() -> None:
        """Скрипт перезаписи описаний и таблицы.

        :return: None
        """
        controller = ScriptController(rewrite=True)
        controller.run_update_script()

    @staticmethod
    def show_invalid_task_names() -> None:
        """Скрипт для показа недействительных имен.

        :return: None
        """
        controller = ScriptController()
        controller.show_invalid_task_names()

    @staticmethod
    def remove_all_descriptions() -> None:
        """Скрипт удаляет описания из всех файлов.

        :return: None
        """
        controller = ScriptController()
        controller.remove_all_descriptions()

    @staticmethod
    def add_missing_descriptions() -> None:
        """Скрипт добавляет недостающие описания к файлам.

        :return: None
        """
        controller = ScriptController()
        controller.add_missing_descriptions()