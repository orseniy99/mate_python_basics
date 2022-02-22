import re

from . import string_interpolation


def test_result_string_should_be_defined():
    assert hasattr(
        string_interpolation, "result_string"
    ), "Variable 'result_string' should be defined"


def test_result_string_should_be_a_string():
    assert isinstance(
        string_interpolation.result_string, str
    ), "Variable 'result_string' is not a string"


def test_result_string_should_be_equal_to_hello_world():
    assert (
        string_interpolation.result_string == "Hello, world!"
    ), "Variable 'result_string' is should be equal to 'Hello, world!' "


def test_a_should_be_defined():
    assert hasattr(
        string_interpolation, "a"
    ), "Variable 'a' should be defined."


def test_a_should_be_equal_to_hello():
    assert (
        string_interpolation.a == "Hello"
    ), "Variable 'a' should be equal to 'Hello'"


def test_b_should_be_defined():
    assert hasattr(
        string_interpolation, "b"
    ), "Variable 'b' should be defined."


def test_b_should_be_equal_to_world():
    assert (
        string_interpolation.b == "world"
    ), "Variable 'b' should be equal to 'world'"


def test_result_string_should_not_be_hardcoded():
    with open(string_interpolation.__file__) as f:
        code = f.read()
        regex = "['\"]Hello, world!['\"]"
        assert re.search(regex, code) is None, (
            "Variable 'result_string' should be assigned value using interpolation "
            "DO NOT write 'result_string = 'Hello, world!'"
        )


def test_result_string_should_not_be_assigned_using_concatenation():
    with open(string_interpolation.__file__) as f:
        code = f.read()

        concat_regex = "\w+\s*\+\s*['\"], ['\"]\s*\+\s*\w+\s*\+\s*['\"]!['\"]"
        assert re.search(concat_regex, code) is None, (
            "Variable 'result_string' should be assigned value using interpolation "
            "DO NOT write 'result_string = a + ', ' + b + '!'"
        )
