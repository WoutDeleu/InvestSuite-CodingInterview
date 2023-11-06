from numbers import Number


def digit_counter(n: Number):
    """
    Count the number of digits in a positive integer.
    :param n: a positive integer
    :return: the number of digits in n
    """
    # Input-checker
    if not isinstance(n, Number):
        raise TypeError

    value: int = int(n)
    counter = 0
    while value >= 1 or value <= -1:
        value = int(value / 10)
        counter += 1

    return counter
