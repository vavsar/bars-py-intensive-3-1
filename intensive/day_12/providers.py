from dataclasses import dataclass

from django.contrib.auth.hashers import make_password
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


class TestTaskProvider(DjangoModelProvider):
    """
    Тестовый провайдер для задания
    """
    def save(self, obj):
        if getattr(obj, 'password'):
            password = make_password(getattr(obj, 'password'))
            setattr(obj, 'password', password)
        super().save(obj)
