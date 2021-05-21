"""A module that implement the fibonacci sequence."""


class Fib:
    """Implement the Fib class."""

    def __init__(self, value=0, previous=0):
        self.value = value
        self.previous = previous

    def __iter__(self):
        """Iterate the values of the fibonacci sequence."""
        return self

    def __next__(self):
        """Iterate the values of the fibonacci sequence."""
        if self.value == 0:
            previous = 0
            value = 1
        elif self.value == 1:
            previous = 1
            value = 2
        else:
            previous = self.value
            value = self.value + self.previous
        self.value = value
        self.previous = previous
        next = Fib(value, previous)
        return next.value
