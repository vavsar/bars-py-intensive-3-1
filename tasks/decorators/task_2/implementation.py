from tasks.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(num_type):
        if not isinstance(num_type, int) or num_type < 0:
            raise MyException
        used_func = func(num_type)
        return used_func
    return wrapper


def cache_result(func):
    """
    Декоратор с кэшем результата
    """
    cached_number = 0
    cached_result = 0

    def wrapper(number):
        nonlocal cached_number
        nonlocal cached_result

        used_func = cached_result
        if number != cached_number:
            used_func = func(number)
        cached_number = number
        cached_result = used_func
        return used_func
    return wrapper
