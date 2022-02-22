from tasks.common import MyException


def check_operand(self, var, operand):
    if operand == '+':
        return self.value + var
    elif operand == '-':
        return self.value - var
    elif operand == '*':
        return self.value * var
    elif operand == '/':
        try:
            return self.value / var
        except ZeroDivisionError:
            raise MyException
    else:
        return f'Операция {operand} не поддерживается'


class Value:
    def __init__(self, value):
        try:
            self.value = int(value)
        except MyException:
            raise TypeError('Необходимо ввести число')

    @property
    def get_result(self):
        return self.value

    def __add__(self, other):
        return check_operand(self, other, '+')

    def __sub__(self, other):
        return check_operand(self, other, '-')

    def __mul__(self, other):
        return check_operand(self, other, '*')

    def __truediv__(self, other):
        return check_operand(self, other, '/')
