from datetime import date


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    day, month, year = some_date.day, some_date.month, some_date.year

    if year % 4 == 0:
        days_in_month[2] = 29

    if day == days_in_month[month]:
        day = 1
        if month == 12:
            month = 1
            year = year + 1
        else:
            month += 1

    elif month == 12:
        month = 1
        year = year + 1

    else:
        day += 1

    new_date = year, month, day

    return date(*new_date)
