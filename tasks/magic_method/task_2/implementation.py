class MathClock:
    """
    - сложение с числом увеличивает количество минут на входящее значение
    - вычитание числа уменьшает количество минут на входящее значение
    - умножение на число увеличивает количество часов на входящее значение
    - деление на число уменьшает количество часов на входящее значение

    метод *get_time* возвращает время в формате 'hh:mm'.

    При инстанцировании часы установлены в значение 00:00.
    """
    def __init__(self, minutes=0):
        self.minutes = minutes

    def __add__(self, other):
        self.minutes += other
        return self.minutes

    def __sub__(self, other):
        self.minutes -= other
        return self.minutes

    def __mul__(self, other):
        self.minutes = self.minutes + other * 60
        return self.minutes

    def __truediv__(self, other):
        self.minutes = self.minutes - other * 60
        return self.minutes

    def get_time(self):
        m = self.minutes % 60
        h = (self.minutes // 60) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")