from polynomials import Polynomial
import pytest


@pytest.mark.parametrize(
    "f, p, fp", (
     ((1, -1, 1), 3, (1, -3, 6, -7, 6, -3, 1)),
     ((1, -1, 1), 2, (1, -2, 3, -2, 1)),
     ((1, -3, 4), 2, (1, -6, 17, -24, 16)))
    )
def test_pow(f, p, fp):
    assert Polynomial(f)**p == Polynomial(fp)
