import pytest
from ex39_immutable_me import ImmutableParent, ImmutableMeansImmutableError


def test_immutable():
    class ImmutableMe(ImmutableParent):
        pass

    im = ImmutableMe(x=111, y=222, z=[10, 20, 30])
    print(f"Before, vars(im) = {vars(im)}")
    im.z[2] = 'hello'

    with pytest.raises(ImmutableMeansImmutableError) as e:
        im.x = 999
    assert e.value.args[0] == 'Cannot change an attribute!'

    with pytest.raises(ImmutableMeansImmutableError) as e:
        im.a = 'Hello'
    assert e.value.args[0] == 'Cannot add an attribute!'

    assert vars(im) == {'x': 111, 'y': 222, 'z': [10, 20, 'hello']}
