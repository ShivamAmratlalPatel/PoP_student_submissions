import pytest


def test_import_Circle():
    from shape.circle import Circle  # noqa F401


def test_no_value():
    from shape.circle import Circle
    with pytest.raises(Exception):
        Circle()
