from tasks.common import MyException


class ClassFather:
    _name = None
    registered_list = []

    @classmethod
    def register(cls):
        if cls == ClassFather:
            raise MyException
        cls.registered_list.append(cls)

    @classmethod
    def get_name(cls):
        if cls not in cls.registered_list:
            raise MyException
        return cls._name


class User1(ClassFather):
    _name = 'alex'


class User2(ClassFather):
    _name = 'john'
