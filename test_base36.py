import pytest
import base36


@pytest.mark.parametrize('number,value', [
    (3951668550778163018, 'u0tplaqiv70q'),
    (1024, 'sg'),
    (1843067821, 'uhbc8d'),
])
def test_dumps_and_loads(number, value):
    assert base36.dumps(number) == value
    assert base36.dumps(-number) == '-' + value
    assert base36.loads(value) == number
    assert base36.loads('-' + value) == -number


def test_failure():
    with pytest.raises(TypeError):
        base36.dumps('wrong type')
