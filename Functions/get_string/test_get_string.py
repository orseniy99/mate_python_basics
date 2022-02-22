from . import get_string
import re
import types


def test_should_be_defined():
    assert (
        hasattr(get_string, "get_string") is True
    ), "Function get_string should be defined."


def test_should_be_a_function():
    assert (
        isinstance(get_string.get_string, types.FunctionType) is True
    ), "get_string should be a function."


def test_should_return_hello_message():
    assert (
        get_string.get_string() == "Hello, Mate Academy!"
    ), "Function get_string should return 'Hello, Mate Academy!'."


def test_should_use_variable_greeting():
    with open(get_string.__file__) as f:
        assign_regex = "greeting *="
        code = f.read()
        assert (
            re.search(assign_regex, code) is not None
        ), "Variable greeting should be created inside get_string function."


def test_should_return_variable_greeting():
    with open(get_string.__file__) as f:
        return_regex = "return [\(\s]*greeting[\s\)]*"
        code = f.read()
        assert (
            re.search(return_regex, code) is not None
        ), "Function get_string should return variable greeting."
