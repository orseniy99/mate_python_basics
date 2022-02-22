from . import declare_function
import types


def test_should_be_declared():
    assert (
        hasattr(declare_function, "my_function") is True
    ), "Function my_function should be declared."


def test_should_be_a_function():
    assert (
        isinstance(declare_function.my_function, types.FunctionType) is True
    ), "my_function should be a function."
