import pytest


@pytest.mark.parametrize("centre, radius, point, expected", [
    ((1., 0.), 2, (0.5, 0.5),  True),
    ((1., 3.), 1, (2.0, 2.0),  False),
    ((1.2, -0.1), 0.8, (1.2, 1.11),  False),
    ((11.2, -5.1), 2.8, (10.2, -3.11),  True),
])
def test_contains(centre, radius, point, expected):
    from shape import Circle

    assert (point in Circle(centre, radius)) == expected,\
        "test point is being incorrectly classified"
