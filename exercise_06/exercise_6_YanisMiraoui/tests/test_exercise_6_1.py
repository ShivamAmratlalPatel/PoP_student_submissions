import pytest
import numpy as np
import numpy.testing as npt

try:
    from nonlinear_solvers.solvers import (
        newton_raphson,
        bisection,
        solve,
        ConvergenceError,
    )
except ImportError:
    pass


@pytest.mark.parametrize(
    "f, g, x0, eps, k, ans",
    [
        (lambda x: np.cos(x) - x, lambda x: -np.sin(x) - 1, 1, 1e-10, 4, 0.7390851332),
        (
            lambda x: np.sin(np.exp(x)) - 1,
            lambda x: np.exp(x) * np.cos(np.exp(x)),
            0.5,
            1e-20,
            25,
            0.45158270719343396,
        ),
        (lambda x: x ** 2 - 1, lambda x: 2 * x, 2, 1e-5, 5, 1.00000004646114741),
    ],
)
def test_working_newton(f, g, x0, eps, k, ans):
    from nonlinear_solvers.solvers import newton_raphson

    npt.assert_almost_equal(newton_raphson(f, g, x0, eps, k), ans, decimal=6)


@pytest.mark.parametrize(
    "f, g, x0, eps, k",
    [
        (lambda x: np.cos(x) - x, lambda x: -np.sin(x) - 1, 1, 1e-10, 2),
        (
            lambda x: np.sin(np.exp(x)) - 1,
            lambda x: np.exp(x) * np.cos(np.exp(x)),
            0.5,
            1e-20,
            20,
        ),
        (lambda x: x ** (1 / 3), lambda x: (1 / 3) * x ** (-2 / 3), 1, 1e-5, 5),
        (lambda x: x ** 2 - 1, lambda x: 2 * x, 2, 1e-5, 1),
    ],
)
def test_newton_convergence(f, g, x0, eps, k):
    from nonlinear_solvers.solvers import newton_raphson, ConvergenceError

    with pytest.raises(ConvergenceError):
        newton_raphson(f, g, x0, eps, k)
