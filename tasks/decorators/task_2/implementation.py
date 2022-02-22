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
    cache = {}

    def wrapper(number):
        used_func = cache[number]
        if number not in cache:
            used_func = func(number)
            cache[number] = used_func
        return used_func
    return wrapper
