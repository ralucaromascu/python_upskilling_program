import math


class PercentageTooHighError(Exception):
    pass


class PercentageTooLowError(Exception):
    pass


class PercentageNotANumber(Exception):
    pass


class Percentage:
    def __init__(self, value=100):
        self.value = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        return math.trunc(obj.__dict__.get(self.name, self.value))

    def __set__(self, obj, value):
        if type(value) != int and type(value) != float:
            raise PercentageNotANumber("the value for descriptor should be a number")
        elif value < 0:
            raise PercentageTooLowError("the value for descriptor should be higher tor equal to 0")
        elif value > 100:
            raise PercentageTooHighError("the value for descriptor should be lower or equal to 100")
        obj.__dict__[self.name] = value


if __name__ == '__main__':
    class Foo(object):
        participation = Percentage()


    f = Foo()
    f.participation = 500  # results in a PercentageTooHighError
    f.participation = -5  # results in a PercentageTooLowError
    f.participation = 'a'  # results in a PercentageNotANumber
    f.participation = 50.3
    print(f.participation)  # returns 50, the result of truncating to get an int

    f1 = Foo()
    f1.participation = 30

    f2 = Foo()
    f2.participation = 70
    print(f1.participation)  # prints 30, not 70
