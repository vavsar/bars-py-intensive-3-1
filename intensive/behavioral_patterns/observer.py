from abc import ABC, abstractmethod


class AbstractBlogger(ABC):
    """
    Интферфейс издателя объявляет набор методов для управлениями подписчиками.
    """

    @abstractmethod
    def add_subscriber(self, observer):
        pass

    @abstractmethod
    def remove_subscriber(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Blogger(AbstractBlogger):

    _subscribers = []

    def add_subscriber(self, observer):
        self._subscribers.append(observer)

    def remove_subscriber(self, observer):
        self._subscribers.remove(observer)

    def notify(self):

        for subscriber in self._subscribers:
            subscriber.update()

    def some_business_logic(self):

        print(f"Только что опубликовал новую статью!")
        self.notify()


class AbstractSubscriber(ABC):

    @abstractmethod
    def update(self):
        pass


class SubscriberA(AbstractSubscriber):
    def update(self):
        print("Подписчик_A: Статью получил")


class SubscriberB(AbstractSubscriber):
    def update(self):
        print("Подписчик_В: Статью получил")


if __name__ == "__main__":
    blogger = Blogger()

    subscriber_a = SubscriberA()
    blogger.add_subscriber(subscriber_a)

    subscriber_b = SubscriberB()
    blogger.add_subscriber(subscriber_b)

    blogger.some_business_logic()

    blogger.remove_subscriber(subscriber_a)

    blogger.some_business_logic()
