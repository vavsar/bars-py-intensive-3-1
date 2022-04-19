class BaseClass:
    """
    Базовый класс.
    """

    def make(self):
        pass


class BasePizza(BaseClass):
    """
    Базовая пицца
    """

    def make(self):
        return "Основа для пиццы"


class Decorator(BaseClass):
    """
    Базовый класс декоратора
    """

    def __init__(self, pizza):
        self._pizza = pizza

    @property
    def pizza(self):
        return self._pizza

    def make(self):
        return self._pizza.make()


class SauceDecorator(Decorator):
    """
    Добавляет соус
    """

    def make(self):
        return f"{self.pizza.make()} с томатным соусом"


class MozarellaDecorator(Decorator):
    """
    Добавляет моцареллу
    """

    def make(self):
        return f"{self.pizza.make()} посыпана моцареллой"


class BasilikDecorator(Decorator):
    """
    Добавляет моцареллу
    """

    def make(self):
        return f"{self.pizza.make()} украшена базиликом"


def print_custom(pizza):
    print(f"Выбрано: {pizza.make()}", end="\n")


if __name__ == "__main__":
    base = BasePizza()
    print_custom(base)

    sauce = SauceDecorator(base)
    print_custom(sauce)

    sauce_mozarella = MozarellaDecorator(sauce)
    base_mozarells = MozarellaDecorator(base)
    print_custom(base_mozarells)
    print_custom(sauce_mozarella)

    basilik_ingredient = BasilikDecorator(base)
    print_custom(basilik_ingredient)

    mozarella_basilik = MozarellaDecorator(basilik_ingredient)
    print_custom(mozarella_basilik)
