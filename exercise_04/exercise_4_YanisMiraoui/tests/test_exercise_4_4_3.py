import pytest
import numpy as np


def test_flip_vertical():
    from life import Pattern

    test_pattern = np.array([
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1]
    ])
    vflip_pattern = np.array([
        [0, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0]]
    )
    test_flipped = Pattern(test_pattern)
    assert np.array_equal(test_flipped.flip_vertical().grid, vflip_pattern), \
        "flip_vertical() transformation incorrect"
    assert np.array_equal(test_flipped.grid, test_pattern), \
        "flip_vertical() modifying original pattern"


def test_flip_horizontal():
    from life import Pattern

    test_pattern = np.array([
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1]
    ])
    hflip_pattern = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0]
    ])
    test_flipped = Pattern(test_pattern)
    assert np.array_equal(test_flipped.flip_horizontal().grid, hflip_pattern),\
        "flip_horizontal() transformation incorrect"
    assert np.array_equal(test_flipped.grid, test_pattern), \
        "flip_horizontal() modifying original pattern"


def test_flip_diag():
    from life import Pattern

    test_pattern = np.array([
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1]
    ])
    diag_pattern = np.array([
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 1]
    ])
    test_flipped = Pattern(test_pattern)
    assert np.array_equal(test_flipped.flip_diag().grid, diag_pattern), \
        "flip_diag() transformation incorrect  / wrong dimensions"
    assert np.array_equal(test_flipped.grid, test_pattern), \
        "flip_diag() modifying original pattern"


@pytest.mark.parametrize("n, transformation", [
    (1, np.array([
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 0]
    ])),
    (2, np.array([
        [1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0]
    ])),
    (3, np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 0]
    ]))
])
def test_rotations(n, transformation):
    from life import Pattern

    test_pattern = np.array([
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1]
    ])

    test_flipped = Pattern(test_pattern)
    assert np.array_equal(test_flipped.rotate(n).grid, transformation), \
        "rotate(n) transformation incorrect / wrong dimensions"
    assert np.array_equal(test_flipped.grid, test_pattern), \
        "rotate(n) modifying original pattern"
