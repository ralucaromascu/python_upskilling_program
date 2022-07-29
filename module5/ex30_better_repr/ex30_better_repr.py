def betterrepr(target_obj):

    def better_repr(self):
        return f"Instance of {self.__class__.__name__}, vars = {self.__dict__}"
    target_obj.__repr__ = better_repr
    return target_obj


if __name__ == '__main__':
    @betterrepr
    class Foo(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


    f = Foo(10, [1, 2, 3, 4, 5])
    print(f)
