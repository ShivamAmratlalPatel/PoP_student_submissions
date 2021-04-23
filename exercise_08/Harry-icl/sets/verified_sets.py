"""Verified Sets module."""

from numbers import Integral


class UniquenessError(KeyError):
    """Error to be raised in the case of non-unique elements in UniqueSet."""

    pass


class VerifiedSet(set):
    """Abstract class for Verified Sets."""

    def __init__(self, values):
        self._verify_set(values)
        set.__init__(self, values)

    def _verify(self, n):
        raise NotImplementedError

    def _verify_others(self, *others):
        for other_set in others:
            self._verify_set(other_set)

    def _verify_set(self, values):
        for elem in values:
            self._verify(elem)

    def add(self, elem):
        """
        Add an element to the set.

        Parameters
        ----------
        elem: The element to add.
        """
        self._verify(elem)
        return set.add(self, elem)

    def update(self, *others):
        """
        Add elements from all others.

        Parameters
        ----------
        *others(set): The sets from which to add elements.
        """
        self._verify_others(*others)
        return set.update(self, *others)

    def symmetric_difference_update(self, other):
        """
        Add only elements found in self and other.

        Parameters
        ----------
        other(set): The set with which to compare.
        """
        self._verify_set(other)
        return set.symmetric_difference_update(self, other)

    def union(self, *others):
        """
        Return the union of multiple sets.

        Parameters
        ----------
        *others(sets): The sets with which to union.

        Returns
        -------
        set: The result of the intersection.
        """
        self._verify_others(*others)
        return type(self)(set.union(self, *others))

    def intersection(self, *others):
        """
        Return the intersection of multiple sets.

        Parameters
        ----------
        *others(sets): The sets with which to intersect.

        Returns
        -------
        set: The result of the intersection.
        """
        self._verify_others(*others)
        return type(self)(set.intersection(self, *others))

    def difference(self, *others):
        """
        Return a set of elements that are in self but no others.

        Parameters
        ----------
        *others(sets): The sets with which to compare.

        Returns
        -------
        set: The result of the comparison
        """
        self._verify_others(*others)
        return type(self)(set.difference(self, *others))

    def symmetric_difference(self, other):
        """
        Return a set of elements in either self or other but not both.

        Parameters
        ----------
        other(set): The set with which to compare.

        Returns
        -------
        set: The result of the comparison.
        """
        self._verify_set(other)
        return type(self)(set.symmetric_difference(self, other))

    def copy(self):
        """
        Return a copy of the set.

        Returns
        -------
        set: A copy of self.
        """
        return type(self)(set.copy(self))


class IntSet(VerifiedSet):
    """Subclass of VerifiedSet for implementing sets of integers."""

    def _verify(self, n):
        if not isinstance(n, Integral):
            raise TypeError("IntSet expected an integer, got a %s" % type(n))


class UniqueSet(VerifiedSet):
    """Sets where only unique elements can be added."""

    def _verify(self, n):
        if n in self:
            raise UniquenessError
