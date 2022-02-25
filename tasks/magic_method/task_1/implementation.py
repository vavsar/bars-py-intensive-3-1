class Multiplier:
    """
    Класс реализуает базовые арифметические операции с числами
    и аналогичными классами
    """

    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return str(self.value)

    def get_value(self):
        return int(self.value)

    def __add__(self, other):
        other = self.__check_operand_type(other)
        return Multiplier(self.value + other)

    def __sub__(self, other):
        other = self.__check_operand_type(other)
        return Multiplier(self.value - other)

    def __mul__(self, other):
        other = self.__check_operand_type(other)
        return Multiplier(self.value * other)

    def __truediv__(self, other):
        other = self.__check_operand_type(other)
        return Multiplier(self.value / other)

    @classmethod
    def __check_operand_type(cls, other):
        if type(other) == int:
            value = other
        elif isinstance(other, Multiplier):
            value = other.get_value()
        else:
            raise TypeError('Правый операнд может быть числом или Multiplier')
        return value


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        super().__init__(value * 100)


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        super().__init__(value * 1000)


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        super().__init__(value * 1000000)
