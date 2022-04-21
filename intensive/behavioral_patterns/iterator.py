from collections.abc import Iterable, Iterator


class AllowedLettersIterator(Iterator):

    _position = None

    _reverse = False

    _allowed_letters = 'abcdef'

    def __init__(self, collection, reverse=False):
        self._collection = []
        for word in collection:
            if word[0].lower() in self._allowed_letters:
                self._collection.append(word)
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, collection=[]):
        self._collection = collection

    def __iter__(self):
        return AllowedLettersIterator(self._collection)

    def get_reverse_iterator(self):
        return AllowedLettersIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Apple")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()))
