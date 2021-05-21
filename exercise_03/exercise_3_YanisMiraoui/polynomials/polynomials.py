from numbers import Number

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
            selflist = list(self.coefficients)
            otherlist = list(other.coefficients)
            # Work out how many coefficient places the two polynomials have in common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = list(a - b for a, b in zip(selflist[:common], otherlist[:common]))
            # Append the high degree coefficients from the higher degree summand.
            rest = [-a for a in otherlist[common:]]
            coefs += selflist[common:] + rest
            
            return Polynomial(tuple(coefs))

        
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])

        else:
            return NotImplemented
    
    def __rsub__(self, other):

        if isinstance(other, Polynomial):
            selflist = list(self.coefficients)
            otherlist = list(other.coefficients)
            # Work out how many coefficient places the two polynomials have in common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = list(a - b for b, a in zip(selflist[:common], otherlist[:common]))
            # Append the high degree coefficients from the higher degree summand.
            rest = [-a for a in selflist[common:]]
            coefs += otherlist[common:] + rest
            
            return Polynomial(tuple(coefs))

        
        elif isinstance(other, Number):
            first = other - self.coefficients[0]
            coefs = [first]
            coefs += list(-a for a in self.coefficients[1:])
            return Polynomial(tuple(coefs))

        else:
            return NotImplemented

    def __mul__(self, other):

        if isinstance(other, Polynomial):
           
            m = self.degree() + 1
            n = other.degree() + 1
            prod = [0] * (m + n - 1);
            # Multiply two polynomials term by term 
            # Take ever term of first polynomial 
            for i in range(m): 
          
                # Multiply the current term of first  
                # polynomial with every term of  
                # second polynomial. 
                for j in range(n): 
                    prod[i + j] += self.coefficients[i] * other.coefficients[j] 
            
            return Polynomial(tuple(prod))

        
        elif isinstance(other, Number):
            coefs = tuple(other*a for a in self.coefficients)
            return Polynomial(coefs)

        else:
            return NotImplemented


    def __rmul__(self, other):
        return self * other
    
    def __pow__(self, other):
        
        if isinstance(other, Number):
            poly = self.coefficients
        
            for i in range(other-1): 
                self = self * Polynomial(poly)
            return self
        else:
            return NotImplemented

    def __call__(self, other):
        if isinstance(other, Number):
            deg = self.degree() + 1
            coeflist = list(self.coefficients)
            result = 0
            
            for i in range(deg):
                result += (other**i)*coeflist[i]
            
            return result
            
        else:
            return NotImplemented

    def dx(self):
        if isinstance(self, Polynomial):
            coefs = list(self.coefficients)
            deg = self.degree()
            if deg < 1 :
                deriv = [0]
            else :
                deriv =[]
                for i in range(1,deg+1):
                    deriv.append(i*coefs[i])
            return Polynomial(tuple(deriv))
        else: 
            return NotImplemented

def derivative(poly):
    return poly.dx()