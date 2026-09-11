"""Write a function that returns True if a positive integer n is a prime number and False otherwise."""
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    k = 2
    if n == 1:
        return False
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


"""
If i is divisible by both 3 and 5, print fizzbuzz.
If i is divisible by 3 (but not 5), print fizz.
If i is divisible by 5 (but not 3), print buzz.
Otherwise, print the number i.
"""

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    k = 0
    while k < n:
        k += 1
        if k % 3 ==0 and k % 5 == 0:
            print("fizzbuzz")
            continue
        if k % 3 == 0:
            print("fizz")
            continue
        if k % 5 == 0: 
            print("buzz")
        else:
            print(k)


"""Write a function that returns the number of unique digits in a positive integer."""

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    def has_digit(n, k):
        """Returns whether k is a digit in n.

        >>> has_digit(10, 1)
        True
        >>> has_digit(12, 7)
        False
        """
        assert k >= 0 and k < 10
        "*** YOUR CODE HERE ***"
        while n > 0:
            if n % 10 == k:
                return True
            n //= 10
        return False

    k, total = 0, 0
    while k <= 9:
        if has_digit(n, k) == True:
            total += 1
        k += 1
    return total


"""Definition: A positive integer n is a repeating sequence of positive integer m if n is written by repeating the digits of m one or more times. For example, 616161 is a repeating sequence of 61, but 61616 is not."""


def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    end = n % pow(10, t)
    rest = n
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest //= pow(10,t)
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()