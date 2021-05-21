from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    notation = "S"
    symbol = "S"

    def _validate(self, value):
        """Ensure that value is a legitimate element value in this group."""
        value = np.asarray(list(value))
        if not (
            isinstance(value, np.ndarray)
            and np.shape(value)[0] == self.n
            and np.amax(value) == self.n - 1
            and np.amin(value) == 0
        ):
            raise ValueError(
                "Element value must be an numpy array"
                f" with elements in the range [0, {self.n})"
            )

    def operation(self, a, b):
        result = np.copy(a)
        for i in range(np.size(a)):
            result[i] = a[b[i]]
        return result
