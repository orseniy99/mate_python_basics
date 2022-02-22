from io import StringIO
import sys
import importlib
from . import make_fruit_juice


def test_apples_should_be_defined():
    assert (
        hasattr(make_fruit_juice, "apples") is True
    ), "Variable 'apples' should be defined"


def test_apples_should_be_equal_to_4():
    assert (
        make_fruit_juice.apples == 4
    ), "Variable 'apples' should be equal to 4"


def test_pears_should_be_defined():
    assert (
        hasattr(make_fruit_juice, "pears") is True
    ), "Variable 'pears' should be defined"


def test_pear_should_be_equal_to_3():
    assert make_fruit_juice.pears == 3, "Variable 'pears' should be equal to 3"


def test_fruits_should_be_defined():
    assert (
        hasattr(make_fruit_juice, "fruits") is True
    ), "Variable 'fruits' should be defined"


def test_fruits_should_be_equal_to_7():
    assert (
        make_fruit_juice.fruits == 7
    ), "Variable 'fruits' should be equal to 7"


def test_should_print_can_make_juice():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    importlib.reload(make_fruit_juice)

    assert (
        captured_output.getvalue() == "You can make juice!\n"
    ), "Program should print 'You can make juice!'"

    sys.stdout = prev_stdout
