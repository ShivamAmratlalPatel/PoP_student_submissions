import pytest


@pytest.mark.parametrize(
    "c, d, ans",
    [
        ((11, 2), (8, 9, 3, 1), "IntSet({1, 2, 3, 8, 9, 11})"),
        ((11, 2, 4, 1), (8, 9, 3, 1), "IntSet({1, 2, 3, 4, 8, 9, 11})"),
        ((), (), "IntSet()"),
    ],
)
def test_union(c, d, ans):
    from sets.verified_sets import IntSet

    a = IntSet(c)
    b = IntSet(d)
    t = a.union(b)
    assert str(t) == ans and isinstance(
        t, IntSet
    ), f"Expected union {ans} and type IntSet"


def test_union_subclass():
    from sets.verified_sets import IntSet

    a = IntSet(())
    with pytest.raises(TypeError):
        a.union(("a", "b"))


@pytest.mark.parametrize(
    "c, d, ans",
    [
        ((11, 2, 1, 9), (8, 9, 3, 1), "IntSet({9, 1})"),
        ((1, 2, 3, 4), (6, 5, 4, 3), "IntSet({3, 4})"),
        ((), (), "IntSet()"),
    ],
)
def test_intersection(c, d, ans):
    from sets.verified_sets import IntSet

    a = IntSet(c)
    b = IntSet(d)
    t = a.intersection(b)
    assert str(t) == ans and isinstance(
        t, IntSet
    ), f"Expected intersection {ans} and type IntSet"


def test_intersection_subclass():
    from sets.verified_sets import IntSet

    a = IntSet(())
    with pytest.raises(TypeError):
        a.intersection(("a", "b"))


@pytest.mark.parametrize(
    "c, d, ans",
    [
        ((11, 2), (8, 9, 3, 1), "IntSet({2, 11})"),
        ((11, 2, 4, 1), (8, 9, 3, 1), "IntSet({2, 11, 4})"),
        ((), (), "IntSet()"),
    ],
)
def test_difference(c, d, ans):
    from sets.verified_sets import IntSet

    a = IntSet(c)
    b = IntSet(d)
    t = a.difference(b)
    assert str(t) == ans and isinstance(
        t, IntSet
    ), f"Expected difference {ans} and type IntSet"


def test_difference_subclass():
    from sets.verified_sets import IntSet

    a = IntSet(())
    with pytest.raises(TypeError):
        a.difference(("a", "b"))


@pytest.mark.parametrize(
    "c, d, ans",
    [
        ((9, 1, 10), (2, 4, 5), "IntSet({1, 2, 4, 5, 9, 10})"),
        ((14, 2, 11), (8, 9, 3), "IntSet({2, 3, 8, 9, 11, 14})"),
        ((1, 2), (8, 9, 3), "IntSet({1, 2, 3, 8, 9})"),
    ],
)
def test_symmetric_difference(c, d, ans):
    from sets.verified_sets import IntSet

    a = IntSet(c)
    b = IntSet(d)
    t = a.symmetric_difference(b)
    assert str(t) == ans and isinstance(
        t, IntSet
    ), f"Expected symmetric difference {ans} and type IntSet"


def test_copy():
    from sets.verified_sets import IntSet

    a = IntSet((9, 1, 10))
    b = a.copy()
    assert str(b) == str(a) and isinstance(b, IntSet)


try:
    from sets.verified_sets import UniqueSet, UniquenessError
except ImportError:
    pass


def test_uniqueset_import():
    from sets.verified_sets import UniqueSet, UniquenessError


def test_uniquenesserror_subclass():
    assert issubclass(UniquenessError, KeyError)


def test_uniqueset_error():
    a = UniqueSet((1, 2, 3))
    with pytest.raises(UniquenessError):
        a.add(1)


def test_uniqueset_add():
    a = UniqueSet((1, 2, 3))
    a.add(4)
    assert str(a) == "UniqueSet({1, 2, 3, 4})" and isinstance(a, UniqueSet)


def test_uniqueset_union():
    a = UniqueSet((1, 2, 3))
    b = {1, 2}
    with pytest.raises(UniquenessError):
        a.union(b)
