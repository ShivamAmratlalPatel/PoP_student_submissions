from functools import singledispatch
import numbers


class Expression:
    def __init__(self, *operands):
        operandlist = [Number(o) if isinstance(o, numbers.Number)
                       else o for o in operands]
        self.operands = operandlist

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return Sub(other, self)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)

    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return Div(other, self)

    def __pow__(self, other):
        return Pow(self, other)

    def __rpow__(self, other):
        return Pow(other, self)


class Terminal(Expression):
    precedence = 3

    def __init__(self, value):
        super().__init__()
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class Operator(Expression):
    def __repr__(self):
        return type(self).__name__ + repr(self.operands)

    def __str__(self):
        first = str(self.operands[0])
        second = str(self.operands[1])

        if (
            type(self.operands[0]).__name__
            in ["Add", "Mul", "Sub", "Div", "Pow"]
           ):
            if self.operands[0].precedence < self.precedence:
                first = "(" + str(self.operands[0]) + ")"
        if (
            type(self.operands[1]).__name__
            in ["Add", "Mul", "Sub", "Div", "Pow"]
           ):
            if self.operands[1].precedence < self.precedence:
                second = "(" + str(self.operands[1]) + ")"
        return first + self.symbol + second


class Number(Terminal):
    def __init__(self, value):
        if isinstance(value, numbers.Number):
            super().__init__(value)


class Symbol(Terminal):
    def __init__(self, value):
        if isinstance(value, str):
            super().__init__(value)


class Add(Operator):
    symbol = " + "
    precedence = 0


class Mul(Operator):
    symbol = " * "
    precedence = 1


class Sub(Operator):
    symbol = " - "
    precedence = 0


class Div(Operator):
    symbol = " / "
    precedence = 1


class Pow(Operator):
    symbol = " ^ "
    precedence = 2


def postvisitor(expr, fn, **kwargs):
    stack = []
    visited = {}
    stack.append(expr)
    while stack:
        e = stack.pop()
        unvisited_children = []
        for o in e.operands:
            if o not in visited:
                unvisited_children.append(o)
        if unvisited_children:
            stack.append(e)
            stack += unvisited_children
        else:
            visited[e] = fn(e, *(visited[o] for o in e.operands), **kwargs)
    return visited[expr]


def previsitor(tree, fn, fn_parent=None):
    fn_out = fn(tree, fn_parent)

    for child in tree.children:
        previsitor(child, fn, fn_out)


@singledispatch
def differentiate(expr, *o, **kwargs):
    raise NotImplementedError(f"Cannot evaluate a {type(expr).__name__}")


@differentiate.register(Number)
def _(expr, *o, **kwargs):
    return Number(0.0)


@differentiate.register(Symbol)
def _(expr, *o, **kwargs):
    if str(expr) == kwargs["var"]:
        return Number(1.0)
    else:
        return Number(0.0)


@differentiate.register(Mul)
def _(expr, *o, **kwargs):
    # if we have d/dz(x*y)
    # y*dx/dz + x*dy/dz
    # 0[0] = dx/dz
    # 0[1] = dy/dz
    # y*o[0] + x*o[1]
    return o[0] * expr.operands[1] + o[1] * expr.operands[0]


@differentiate.register(Add)
def _(expr, *o, **kwargs):
    return o[0] + o[1]


@differentiate.register(Sub)
def _(expr, *o, **kwargs):
    return o[0] - o[1]


@differentiate.register(Div)
def _(expr, *o, **kwargs):
    return ((o[0] * expr.operands[1] - expr.operands[0] * o[1])
            / expr.operands[1] ** 2)


@differentiate.register(Pow)
def _(expr, *o, **kwargs):
    res = 0
    if kwargs["var"] == str(expr.operands[0]):
        res = ((expr.operands[1]) * expr.operands[0] **
               (expr.operands[1] - 1) * o[0])
    return res
