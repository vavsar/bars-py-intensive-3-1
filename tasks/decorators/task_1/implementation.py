from time import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args, **kwargs):
        start_time = time()
        used_func = func(*args, **kwargs)
        end_time = time()
        print(f'func executed for: {end_time-start_time}')
        return used_func
    return wrapper
