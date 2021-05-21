"""A module that implements the Deque type."""


class Deque:
    """Implement the Deque class."""

    def __init__(self, size):
        self.size = size
        self.list = [None] * size
        self.right = 0
        self.left = -1

    def append(self, x):
        """Append a value at the end of a deque."""
        store = self.list
        store[self.right % self.size] = x
        self.right += 1
        print(store)
        print(self.right)
        self.list = store
        return None

    def appendleft(self, x):
        """Append a value at the beginning of a deque."""
        store = self.list
        store[self.left % self.size] = x
        self.left -= 1
        print(store)
        print(self.left)
        self.list = store
        return None

    def pop(self):
        """Pop a value at the end of a deque."""
        store = self.list
        self.right -= 1
        print(self.right)
        value = store[self.right % self.size]
        print(value)
        store[self.right % self.size] = None
        self.list = store
        return value

    def popleft(self):
        """Pop a value at the beginning of a deque."""
        store = self.list
        print(store)
        for i in range(len(store)):
            if store[i]:
                break
        value = store[i % self.size]
        store[i % self.size] = None
        self.list = store
        print(store)
        return value

    def peek(self):
        """Return the value at the end of a deque."""
        store = self.list
        value = store[self.right - 1 % self.size]
        return value

    def peekleft(self):
        """Return the value at the beginning of a deque."""
        store = self.list
        value = store[self.left + 1 % self.size]
        return value

    def __len__(self):
        """Return the length of the deque."""
        print(self.list)
        store = [x for x in self.list if x]
        print(store)
        value = len(store)
        return value

    def __iter__(self):
        """Iterate the values of a deque."""
        return DequeIterator(self)


class DequeIterator:
    """Implement the Iterator of the Deque class."""

    def __init__(self, deque):
        self.here = deque
        self.count = 0

    def __iter__(self):
        """Iterate the values of a deque."""
        return self

    def __next__(self):
        """Iterate the values of a deque."""
        if self.count < self.here.size:
            next = self.here
            value = next.list[next.right % next.size]
            next.right += 1
            self.count += 1
            return value
        else:
            raise StopIteration
