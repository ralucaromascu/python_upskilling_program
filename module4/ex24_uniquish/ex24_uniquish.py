class Foo:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if type(other) is type(self):
            return self.x == other.x
        return False

    def __hash__(self):
        return hash(self.x)


class Uniquish:
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__dict__ == other.__dict__

    def __hash__(self):
        print(tuple(sorted(self.__dict__.items())))
        return hash(tuple(sorted(self.__dict__.items())))


class Bar(Uniquish):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    f1 = Foo(10)
    f2 = Foo(10)
    f3 = Foo(10)
    s = {f1, f2, f3}
    print(s)

    b1 = Bar(10, 'abc')
    b2 = Bar(10, 'abc')
    b3 = Bar(10, 'abc')
    s = {b1, b2, b3}
    print(s)
