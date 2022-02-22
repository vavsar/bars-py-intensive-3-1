from time import sleep

from tasks.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def inner(func):
        def wrapper():
            time = times
            while time > 0:
                try:
                    exec_func = func()
                    return exec_func
                except:
                    sleep(delay)
                    time -= 1
            raise MyException
        return wrapper
    return inner
