

def test_import():
    from shape import Circle  # noqa F401


def test_import_correct_function():
    from shape import Circle, circle

    assert circle.Circle is Circle, \
        "shape.Circle is not the same function as shape.circle.Circle"
