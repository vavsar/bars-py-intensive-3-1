from tasks.common import MyException


class Value:
    """
    Реализованы базовые арифметические операции
    для инстанса класса
    """
    def __init__(self, value):
        try:
            self.value = int(value)
        except MyException:
            raise TypeError('Необходимо ввести число')

    def get_result(self):
        return self.value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        if other == 0:
            raise MyException
        return self.value / other

