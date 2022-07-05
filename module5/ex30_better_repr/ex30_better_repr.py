if __name__ == '__main__':
    @betterrepr
    class Foo(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


    f = Foo(10, [1, 2, 3, 4, 5])
    print(f)
