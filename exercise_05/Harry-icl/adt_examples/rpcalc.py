"""Module containing Reverse Polish Calculator."""

from numbers import Number
from math import sin, cos


class RPCalc:
    """Reverse Polish Calculator class."""

    def __init__(self, stack=None):
        """
        Create an instance of RPCalc.

        Parameters
        ----------
        stack(list): the stack of values to begin with.
        """
        if stack:
            self.stack = stack
        else:
            self.stack = []

    def push(self, n):
        """
        Push a value onto the stack.

        Parameters
        ----------
        n(str/int): the value to push to the stack.
        """
        if isinstance(n, Number):
            self.stack.append(n)
        elif n == "+":
            self.stack.append(self.stack.pop() + self.stack.pop())
        elif n == "-":
            self.stack.append(- self.stack.pop() + self.stack.pop())
        elif n == "*":
            self.stack.append(self.stack.pop() * self.stack.pop())
        elif n == "/":
            self.stack.append((1/self.stack.pop()) * self.stack.pop())
        elif n == "sin":
            self.stack.append(sin(self.stack.pop()))
        elif n == "cos":
            self.stack.append(cos(self.stack.pop()))
        else:
            raise ValueError("This is not a number or an operator.")
        print(self.stack)

    def pop(self):
        """Pop the top value off the stack."""
        return self.stack.pop()

    def peek(self):
        """Peek at the top value of the stack."""
        return self.stack[-1]

    def __len__(self):
        """Return the length of the stack."""
        return len(self.stack)
