import pytest
try:
    from sets.verified_sets import VerifiedSet, IntSet
except ImportError:
    pass


def test_sets_import():
    from sets.verified_sets import VerifiedSet, IntSet


def test_intset_subclass():
    assert issubclass(IntSet, VerifiedSet)


def test_validation_not_implemented():
    with pytest.raises(NotImplementedError):
        VerifiedSet((1,))


@pytest.mark.parametrize("s, a, ans", [
    ((1, 2), 3, 'IntSet({1, 2, 3})'),
    ((1, 2), 1, 'IntSet({1, 2})')
])
def test_add(s, a, ans):
    c = IntSet(s)
    c.add(a)
    assert (str(c) == ans and isinstance(c, IntSet)), \
        f"Expected set of {ans} but got {c}"


def test_add_subclass():
    a = IntSet(())
    with pytest.raises(TypeError):
        a.add("s")


@pytest.mark.parametrize("c, d, ans", [
    ((1, 2), (8, 9, 3), 'IntSet({1, 2, 3, 8, 9})'),
    ((8, 9, 3, 1), (11, 2), 'IntSet({1, 2, 3, 8, 9, 11})')
])
def test_update(c, d, ans):
    a = IntSet(c)
    b = IntSet(d)
    a.update(b)
    assert (str(a) == ans and isinstance(a, IntSet)), \
        f"Expected set of {ans} but got {a}"


def test_update_subclass():
    a = IntSet(())
    with pytest.raises(TypeError):
        a.update((1, "s"))


@pytest.mark.parametrize("c, d, ans", [
    ((11, 2), (8, 9, 3, 1), 'IntSet({1, 2, 3, 8, 9, 11})'),
    ((11, 2, 4, 1), (8, 9, 3, 1), 'IntSet({2, 3, 4, 8, 9, 11})')
])
def test_symmetric_difference_update(c, d, ans):
    a = IntSet(c)
    b = IntSet(d)
    a.symmetric_difference_update(b)
    assert (str(a) == ans and isinstance(a, IntSet)), \
        f"Expected set of {ans} but got {a}"


def test_symmetric_difference_subclass():
    a = IntSet(())
    with pytest.raises(TypeError):
        a.symmetric_difference_update((1, "s"))
