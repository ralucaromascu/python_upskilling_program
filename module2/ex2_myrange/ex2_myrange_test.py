import pytest
import ex2_myrange


def test_myrange2_is_a_list():
    output = ex2_myrange.myrange2(10)
    assert type(output) is list


@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10, 20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10, 20, 2))),
    (10, 20, 3, list(range(10, 20, 3)))
])
def test_myrange2(first, second, third, output):
    if third:
        assert ex2_myrange.myrange2(first, second, third) == output
    else:
        assert ex2_myrange.myrange2(first, second) == output


def test_myrange3_is_a_generator():
    output = ex2_myrange.myrange3(10)
    assert iter(output) is output


@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10, 20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10, 20, 2))),
    (10, 20, 3, list(range(10, 20, 3)))
])
def test_myrange3(first, second, third, output):
    if third:
        assert list(ex2_myrange.myrange3(first, second, third)) == output
    else:
        assert list(ex2_myrange.myrange3(first, second)) == output
