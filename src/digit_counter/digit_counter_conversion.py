from CodingTest.src.util import verify_input, extract_positive_integer


def digit_counter_conversion(number) -> int:
    """
    Count the number of digits in a positive integer. Based on conversion to a string, and the length of that string.

    Args:
        number: a numeric value / any Python type in the standard library that behaves as a number

    Returns:
        int: the number of digits needed to write the integer part of that number
    """

    # Handle and converts input to correct format
    verify_input(number)
    number: int = extract_positive_integer(number)

    return len(str(number))
