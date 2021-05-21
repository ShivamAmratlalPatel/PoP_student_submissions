from numbers import Integral


class VerifiedSet(set):
    def __init__(self, value):
        super().__init__(value)
        self._verify(value)

    def _verify(self, value):
        raise NotImplementedError

    def add(self, element):
        self._verify(element)
        return super().add(element)

    def symmetric_difference_update(self, s):
        self._verify(s)
        return super().symmetric_difference_update(s)

    def update(self, *s):
        self._verify(*s)
        return super().update(*s)

    def union(self, *s):
        self._verify(*s)
        return type(self)(super().union(*s))

    def intersection(self, *s):
        self._verify(*s)
        return type(self)(super().intersection(*s))

    def difference(self, *s):
        self._verify(*s)
        return type(self)(super().difference(*s))

    def symmetric_difference(self, s):
        self._verify(s)
        return type(self)(super().symmetric_difference(s))

    def copy(self):
        return type(self)(super().copy())


class IntSet(VerifiedSet):

    def _verify(self, value):
        store = value
        if isinstance(value, Integral):
            store = [value]
        for i in store:
            if not (isinstance(i, Integral)):
                raise TypeError(
                    f"IntSet expected an integer, got a {type(value).__name__}"
                )


class UniqueSet(VerifiedSet):
    def __init__(self, value):
        super().__init__(value)
        self._verify(value)

    def _verify(self, value):
        print(self)
        print(value)
        if value in self or value == self:
            raise UniquenessError


class UniquenessError(KeyError):
    pass
