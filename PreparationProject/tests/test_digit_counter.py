from ..digit_counter import digit_counter


def test_base_scenarios():
    assert digit_counter(100) == 3
    assert digit_counter(999) == 3
    assert digit_counter(-10) == 2
    assert digit_counter(3.1415) == 1
    assert digit_counter(0.1) == 0

