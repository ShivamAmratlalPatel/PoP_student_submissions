"""Symmetric Group module."""

from example_code.groups import Group


class SymmetricGroup(Group):
    """Class for operating on symmetric groups."""

    symbol = "S"

    def _validate(self, value):
        if sorted(value) != list(range(self.n)):
            raise ValueError("Element value must be a numpy array of integers "
                             "between 0 and %s" % (self.n - 1))

    def operation(self, a, b):
        """
        Perform the group operation on a and b.

        Parameters
        ----------
        a(np.ndarray): The first value.
        b(np.ndarray): The second value.

        Returns
        -------
        np.ndarray: The result of the group operation.
        """
        return a[b]
