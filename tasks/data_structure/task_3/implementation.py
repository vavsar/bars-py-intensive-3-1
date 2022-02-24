import copy


def copy_dict(origin_dict: dict) -> dict:
    """
    Функция возвращает глубокую копию словаря.
    """
    new_dict = copy.deepcopy(origin_dict)
    return new_dict
