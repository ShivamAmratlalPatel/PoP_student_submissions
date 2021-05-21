from polynomials import Polynomial
import pytest


class SpikedError(Exception):
    '''A dummy error just for the purpose of testing.'''
    pass


@pytest.mark.parametrize(
    "f, g", (
        ((3, 2, 1), (2, 2)),
        ((-6, -11, 3, 2, 1), (-11, 6, 6, 4)),
        ((1, 1), (1,)),
        ((1,), (0,))
    )
)
def test_dx(f, g):
    assert Polynomial(f).dx() == Polynomial(g)


def test_derivative_exists():
    try:
        from polynomials import derivative  # noqa F401
    except ImportError:
        raise ImportError("polynomials.derivative not yet implemented,"
                          " or not imported in __init__.py")


def test_derivative_calls_dx():
    from polynomials import derivative

    def spiked_dx(self):
        raise SpikedError

    # Monkey patch Polynomial to check that dx is really called.
    old_dx = Polynomial.dx
    Polynomial.dx = spiked_dx

    try:
        derivative(Polynomial((1,)))
    except SpikedError:
        pass
    else:
        raise RuntimeError("derivative function did not call Polynomial.dx()")
    finally:
        Polynomial.dx = old_dx


@pytest.mark.parametrize(
    "f, g", (
        ((3, 2, 1), (2, 2)),
        ((-6, -11, 3, 2, 1), (-11, 6, 6, 4)),
        ((1, 1), (1,)),
        ((1,), (0,))
    )
)
def test_derivative(f, g):
    from polynomials import derivative
    assert derivative(Polynomial(f)) == Polynomial(g)
