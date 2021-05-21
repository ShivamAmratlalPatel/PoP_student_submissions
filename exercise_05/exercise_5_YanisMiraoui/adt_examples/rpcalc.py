"""A module that implements the Reversed Polish calculator."""

import numpy as np
from numbers import Number


class RPCalc:
    """Implement the Reversed Polish Calculator."""

    def __init__(self, stack=()):
        self.stack = stack

    def push(self, n):
        """Push the value into the calculator."""
        ops = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: y - x),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: y / x),
            "sin": (lambda x: np.sin(x)),
            "cos": (lambda x: np.cos(x)),
        }
        stack = list(self.stack)
        if isinstance(n, Number):
            stack.append(n)
        elif n in ["+", "-", "*", "/"]:
            number_1 = stack.pop()
            number_2 = stack.pop()
            result = ops[n](number_1, number_2)
            stack.append(result)
        elif n in ["sin", "cos"]:
            number_1 = stack.pop()
            result = ops[n](number_1)
            stack.append(result)
        self.stack = tuple(stack)
        print(stack)
        return None

    def pop(self):
        """Pop the value into the calculator."""
        stack = list(self.stack)
        value_pop = stack.pop()
        self.stack = tuple(stack)
        return value_pop

    def peek(self):
        """Return the last value of the calculator."""
        stack = list(self.stack)
        return stack[-1]

    def __len__(self):
        """Return the length of the calculator."""
        stack = list(self.stack)
        return len(stack)
