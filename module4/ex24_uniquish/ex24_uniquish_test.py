from ex24_uniquish import Foo, Uniquish


def test_foo():
    f1 = Foo(10)
    f2 = Foo(10)
    f3 = Foo(10)

    s = {f1, f2, f3}

    assert len(s) == 1
    assert hash(f1) == hash(f2)
    assert hash(f2) == hash(f3)


def test_subclass_non_uniquish():
    class Bar():
        def __init__(self, x):
            self.x = x

    b1 = Bar(10)
    b2 = Bar(10)
    b3 = Bar(10)

    s = {b1, b2, b3}

    assert len(s) == 3
    assert hash(b1) != hash(b2)
    assert hash(b2) != hash(b3)


def test_subclass_uniquish():
    class Bar(Uniquish):
        def __init__(self, x):
            self.x = x

    b1 = Bar(10)
    b2 = Bar(10)
    b3 = Bar(10)

    s = {b1, b2, b3}

    assert len(s) == 1
    assert hash(b1) == hash(b2)
    assert hash(b2) == hash(b3)


def test_subclass_uniquish_two_arguments():
    class Bar(Uniquish):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    b1 = Bar(10, 'abc')
    b2 = Bar(10, 'abc')
    b3 = Bar(10, 'abcde')

    s = {b1, b2, b3}

    assert len(s) == 2
    assert hash(b1) == hash(b2)
    assert hash(b2) != hash(b3)


def test_subclass_uniquish_more_arguments():
    class Bar(Uniquish):
        def __init__(self, x, y, *args):
            self.x = x
            self.y = y
            self.args = args

    b1 = Bar(10, 'asta', ['some', 10, 'args'])
    b2 = Bar(10, 'asta', ['some', 10, 'args', 'more'])
    b3 = Bar(10, 'asta', ['some', 10, 'args'])
    s = {b1, b2, b3}

    assert len(s) == 2
    assert hash(b1) != hash(b2)
    assert hash(b1) == hash(b3)
