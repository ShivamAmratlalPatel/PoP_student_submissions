import pytest
import numpy as np


@pytest.mark.parametrize("grid_size, coordinates, board", [
    (9, [4, 5], np.array([
        [0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 1., 1., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0.]
    ])),
    (5, [3, 1], np.array([
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0.],
        [0., 0., 1., 0., 0.],
        [1., 1., 1., 0., 0.]
    ])),
    (5, [1, 3], np.array([
        [0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 1.],
        [0., 0., 1., 1., 1.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]
    ]))
])
def test_insert(grid_size, coordinates, board):
    from life import Game, Pattern, glider

    g = Game(grid_size)
    g.insert(Pattern(glider), coordinates)
    assert np.array_equal(g.board, board)
