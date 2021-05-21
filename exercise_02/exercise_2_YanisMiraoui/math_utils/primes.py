from math import sqrt

def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    root = int(sqrt(n))
    for i in range(2, root+2) :
        if n % i == 0 : 
            return False
    return True