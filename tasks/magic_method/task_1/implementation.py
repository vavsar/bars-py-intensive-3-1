class Multiplier:
    """
    Класс реализуает базовые арифметические операции с числами
    и аналогичными классами
    """
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)

    def get_value(self):
        return int(self._value)

    def __add__(self, other):
        if not isinstance(other, (int, Multiplier)):
            raise TypeError('Правый операнд должен быть int или Multiplier')
        return Multiplier(self._value + other.get_value())

    def __sub__(self, other):
        if not isinstance(other, (int, Multiplier)):
            raise TypeError('Правый операнд должен быть int или Multiplier')
        return Multiplier(self._value - other.get_value())

    def __mul__(self, other):
        if not isinstance(other, (int, Multiplier)):
            raise TypeError('Правый операнд должен быть int или Multiplier')
        return Multiplier(self._value * other.get_value())

    def __truediv__(self, other):
        if not isinstance(other, (int, Multiplier)):
            raise TypeError('Правый операнд должен быть int или Multiplier')
        return Multiplier(self._value / other.get_value())


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 100


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 1000000