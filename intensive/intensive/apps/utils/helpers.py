def ordered(obj):
    """
    Функция сортировки словарей, списков
    """
    if isinstance(obj, dict):
        result = sorted((k, ordered(v)) for k, v in obj.items())
    elif isinstance(obj, list):
        result = sorted(ordered(x) for x in obj)
    else:
        result = str(obj)

    return result
