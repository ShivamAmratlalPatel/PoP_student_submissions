import pytest
try:
    from adt_examples.rpcalc import RPCalc
except ImportError:
    pass


def test_rpcalc_import():
    from adt_examples.rpcalc import RPCalc # noqa F401


def test_push_implemented():
    assert hasattr(RPCalc(), 'push'), \
        "push not implemented"


@pytest.mark.parametrize("elements", [
    ([1]),
    ([43.21]),
    ([1, 2, "+"]),
    ([1, 2, "-"]),
    ([1, 2, "*"]),
    ([1, 2, "/"]),
    ([0, "cos"]),
    ([0, "sin"])
])
def test_push(elements):
    calc = RPCalc()
    for element in elements:
        calc.push(element)


def test_pop_implemented():
    assert hasattr(RPCalc(), 'pop'), \
        "pop not implemented"


def test_length_implemented():
    assert hasattr(RPCalc(), '__len__'), \
        "RPCalc has no len special method"


def test_length():
    calc = RPCalc()
    calc.push(1)
    calc.push(2)
    calc.push("+")
    assert len(calc) == 1


def test_pop():
    calc = RPCalc()
    calc.push(1)
    calc.pop()
    assert not bool(calc), \
        "expected empty stack"


def test_peek_implemented():
    assert hasattr(RPCalc(), 'peek'), \
        "peek not implemented"


def test_peek():
    calc = RPCalc()
    calc.push(1)
    calc.peek()
    assert bool(calc), \
        "expected non-empty stack"


@pytest.mark.parametrize("expression, answer", [
    ([6, 2, '/', 2, 4, '*', '+'], 11),
    ([99, 11, "+", 8, 7, "+", "+"], 125),
    ([15, 7, 1, 1, "+", "-", "/", 3, "*", 2, 1, 1, "+", "+", "-"], 5),
    ([4, 7, "*", 5, 2, "*", "*"], 280),
    ([5, 8, 2, 0.2617993877991494, "*", "sin", "*", "+", 2,
      0.7853981633974483, "cos", "+", "/"], 3.3245825626631635)
])
def test_calculator_arithmetic(expression, answer):
    calc = RPCalc()
    for element in expression:
        calc.push(element)
    assert calc.peek() == answer, \
        f"expected an answer of {answer}"
