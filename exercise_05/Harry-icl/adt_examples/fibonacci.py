"""Module containing Fibonacci class."""


class Fib:
    """Iterator class for fibonacci numbers."""

    def __init__(self):
        """Create instance of Fib class."""
        self.a = 1
        self.b = 2

    def __iter__(self):
        """Iterate over fibonacci numbers."""
        return self

    def __next__(self):
        """Find the next fibonacci number."""
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib
