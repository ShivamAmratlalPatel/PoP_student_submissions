"""Module containing the Deque class."""


class Deque:
    """Deque class."""

    def __init__(self, size):
        """
        Create an instance of the Deque class.

        Parameters
        ----------
        size(int): the size of the buffer.
        """
        self.size = size
        self.buffer = [None]*size
        self.start = 0
        self.end = 0

    def append(self, x):
        """
        Append a value to the end of the Deque.

        Parameters
        ----------
        x: the value to append.
        """
        if self.buffer[self.end]:
            if self.start <= self.end:
                self.buffer = (self.buffer[self.start:self.end]
                               + [x]
                               + [None]*(self.size - 1))
            else:
                self.buffer = ([(item for item
                                 in (self.buffer[self.start:]
                                     + self.buffer[:self.end])
                                 if item is not None)]
                               + [x]
                               + [None]*(self.size - 1))
            self.start = 0
            self.end = len(self.buffer) - self.size + 1
        else:
            self.buffer[self.end] = x
            self.end = (self.end + 1) % len(self.buffer)

    def appendleft(self, x):
        """
        Append a value to the start of the Deque.

        Parameters
        ----------
        x: the value to append.
        """
        entry = (self.start - 1) % len(self.buffer)
        if self.buffer[entry]:
            if self.start <= self.end:
                self.buffer = ([x]
                               + self.buffer[self.start:self.end]
                               + [None]*(self.size - 1))
            else:
                self.buffer = ([x]
                               + [(item for item
                                   in (self.buffer[self.start:]
                                       + self.buffer[:self.end])
                                   if item is not None)]
                               + [None]*(self.size - 1))
            self.start = 0
            self.end = len(self.buffer) - self.size + 1
        else:
            self.buffer[entry] = x
            self.start = entry

    def pop(self):
        """Pop the last value from the Deque."""
        value = self.buffer[self.end - 1]
        self.buffer[self.end - 1] = None
        self.end = (self.end - 1) % len(self.buffer)
        return value

    def popleft(self):
        """Pop the first value from the Deque."""
        value = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % len(self.buffer)
        return value

    def peek(self):
        """Peek at the last value on the Deque."""
        return self.buffer[self.end - 1]

    def peekleft(self):
        """Peek at the first value on the Deque."""
        return self.buffer[self.start]

    def __len__(self):
        """Return the length of the Deque."""
        diff = (self.end - self.start) % len(self.buffer)
        if diff == 0:
            if self.buffer[self.start]:
                return len(self.buffer)
            else:
                return 0
        else:
            return diff

    def __iter__(self):
        """Iterate over the values in the Deque."""
        self.current = self.start
        self.returned = 0
        return self

    def __next__(self):
        """Return the next value in the Deque."""
        if self.returned >= len(self):
            raise StopIteration
        else:
            val = self.buffer[self.current]
            self.current = (self.current + 1) % len(self.buffer)
            self.returned += 1
            return val
