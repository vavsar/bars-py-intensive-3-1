from dataclasses import dataclass
from recordpack.provider import ObjectListProvider


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


class TestProvider(ObjectListProvider):
    """
    Пример провайдера списковых данных
    """
    def _preprocess_record(self, obj, context=None):
        return obj

    def save(self, obj):
        # автогенерация ID для новых записей
        if obj.id is None:
            obj.id = len(test_data) + 1
        super().save(obj)
