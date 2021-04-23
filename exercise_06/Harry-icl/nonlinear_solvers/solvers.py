"""A module providing numerical solvers for nonlinear equations."""

import numpy as np


class ConvergenceError(Exception):
    """Exception raised if a solver fails to converge."""

    pass


def newton_raphson(f, df, x_0, eps=1.0e-5, max_its=20):
    """
    Solve a nonlinear equation using Newton-Raphson iteration.

    Solve f==0 using Newton-Raphson iteration.

    Parameters
    ----------
    f : function(x: float) -> float
        The function whose root is being found.
    df : function(x: float) -> float
        The derivative of f.
    x_0 : float
        The initial value of x in the iteration.
    eps : float
        The solver tolerance. Convergence is achieved when abs(f(x)) < eps.
    max_its : int
        The maximum number of iterations to be taken before the solver is taken
        to have failed.

    Returns
    -------
    float
        The approximate root computed using Newton iteration.
    """
    count = 0
    x_n1 = x_0
    x_n = x_0 + eps * 2
    while abs(f(x_n1)) >= eps:
        x_n = x_n1
        x_n1 = x_n - (f(x_n) / df(x_n))
        count += 1
        if count > max_its:
            raise ConvergenceError
    return x_n1


def bisection(f, x_0, x_1, eps=1.0e-5, max_its=20):
    """Solve a nonlinear equation using bisection.

    Solve f==0 using bisection starting with the interval [x_0, x_1]. f(x_0)
    and f(x_1) must differ in sign.

    Parameters
    ----------
    f : function(x: float) -> float
        The function whose root is being found.
    x_0 : float
        The left end of the initial bisection interval.
    x_1 : float
        The right end of the initial bisection interval.
    eps : float
        The solver tolerance. Convergence is achieved when abs(f(x)) < eps.
    max_its : int
        The maximum number of iterations to be taken before the solver is taken
        to have failed.

    Returns
    -------
    float
        The approximate root computed using bisection.
    """
    count = 0
    x_star = eps * 2
    if np.sign(f(x_0)) == np.sign(f(x_1)):
        raise ValueError("The values for x0 and x1 do not satisfy the "
                         "condition sign(f(x0)) != sign(f(x1)).")
    while abs(f(x_star)) >= eps:
        x_star = (x_0 + x_1) / 2
        if np.sign(f(x_star)) == np.sign(f(x_0)):
            x_0 = x_star
        else:
            x_1 = x_star
        count += 1
        if count > max_its:
            raise ConvergenceError
    return x_star


def solve(f, df, x_0, x_1, eps=1.0e-5, max_its_n=20, max_its_b=20):
    """Solve a nonlinear equation.

    solve f(x) == 0 using Newton-Raphson iteration, falling back to bisection
    if the former fails.

    Parameters
    ----------
    f : function(x: float) -> float
        The function whose root is being found.
    df : function(x: float) -> float
        The derivative of f.
    x_0 : float
        The initial value of x in the Newton-Raphson iteration, and left end of
        the initial bisection interval.
    x_1 : float
        The right end of the initial bisection interval.
    eps : float
        The solver tolerance. Convergence is achieved when abs(f(x)) < eps.
    max_its_n : int
        The maximum number of iterations to be taken before the newton-raphson
        solver is taken to have failed.
    max_its_b : int
        The maximum number of iterations to be taken before the bisection
        solver is taken to have failed.

    Returns
    -------
    float
        The approximate root.
    """
    try:
        return newton_raphson(f, df, x_0, eps, max_its_n)
    except(ConvergenceError):
        return bisection(f, x_0, x_1, eps, max_its_b)
