import types

from . import greeter


def test_should_be_defined():
    assert (
        hasattr(greeter, "greeter") is True
    ), "Function greeter should be defined."


def test_should_be_a_function():
    assert (
        isinstance(greeter.greeter, types.FunctionType) is True
    ), "greeter should be a function."


def test_hi_max_when_name_is_max():
    assert (
        greeter.greeter("Max") == "Hi, Max!"
    ), "Function greeter should return 'Hi, Max!' when name is equal to 'Max'"


def test_hi_chipollino_when_name_is_chipolino():
    assert (
        greeter.greeter("Chipollino") == "Hi, Chipollino!"
    ), "Function greeter should return 'Hi, Chipollino!' when name is equal to 'Chipollino'"
