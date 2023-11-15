from numbers import Number
from fractions import Fraction
from decimal import Decimal


def digit_counter(n) -> int:
    """
    Count the number of digits in a positive integer.
    :param n: a numeric value / any Python type in the standard library that behaves as a number
    :return: the number of digits needed to write the integer part of that number
    """
    verify_input_type(n)

    # Get real part, in case of complex numbers
    n = n.real

    counter: int = 0
    while n >= 1 or n <= -1:
        # Each loop moves shifts all digits to the right
        n /= 10
        counter += 1

    return counter


def verify_input_type(n) -> None:
    """
    Verifies if input has the correct type (Fraction, Decimal, bool, Number)
    :param n: will be checked on the correct type
    :raises TypeError: if input doesn't have the correct type
    """
    if not isinstance(n, (Fraction, Decimal, bool, Number)):
        raise TypeError("Input must be of type Fraction, Decimal, bool, or Number.")
