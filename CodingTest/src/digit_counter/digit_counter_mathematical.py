from CodingTest.src.util import verify_input, extract_positive_integer


def digit_counter_mathematical(number) -> int:
    """
    Count the number of digits in a positive integer. Based on mathematical operations.

    Args:
        number: a numeric value / any Python type in the standard library that behaves as a number

    Returns:
        int: the number of digits needed to write the integer part of that number
    """

    # Handle and converts input to correct format
    verify_input(number)
    number: int = extract_positive_integer(number)

    # Special case: number is 0. Return 1.
    if number == 0:
        return 1

    # Count the number of integer digits
    counter = 0
    while number >= 1:
        number //= 10
        counter += 1

    return counter
