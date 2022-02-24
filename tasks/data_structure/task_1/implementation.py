class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, *args):
        self.array = args

    def __getitem__(self, key):
        return self.array[key]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        count = 0
        for number in self.array:
            if value == number:
                count += 1

        return count

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        if value not in self.array:
            raise ValueError

        for index, number in enumerate(self.array):
            if number == value:
                return index
