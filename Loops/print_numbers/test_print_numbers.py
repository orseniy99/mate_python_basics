import sys
import types
from io import StringIO

import print_numbers


def test_should_be_defined():
    assert (
        hasattr(print_numbers, "print_numbers") is True
    ), "Function 'print_numbers' should be defined."


def test_should_be_a_function():
    assert (
        isinstance(print_numbers.print_numbers, types.FunctionType) is True
    ), "'print_numbers' should be a function."


def test_prints_nothing_when_n_is_0():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    print_numbers.print_numbers(0)
    assert (
        captured_output.getvalue() == ""
    ), "Function 'print_numbers' should print nothing when n is equal to 0."
    sys.stdout = prev_stdout


def test_prints_0_when_n_is_1():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    print_numbers.print_numbers(1)
    assert (
        captured_output.getvalue() == "0\n"
    ), "Function 'print_numbers' should print '0\n' when n is equal to 1."
    sys.stdout = prev_stdout


def test_prints_from_1_to_5_when_n_is_5():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    print_numbers.print_numbers(5)
    expected_output = "".join([str(i) + "\n" for i in range(5)])
    assert captured_output.getvalue() == expected_output, (
        "Function 'print_numbers' should print numbers from 0 to 5 exclusive"
        "(each number on a separate line) when n is equal to 5."
    )
    sys.stdout = prev_stdout


def test_prints_from_1_to_10_when_n_is_10():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    print_numbers.print_numbers(10)
    expected_output = "".join([str(i) + "\n" for i in range(10)])
    assert captured_output.getvalue() == expected_output, (
        "Function 'print_numbers' should print numbers from 0 to 10 exclusive"
        "(each number on a separate line) when n is equal to 10"
    )

    sys.stdout = prev_stdout
