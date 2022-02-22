import types

import get_drinks


def test_should_be_defined():
    assert (
        hasattr(get_drinks, "get_drinks") is True
    ), "Function 'get_drinks' should be defined."


def test_should_be_a_function():
    assert (
        isinstance(get_drinks.get_drinks, types.FunctionType) is True
    ), "'get_drinks' should be a function."


def test_6_when_number_of_guests_is_3():
    assert (
        get_drinks.get_drinks(3) == 6
    ), "Function 'get_drinks' should return 6 when 'number_of_guests' is equal to 3."


def test_0_when_number_of_guests_is_0():
    assert (
        get_drinks.get_drinks(0) == 0
    ), "Function 'get_drinks' should return 0 when 'number_of_guests' is equal to 0."


def test_15_when_number_of_guests_is_5():
    assert (
        get_drinks.get_drinks(5) == 15
    ), "Function 'get_drinks' should return 15 when 'number_of_guests' is equal to 5."


def test_1_when_number_of_guests_is_1():
    assert (
        get_drinks.get_drinks(1) == 1
    ), "Function 'get_drinks' should return 1 when 'number_of_guests' is equal to 1."
