import pytest
from ex32_percentage import Percentage, PercentageTooLowError, PercentageTooHighError, PercentageNotANumber


def test_default_is_100():
    class Foo():
        participation = Percentage()

    f = Foo()
    assert f.participation == 100


def test_override_default():
    class Foo():
        participation = Percentage(30)

    f = Foo()
    assert f.participation == 30


def test_can_set_to_an_int():
    class Foo():
        participation = Percentage(100)

    f = Foo()
    f.participation = 35
    assert f.participation == 35

    f.participation = 70
    assert f.participation == 70

    f.participation = 80.3
    assert f.participation == 80


def test_not_too_low_or_too_high():
    class Foo():
        participation = Percentage(100)

    f = Foo()
    with pytest.raises(PercentageTooLowError):
        f.participation = -10

    with pytest.raises(PercentageTooHighError):
        f.participation = 105


def test_not_a_number():
    class Foo():
        participation = Percentage(50)

    f = Foo()
    with pytest.raises(PercentageNotANumber):
        f.participation = 'a'
