def print_LOG(message: str = "") -> None:
    """
    Выводит сообщение журнала для указанной функции.

    :param message: Сообщение в заголовке.
    :return: None
    """
    print(f"\nLOG:  {message}\n{'-' * 50}")