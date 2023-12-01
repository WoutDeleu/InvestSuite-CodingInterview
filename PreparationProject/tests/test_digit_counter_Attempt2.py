from ..digit_counter_Attempt2 import digit_counter


def test_integers():
    assert digit_counter(100) == 3
    assert digit_counter(999) == 3


def test_smaller_than_zero():
    assert digit_counter(0.1) == 0


def test_fraction():
    assert digit_counter(3 / 2) == 1


def test_imaginary():
    assert digit_counter(3 + 2j) == 1


def test_float():
    assert digit_counter(3.1415) == 1


def test_negative():
    assert digit_counter(-10) == 2
