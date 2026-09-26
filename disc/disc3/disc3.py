def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n-2 > 0:
        return n * skip_factorial(n-2)
    else:
        return n
    
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.
    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7   
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        print(n % 10)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def g(k):
        if k < n:
            if n % k != 0:
                g(k + 1)
            else:
                return False
        else:
            return True
    return g(2)