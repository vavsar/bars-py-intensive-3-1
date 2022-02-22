class Coffee:
    def __init__(self):
        self.coffee = "Coffee"

    def get_cappuchino(self):
        return f'{self.coffee} cappuchino'

    def get_latte(self):
        return f'{self.coffee} latee'

    def get_glasse(self):
        return f'{self.coffee} glasse'


if __name__ == '__main__':
    c1 = Coffee()
    print(c1.get_cappuchino())
    print(c1.get_latte())
    print(c1.get_glasse())
