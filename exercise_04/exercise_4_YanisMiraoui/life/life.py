"""Module to play to the Game of Life."""

import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

glider_gun = np.array(
    [
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
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
    ]
)


class Game:
    """A class to represent a game."""

    def __init__(self, size):
        self.board = np.zeros((size, size))

    def play(self):
        """Make the game run."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Move points through the square."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbourcount = convolve2d(self.board, stencil, mode="same")

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = (
                    1
                    if (
                        neighbourcount[i, j] == 3
                        or (neighbourcount[i, j] == 2 and self.board[i, j])
                    )
                    else 0
                )

    def __setitem__(self, key, value):
        """Set value to the key of the board."""
        self.board[key] = value

    def show(self):
        """Show the game."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap="binary")
        pyplot.show()

    def insert(self, pattern, pair):
        """Return a new Pattern whose rows are in reversed order."""
        mat = self.board
        n, m = pattern.grid.shape
        insert_mat = pattern.grid
        nb_left = m // 2
        nb_up = n // 2
        x = pair[0] - nb_left
        y = pair[1] - nb_up
        print(mat)
        print(insert_mat)
        for i in range(n):
            y = pair[1] - nb_up
            for j in range(m):
                print(insert_mat[i][j])
                print(i, j)
                print(x, y)
                mat[x][y] = insert_mat[i][j]
                print(mat)
                y += 1
            x += 1
        return mat


class Pattern:
    """A class to represent a pattern."""

    def __init__(self, grid):
        self.grid = grid

    def flip_vertical(self):
        """Return a new Pattern whose rows are in reversed order."""
        return Pattern(self.grid[::-1])

    def flip_horizontal(self):
        """Return a new Pattern whose rows are in reversed order."""
        return Pattern(self.grid[:, ::-1])

    def flip_diag(self):
        """Return a new Pattern which is the transpose of the original."""
        mat = np.transpose(self.grid)
        return Pattern(mat)

    def rotate(self, n):
        """Return a new Pattern rotated anticlockwise."""
        print(self.grid)
        mat = self
        for k in range(n):
            mat = mat.flip_diag()
            print(mat.grid)
            mat = mat.flip_vertical()
            print(mat.grid)
        return mat
