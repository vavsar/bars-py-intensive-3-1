from abc import ABC, abstractmethod


class Item(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @abstractmethod
    def get_cost(self):
        pass


class Gift(Item):

    def get_cost(self):
        return 10


class Box(Item):

    def __init__(self):
        self._children = []
        self._cost = 5

    def add(self, item):
        self._children.append(item)
        item.parent = self

    def remove(self, item):
        self._children.remove(item)
        item.parent = None

    def is_composite(self):
        return True

    def get_cost(self):
        results = []
        for child in self._children:
            results.append(self._cost)
            results.append(child.get_cost())

        return sum(results)


def client_code(component):
    print(f"Total: {component.get_cost()}\n")


if __name__ == "__main__":
    simple = Gift()
    print("Price for a single item:")
    client_code(simple)

    tree = Box()

    branch1 = Box()
    branch1.add(Gift())
    branch1.add(Gift())

    branch2 = Box()
    branch2.add(Gift())

    tree.add(branch1)
    tree.add(branch2)

    print("Price for a composite box:")
    client_code(tree)
