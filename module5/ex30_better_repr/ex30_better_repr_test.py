from ex30_better_repr import betterrepr


def test_one_attribute():
    @betterrepr
    class Foo:
        def __init__(self, x):
            self.x = x

    f = Foo(10)
    assert str(f) == """Instance of Foo, vars = {'x': 10}"""


def test_two_attributes():
    @betterrepr
    class Foo:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(10, 20)
    assert str(f) == """Instance of Foo, vars = {'x': 10, 'y': 20}"""
