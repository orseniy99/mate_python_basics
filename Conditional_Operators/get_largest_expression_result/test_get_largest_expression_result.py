import re
import types

import get_largest_expression_result


def test_should_be_defined():
    assert (
        hasattr(get_largest_expression_result, "get_largest_expression_result")
        is True
    ), "Function get_largest_expression_result should be defined."


def test_should_be_a_function():
    assert (
        isinstance(
            get_largest_expression_result.get_largest_expression_result,
            types.FunctionType,
        )
        is True
    ), "get_largest_expression_result should be a function."


def test_should_not_use_math_module():
    math_regex = "import math|from math"
    with open(get_largest_expression_result.__file__, "r") as f:
        code = f.read()
        assert (
            re.search(math_regex, code) is None
        ), "Function shouldn't use math module."


def test_should_not_use_else_keyword():
    else_regex = "[ ]else[: ]"
    with open(get_largest_expression_result.__file__, "r") as f:
        code = f.read()
        assert (
            re.search(else_regex, code) is None
        ), "Function shouldn't use else keyword."


def test_division_when_b_is_less_than_1():
    assert (
        get_largest_expression_result.get_largest_expression_result(5, 0.5)
        == 10
    ), "Function get_largest_expression should return 10 when a = 5, b = 0.5."


def test_subtraction_when_b_is_negative():
    assert (
        get_largest_expression_result.get_largest_expression_result(2, -2) == 4
    ), "Function get_largest_expression should return 4 when a = 2, b = -2."


def test_multiplication_when_a_and_b_are_negative():
    assert (
        get_largest_expression_result.get_largest_expression_result(-5, -5)
        == 25
    ), "Function get_largest_expression should return 25 when a = -5, b = -5."


def test_addition_when_a_is_negative_b_positive():
    assert (
        get_largest_expression_result.get_largest_expression_result(-2, 3) == 1
    ), "Function get_largest_expression should return 1 when a = -2, b = 3."


def test_two_operations_have_same_largest_result():
    assert (
        get_largest_expression_result.get_largest_expression_result(2, 2) == 4
    ), "Function get_largest_expression should return 4 when a = 2, b = 2."
