
def test_import():
    '''Ensure we can import isprime in the new location.'''
    from math_utils import isprime


def test_import_correct_function():
    from math_utils import isprime, primes

    assert primes.isprime is isprime, \
        "math_utils.isprime is not the same function as math_utils.primes.isprime"
