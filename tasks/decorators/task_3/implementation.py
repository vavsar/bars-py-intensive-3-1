def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        func()
        return count
    return wrapper
