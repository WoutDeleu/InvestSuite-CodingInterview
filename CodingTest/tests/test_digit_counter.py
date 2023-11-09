from decimal import Decimal

from CodingTest.src.digit_counter import digit_counter_conversion, digit_counter_mathematical


def test_integers():
    assert digit_counter_conversion(12345) == 5
    assert digit_counter_conversion(100) == 3
    assert digit_counter_conversion(999) == 3

    assert digit_counter_mathematical(12345) == 5
    assert digit_counter_mathematical(100) == 3
    assert digit_counter_mathematical(999) == 3


def test_null():
    assert digit_counter_conversion(0) == 1
    assert digit_counter_mathematical(0) == 1


def test_negative():
    assert digit_counter_conversion(-12345) == 5
    assert digit_counter_conversion(-10) == 2
    assert digit_counter_conversion(-999) == 3

    assert digit_counter_mathematical(-12345) == 5
    assert digit_counter_mathematical(-10) == 2
    assert digit_counter_mathematical(-999) == 3


def test_floats():
    assert digit_counter_conversion(1.2345) == 1
    assert digit_counter_conversion(1.0) == 1
    assert digit_counter_conversion(0.999) == 1

    assert digit_counter_mathematical(1.2345) == 1
    assert digit_counter_mathematical(1.0) == 1
    assert digit_counter_mathematical(0.999) == 1

def test_complex():
    assert digit_counter_conversion(1 + 2j) == 1
    assert digit_counter_conversion(14.56 + 2j) == 2

    assert digit_counter_mathematical(1 + 2j) == 1
    assert digit_counter_mathematical(14.56 + 2j) == 2

def test_fractions():
    assert digit_counter_conversion(1 / 2) == 1
    assert digit_counter_conversion(7776 / 7) == 4

    assert digit_counter_mathematical(1 / 2) == 1
    assert digit_counter_mathematical(7776 / 7) == 4


def test_decimal():
    assert digit_counter_conversion(Decimal(211.2345)) == 3

    assert digit_counter_mathematical(Decimal(211.2345)) == 3

