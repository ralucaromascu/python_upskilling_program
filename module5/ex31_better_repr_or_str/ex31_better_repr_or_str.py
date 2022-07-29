def replacement_str(self):
    return f'Replacement str, vars = {vars(self)}'


def replacement_repr(self):
    return f'Replacement repr, vars = {vars(self)}'


def better_repr(self):
    return f"Instance of {self.__class__.__name__}, vars = {self.__dict__}"


def betterrepr(newstr=None, newrepr=better_repr):
    def decorator(my_obj):
        if newstr:
            my_obj.__str__ = newstr
        if newrepr:
            my_obj.__repr__ = newrepr
        else:
            my_obj.__repr__ = better_repr
        return my_obj
    return decorator


if __name__ == '__main__':
    @betterrepr(newstr=replacement_str)
    class Foo1:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    f = Foo1(10, 20)
    print(str(f))


    @betterrepr(newrepr=replacement_repr)
    class Foo2:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    f2 = Foo2(10, 20)
    print(repr(f2))


    @betterrepr(newstr=replacement_str, newrepr=replacement_repr)
    class Foo:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    f3 = Foo(10, 20)
    print(repr(f3))
    print(str(f3))
