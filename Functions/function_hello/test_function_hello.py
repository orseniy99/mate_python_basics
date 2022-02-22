import sys
from io import StringIO
from . import function_hello
import types


def test_should_be_defined():
    assert (
        hasattr(function_hello, "hello") is True
    ), "Function hello should be defined"


def test_should_be_a_function():
    assert (
        isinstance(function_hello.hello, types.FunctionType) is True
    ), "hello should be a function"


def test_should_print_hello_world():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    function_hello.hello()

    assert (
        captured_output.getvalue() == "Hello, world!\n"
    ), "Function hello should print 'Hello, world!'"

    sys.stdout = prev_stdout
