#!/bin/bash

# Получаем путь к текущему скрипту
SCRIPT_PATH=$(realpath "${BASH_SOURCE[0]}")
# Извлекаем каталог, где находится скрипт
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR" || exit
CONFIG_FILE="$SCRIPT_DIR/config.ini"

# Чтение версии интерпретатора Python из файла config.ini
VENV_PATH=$(grep '^venv_path=' "$CONFIG_FILE" | cut -d '=' -f2-)

# Проверка наличия переменной VENV_PATH
if [ -z "$VENV_PATH" ]; then
    echo "Ошибка: переменная venv_path не установлена в файле конфигурации."
    exit 1
fi

# Проверка существования директории
if [ ! -d "$VENV_PATH" ]; then
    echo "Ошибка: директория виртуального окружения не существует."
    exit 1
fi

# Запускаем виртуальное окружение
source "$VENV_PATH/bin/activate"

# Если переданы аргументы, запускаем Python скрипт с переданными аргументами
python3 "$SCRIPT_DIR/modules/main.py" "$@"

# Деактивация виртуального окружения
deactivate
