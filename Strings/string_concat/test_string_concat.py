from . import string_concat
import re


def test_result_string_should_be_defined():
    assert (
        hasattr(string_concat, "result_string") is True
    ), "Variable 'result_string' should be defined."


def test_result_string_should_be_a_string():
    assert (
        isinstance(string_concat.result_string, str) is True
    ), "Variable 'result_string' should be a string."


def test_result_string_should_be_equal_to_concatenation():
    assert (
        string_concat.result_string == "Concatenation"
    ), "Variable 'result_string' should be equal to 'Concatenation'."


def test_a_should_be_defined():
    assert (
        hasattr(string_concat, "a") is True
    ), "Variable 'a' should be defined."


def test_a_should_be_a_string():
    assert (
        isinstance(string_concat.a, str) is True
    ), "Variable 'a' should be a string."


def test_a_should_be_equal_to_con():
    assert (
        string_concat.a == "Con"
    ), "Variable 'a' should be equal to 'Con'. DO NOT change its value."


def test_b_should_be_defined():
    assert (
        hasattr(string_concat, "b") is True
    ), "Variable 'b' should be defined."


def test_b_should_be_a_string():
    assert (
        isinstance(string_concat.b, str) is True
    ), "Variable 'b' should be a string."


def test_b_should_be_equal_to_enation():
    assert (
        string_concat.b == "enation"
    ), "Variable 'b' should be equal to 'enation'. DO NOT change its value."


def test_c_should_be_defined():
    assert (
        hasattr(string_concat, "c") is True
    ), "Variable 'c' should be defined."


def test_c_should_be_a_string():
    assert (
        isinstance(string_concat.c, str) is True
    ), "Variable 'c' should be a string."


def test_c_should_be_equal_to_cat():
    assert (
        string_concat.c == "cat"
    ), "Variable 'c' should be equal to 'cat'. DO NOT change its value."


def test_result_string_should_not_be_assigned_using_literal():
    with open(string_concat.__file__) as f:
        code = f.read()
        regex = "['\"]Concatenation['\"]"
        assert re.search(regex, code) is None, (
            "Variable 'result_string' should be assigned value using concatenation."
            "DO NOT write 'result_string = 'Concatenation'."
        )
