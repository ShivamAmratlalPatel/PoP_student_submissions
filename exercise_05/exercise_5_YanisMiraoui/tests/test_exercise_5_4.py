import pytest
import numpy as np

try:
    from adt_examples.fibonacci import Fib
except ImportError:
    pass


def test_fib_import():
    from adt_examples.fibonacci import Fib


def test_fib_iterator():
    x = Fib()
    assert hasattr(x, "__iter__"), "Fib has no __iter__ special method."


def test_fib_next():
    x = Fib()
    assert hasattr(x, "__next__"), "Fib has no __next__ special method."


@pytest.mark.parametrize(
    "n, fib_lst",
    [
        (5, [1, 2, 3, 5, 8]),
        (10, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
        (15, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]),
    ],
)
def test_fib_values(n, fib_lst):
    x = Fib()
    test_lst = [next(x) for i in range(n)]
    assert np.array_equal(
        test_lst, fib_lst
    ), "fibonacci sequences are not what is expected"


@pytest.mark.timeout(30e0, method="signal")
@pytest.mark.parametrize(
    "size,",
    [
        (1e7),
        (1e11),
    ],
)
def test_fibonacci_complexity(size):
    for n in Fib():
        if n >= size:
            break
    pass
