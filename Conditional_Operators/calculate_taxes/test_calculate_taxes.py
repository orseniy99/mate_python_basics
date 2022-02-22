import math
import types

import pytest

import calculate_taxes


def test_should_be_defined():
    assert (
        hasattr(calculate_taxes, "calculate_taxes") is True
    ), "Function calculate_taxes should be defined."


def test_should_be_a_function():
    assert (
        isinstance(calculate_taxes.calculate_taxes, types.FunctionType) is True
    ), "calculate_taxes should be a function."


def test_should_multiply_by_002_when_income_is_less_than_or_equal_to_1000():
    assert (
        calculate_taxes.calculate_taxes(900) == 18
    ), "Function calculate_taxes should return 18 when income is 900: 900 * 0.02 == 18."
    assert (
        calculate_taxes.calculate_taxes(999) == 19.98
    ), "Function calculate_taxes should return 19.98 when income is 999: 999 * 0.02 == 19.98."
    assert (
        calculate_taxes.calculate_taxes(999) == 19.98
    ), "Function calculate_taxes should return 19.98 when income is 999: 999 * 0.02 == 19.98."
    assert (
        calculate_taxes.calculate_taxes(1000) == 20
    ), "Function calculate_taxes should return 20 when income is 1000: 1000 * 0.02 == 20."


def test_should_multiply_by_003_when_income_is_between_1000_and_10000_inclusive():
    assert calculate_taxes.calculate_taxes(1001) == pytest.approx(
        30.03
    ), "Function calculate_taxes should return 30.03 when income is 1001: 1001 * 0.03 == 30.03"
    assert (
        calculate_taxes.calculate_taxes(5000) == 150
    ), "Function calculate_taxes should return 150 when income is 5000: 5000 * 0.03 == 150."
    assert (
        math.trunc(calculate_taxes.calculate_taxes(9999)) == 299
    ), "Function calculate_taxes should return 299.97 when income is 9999: 9999 * 0.03 == 299.97."
    assert (
        calculate_taxes.calculate_taxes(10000) == 300
    ), "Function calculate_taxes should return 300 when income is 10000: 10000 * 0.03 == 300."


def test_should_multiply_by_005_when_income_is_grater_than_10000():
    assert calculate_taxes.calculate_taxes(10001) == pytest.approx(
        500.05
    ), "Function calculate_taxes should return 500.05 when income is 10001: 10001 * 0.005 == 500.05."
    assert (
        calculate_taxes.calculate_taxes(10500) == 525
    ), "Function calculate_taxes should return 525 when income is 10000: 10000 * 0.005 == 525."
