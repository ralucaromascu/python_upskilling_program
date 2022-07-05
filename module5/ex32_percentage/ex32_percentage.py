class Percentage:
    pass


if __name__ == '__main__':
    class Foo(object):
        participation = Percentage()


    f = Foo()
    f.participation = 500       # results in a PercentageTooHighError
    f.participation = -5        # results in a PercentageTooLowError
    f.participation = 'a'       # results in a PercentageNotANumber
    f.participation = 50.3
    print(f.participation)      # returns 50, the result of truncating to get an int

    f1 = Foo()
    f1.participation = 30

    f2 = Foo()
    f2.participation = 70

    print(f1.participation)     # prints 30, not 70
