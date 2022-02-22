from tasks.common import MyException


class ClassFather:
    registered_list = []

    def register(self):
        raise MyException

    def get_name(self):
        raise MyException


class User1(ClassFather):
    _name = 'alex'

    def register(self):
        return self.registered_list.append(self._name)

    def get_name(self):
        if self._name in self.registered_list:
            return self._name
        else:
            raise MyException


class User2(ClassFather):
    _name = 'john'

    def register(self):
        return self.registered_list.append(self._name)

    def get_name(self):
        if self._name in self.registered_list:
            return self._name
        else:
            raise MyException
