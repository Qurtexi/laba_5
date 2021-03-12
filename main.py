import math as m

class X:
    def __init__(self, _x1, _x2):
        self.x1 = _x1
        self.x2 = _x2

    def __del__(self):
        print("Удалено")

    def smotr(self):
        print('x1: ', self.x1,
              '\nx2: ', self.x2)

    def izmen(self):
        self.x1 = int(input('New x1: '))
        self.x2 = int(input('New x2: '))

class Y(X):

    def __init__(self, _x1, _x2, _y):
        super().__init__(_x1, _x2)
        self.y = _y

    def run(self):
        return m.pow((self.x1 * self.x2 * self.y), 2)

    def smotr(self):
        super().smotr()
        print('y: ', self.y)

    def izmen(self):
        super().izmen()
        self.y = int(input('New y: '))


if __name__ == '__main__':
    x1 = int(input("Введите x1: "))
    x2 = int(input("Введите x2: "))
    y = int(input("Введите y: "))
    Y = Y(x1, x2, y)
    print("Резултат вычислений: ", Y.run())

