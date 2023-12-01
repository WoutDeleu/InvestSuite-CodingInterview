from decimal import Decimal
from fractions import Fraction
from numbers import Number


def verify_input(number) -> None:
    """
    Verifies if input has the correct type (Fraction, Decimal, Number)

    Args:
        number: will be checked on correct type

    Raises:
         TypeError: if input doesn't have the correct type
    """

    if not isinstance(number, (Fraction, Decimal, complex, Number)):
        raise TypeError("Input must be of type Fraction, Decimal, complex or Number.")


def extract_positive_integer(number) -> int:
    """
    Function which extract the real part (in case of complex numbers), and converts it to a positive integer.

    Args:
        number: a numeric value / any Python type in the standard library that behaves as a number

    Returns:
        int: the real, positive integer part of the number

    """
    return int(abs(number.real))
