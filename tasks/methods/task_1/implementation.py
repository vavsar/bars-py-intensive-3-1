COFFEE_SORTS = {
    'Латте': ('Кофе', 'Молоко', 'Пенка'),
    'Мокко': ('Кофе', 'Молоко', 'Шоколад'),
    'Американо': ('Кофе', 'вода')
}


class Coffee:
    """
    Класс инициализирует ингредиенты в зависимости от введенного типа кофе
    """

    def __init__(self, coffee):
        if coffee in COFFEE_SORTS:
            self.ingredients = COFFEE_SORTS.get(coffee)
        else:
            raise AttributeError('Выберите "Латте", "Мокко" или "Американо"')
