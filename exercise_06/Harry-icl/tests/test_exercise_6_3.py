import pytest
import numpy as np
import math


def test_attempt_newton_failure(monkeypatch):
    from nonlinear_solvers.solvers import solve

    def mockreturn(f, g, x0, eps, k):
        from nonlinear_solvers.solvers import ConvergenceError
        raise ConvergenceError
    monkeypatch.setattr('nonlinear_solvers.solvers.newton_raphson', mockreturn)
    assert math.isclose(solve(lambda x: np.cos(x) - x,
                        lambda x: -np.sin(x) - 1, 0, 1, 1e-5, 15, 20),
                        0.7390899658203125, rel_tol=1e-6), \
        "expected fallback to bisection solution"
