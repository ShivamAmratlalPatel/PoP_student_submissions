from polynomials import Polynomial
import pytest


@pytest.mark.parametrize(
    "f, x, val",
    (((0, 1), 8, 8),
     ((2, 0, 3), -3, 29),
     ((4, 2), -11, -18))
    )
def test_call(f, x, val):
    assert Polynomial(f)(x) == val
