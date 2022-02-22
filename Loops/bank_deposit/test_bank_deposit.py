import math

from bank_deposit import calculate_profit


def test_one_year_period():
    assert calculate_profit(1000, 5, 1) == 50, \
        "Function 'calculate_profit' should return 50 " \
        "when amount is 1000, percent is 5 and period is 1"


def test_longer_period():
    assert math.trunc(calculate_profit(12500, 3, 12)) == 5322, \
        "Function 'calculate_profit' should return 5322 " \
        "when amount is 12500, percent is 3 and period is 12"


def test_amount_is_0():
    assert calculate_profit(0, 3, 1) == 0, \
        "Function 'calculate_profit' should return 0 " \
        "when amount is 0"


def test_percent_is_0():
    assert calculate_profit(10000, 0, 10) == 0, \
        "Function 'calculate_profit' should return 0 " \
        "when percent is 0"


def test_period_is_0():
    assert calculate_profit(10000, 100, 0) == 0, \
        "Function 'calculate_profit' should return 0 " \
        "when period is 0"


def test_float_percent():
    assert math.trunc(calculate_profit(1000, 5.5, 7)) == 454, \
        "Function 'calculate_profit' should return 454 " \
        "when amount is 1000, percent is 5.5, period is 0"
