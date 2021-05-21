"""A module providing numerical solvers for nonlinear equations."""


class ConvergenceError(Exception):
    """Exception raised if a solver fails to converge."""

    pass


def newton_raphson(f, df, x_0, eps=1.0e-5, max_its=20):
    """Solve a nonlinear equation using Newton-Raphson iteration.

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
    res = f(x_0)
    count = 0
    while abs(f(res)) >= eps:
        res = res - (f(res) / df(res))
        count += 1
        print(res)
        print(f(res))
        if count > max_its + 1:
            raise ConvergenceError
    return res


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
    x_star = (x_0 + x_1) / 2
    count = 0
    if (f(x_0) >= 0 and f(x_1) >= 0) or ((f(x_0) < 0 and f(x_1) < 0)):
        raise ValueError
    while abs(f(x_star)) >= eps:
        if (f(x_star) > 0 and f(x_0) > 0) or ((f(x_star) < 0 and f(x_0) < 0)):
            x_0 = x_star
        else:
            x_1 = x_star
        x_star = (x_0 + x_1) / 2
        count += 1
        if count > max_its + 1:
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
        The maximum number of iterations to be taken before the newton-raphson
        solver is taken to have failed.

    Returns
    -------
    float
        The approximate root.
    """
    try:
        result = newton_raphson(f, df, x_0, eps, max_its_n)
    except ConvergenceError:
        result = bisection(f, x_0, x_1, eps, max_its_b)
    finally:
        return result
