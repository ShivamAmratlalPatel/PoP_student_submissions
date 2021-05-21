import pytest
import numpy as np
import numpy.testing as npt


@pytest.mark.parametrize(
    "f, x0, x1, eps, k, ans",
    [
        (lambda x: np.cos(x) - x, 0, 1, 1e-5, 17, 0.7390899658203125),
        (lambda x: 4 * x ** 3 - 1, -1, 2, 1e-5, 20, 0.6299591064453125),
        (lambda x: x ** 2 - 1, 0.825, 8.125, 1e-5, 25, 0.9999993324279786),
    ],
)
def test_working_bisction(f, x0, x1, eps, k, ans):
    from nonlinear_solvers.solvers import bisection

    npt.assert_almost_equal(bisection(f, x0, x1, eps, k), ans, decimal=6)


@pytest.mark.parametrize(
    "f, x0, x1, eps, k, ans",
    [
        (lambda x: np.cos(x) - x, 0, 1, 1e-5, 2, 0.7390899658203125),
        (lambda x: 4 * x ** 3 - 1, -1, 2, 1e-5, 4, 0.6299591064453125),
        (lambda x: x ** 2 - 1, 0.825, 8.125, 1e-5, 6, 0.9999993324279786),
    ],
)
def test_bisection_convergence(f, x0, x1, eps, k, ans):
    from nonlinear_solvers.solvers import bisection, ConvergenceError

    with pytest.raises(ConvergenceError):
        bisection(f, x0, x1, eps, k)


@pytest.mark.parametrize(
    "f, x0, x1, eps, k, ans",
    [
        (lambda x: np.cos(x) - x, 0.7, 0.73, 1e-5, 20, 0.7390899658203125),
        (lambda x: 4 * x ** 3 - 1, 1, 2, 1e-5, 20, 0.6299591064453125),
        (lambda x: x ** 2 - 1, 1.825, 8.125, 1e-5, 25, 0.9999993324279786),
    ],
)
def test_bisection_ivt(f, x0, x1, eps, k, ans):
    from nonlinear_solvers.solvers import bisection

    with pytest.raises(ValueError):
        bisection(f, x0, x1, eps, k)
