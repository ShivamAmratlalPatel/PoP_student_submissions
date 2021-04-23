from numbers import Number, Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + tuple(-x for x in other.coefficients[common:])
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        return Polynomial((0,)) - (self - other)
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            degree = self.degree()+other.degree()
            coefs = [0]*(degree + 1)
            for i in range(len(self.coefficients)):
                for j in range(len(other.coefficients)):
                    coefs[i + j] += self.coefficients[i]*other.coefficients[j]
            return Polynomial(tuple(coefs))
        
        elif isinstance(other, Number):
            return Polynomial(tuple(x*other for x in self.coefficients))

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        if isinstance(other, Integral):
            if other == 0:
                return Polynomial((1,))
            elif other > 0:
                return self * (self**(other - 1))
            else:
                return NotImplemented
        else:
            return NotImplemented
    
    def __call__(self, other):
        if isinstance(other, Number):
            return sum([self.coefficients[i]*(other**i) for i in range(len(self.coefficients))])

        else:
            return NotImplemented

    def dx(self):
        if self.degree() == 0:
            return Polynomial((0,))
        else:
            coefs = tuple(i*x for i, x in zip(range(1,len(self.coefficients)),self.coefficients[1:]))
            return Polynomial(coefs)
    
def derivative(f: Polynomial):
    return f.dx()
