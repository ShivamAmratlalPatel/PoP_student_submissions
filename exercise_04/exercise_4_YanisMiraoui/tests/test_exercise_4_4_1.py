import pytest
import numpy as np


def test_import_pattern():
    """Ensure we can import class Pattern."""
    from life.life import Pattern


def test_pattern_grid():
    from life.life import Pattern, glider

    assert np.array_equal(Pattern(glider).grid, glider), \
        "Pattern.grid incorrectly defined"
