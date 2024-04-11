import os.path
from subprocess import run, PIPE, CalledProcessError


def get_info_sh():
    """Выполняет скрипт 'parse_git.sh' на Bash. В случае успеха, возвращает
    имя репозитория, название ветки Git, имя пользователя Git.

    :return: Картеж с атрибутами.
    """
    script_path = os.path.join(os.path.dirname(__file__), "parse_git.sh")
    try:
        result = run(["bash", script_path], check=True, stdout=PIPE, text=True)
        attributes = result.stdout.strip().split('\n')
        if all(attributes):
            return tuple(attributes)
        print("Error: Failed to retrieve Git attributes.")
    except CalledProcessError as e:
        # Код ошибки 126 означает "Permission denied"
        if e.returncode == 126:
            print(f"Permission denied: Insufficient permissions to execute the script\n")
        else:
            print(f"Script execution error: {e}\n")
        print(f"target: {script_path}\n")
