"""Module that contains the components for the Game of Life."""

import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]])

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """
    A class to contain the Game of Life.

    Attributes
    ----------
    board(np.array): the current board.
    """

    def __init__(self, size):
        self.board = np.zeros((size, size))

    def play(self):
        """Start the game with the current board."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Do 1 move on the current game."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbour_count = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (
                    neighbour_count[i, j] == 3
                    or (
                        neighbour_count[i, j] == 2
                        and self.board[i, j]
                        )
                    ) else 0

    def __setitem__(self, key, value):
        """
        Set the value of the specified point on the board.

        Parameters
        ----------
        key(tuple): the location of the point.
        value(int): the value to set.
        """
        self.board[key] = value

    def show(self):
        """Show the current game."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, pattern, location):
        """
        Insert a pattern centered at the specified location.

        Parameters
        ----------
        pattern(Pattern): the pattern to insert.
        location(tuple): the center of where to insert it.
        """
        size = np.shape(pattern.grid)
        topleft = (location[0] - (size[0] - 1) // 2,
                   location[1] - (size[1] - 1) // 2)
        for i in range(size[0]):
            for j in range(size[1]):
                self[(topleft[0] + i, topleft[1] + j)] = pattern.grid[(i, j)]


class Pattern:
    """
    A class to contain patterns to place on the board for the Game of Life.

    Attributes
    ----------
    grid(np.array): the pattern.
    """

    def __init__(self, grid):
        self.grid = grid

    def flip_vertical(self):
        """Flip the pattern vertically (top to bottom)."""
        return Pattern(np.flipud(self.grid))

    def flip_horizontal(self):
        """Flip the pattern horizontally (left to right)."""
        return Pattern(np.fliplr(self.grid))

    def flip_diag(self):
        """Flip the pattern diagonally (top right to bottom left)."""
        return Pattern(self.grid.T)

    def rotate(self, n):
        """
        Rotate the pattern 90 degrees anticlockwise `n` times.

        Parameters
        ----------
        n(int): the number of times to rotate the pattern anticlockwise.
        """
        if n == 0:
            return self
        else:
            return self.flip_horizontal().flip_diag().rotate(n - 1)
