from polynomials import Polynomial
import pytest


@pytest.mark.parametrize(
    "a, b, difference",
    (((0,), (0, 1), (0, -1)),
     ((2, 0, 3), (1, 2), (1, -2, 3)),
     ((4, 2), (10, 2, 4), (-6, 0, -4)))
    )
def test_sub(a, b, difference):
    assert Polynomial(a) - Polynomial(b) == Polynomial(difference)


def test_sub_scalar():
    assert Polynomial((2, 1)) - 3 == Polynomial((-1, 1))


def test_reverse_sub_scalar():
    assert 3 - Polynomial((2, 1)) == Polynomial((1, -1))
