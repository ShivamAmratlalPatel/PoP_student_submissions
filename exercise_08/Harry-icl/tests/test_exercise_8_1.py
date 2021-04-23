import pytest
import numpy as np
try:
    from groups.symmetric_groups import SymmetricGroup
except ImportError:
    pass


def test_group_import():
    from groups.symmetric_groups import SymmetricGroup


def test_symmetric_subclass():
    from example_code.groups import Group
    assert issubclass(SymmetricGroup, Group)


def test_symmetric_group_symbol():
    s = SymmetricGroup(2)
    assert s.symbol == 'S'


@pytest.mark.parametrize("n, a, b, ans", [
    (4, np.array([0, 2, 3, 1]), np.array([3, 2, 1, 0]), '[1 3 2 0]_S4'),
    (4, np.array([3, 2, 1, 0]), np.array([0, 2, 3, 1]), '[3 1 0 2]_S4'),
    (3, np.array([1, 2, 0]), np.array([2, 0, 1]), '[0 1 2]_S3')
])
def test_symmetric_group_operation(n, a, b, ans):
    s = SymmetricGroup(n)
    m = s(a) * s(b)
    assert str(m) == ans, \
        f"Expected answer of {ans} for mapping {a} and {b}"


@pytest.mark.parametrize("n, call", [
    (2, np.array([1, 2])),
    (2, 'g'),
    (4, np.array([0, 1, 2]))
])
def test_symmetric_group_validation(n, call):
    s = SymmetricGroup(n)
    with pytest.raises(ValueError):
        s(call)
