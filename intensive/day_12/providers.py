from dataclasses import dataclass
from recordpack.provider import DjangoModelProvider


@dataclass(init=False)
class GridItem:
    """
    Пример класса элемента грида
    """
    id: int
    name: str = ''

    def __init__(self, id=None, context=None) -> None:
        self.id = id
        self.name = str(id)
        super().__init__()


# Тестовый набор данных, чтобы не использовать БД
test_data = [GridItem(i) for i in range(1, 10)]


class TestTaskProvider(DjangoModelProvider):
    """
    Тестовый провайдер для задания
    """
    def save(self, obj):
        super().save(obj)
