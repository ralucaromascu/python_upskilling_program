import pytest
from ex36_tr import tr


def test_empty_source():
    with pytest.raises(TypeError):
        noop_tr = tr('', 'abcd')


def test_empty_result():
    with pytest.raises(TypeError):
        noop_tr = tr('abcd', '')


def test_simple():
    a_to_b_tr = tr('a', 'b')
    assert callable(a_to_b_tr)
    assert a_to_b_tr('abcdabcd') == 'bbcdbbcd'


def test_2_to_1():
    ab_to_c_tr = tr('ab', 'c')
    assert ab_to_c_tr('abcdabcd') == 'cccdcccd'


def test_remove():
    ab_to_c_tr = tr('ab', 'x')
    assert ab_to_c_tr('abcdabcd') == 'xxcdxxcd'


def test_1_to_2():
    a_to_bc_tr = tr('a', 'bc')
    assert a_to_bc_tr('abcdabcd') == 'bbcdbbcd'
