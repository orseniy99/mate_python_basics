import types

from . import double


def test_should_be_defined():
    assert (
        hasattr(double, "double") is True
    ), "Function double should be defined."


def test_should_be_a_function():
    assert (
        isinstance(double.double, types.FunctionType) is True
    ), "double should be a function."


def test_10_when_num_is_5():
    assert (
        double.double(5) == 10
    ), "Function double should return 10 when num is equal to 5"


def test_48_when_num_is_24():
    assert (
        double.double(24) == 48
    ), "Function double should return 48 when num is equal to 24"


def test_4_when_num_is_2():
    assert (
        double.double(2) == 4
    ), "Function double should return 4 when num is equal to 2"


def test_0_when_num_is_0():
    assert (
        double.double(0) == 0
    ), "Function double should return 0 when num is equal to 0"


def test_should_return_double_negative_when_num_is_negative():
    assert (
        double.double(-2) == -4
    ), "Function double should return -4 when num is equal to -2"
