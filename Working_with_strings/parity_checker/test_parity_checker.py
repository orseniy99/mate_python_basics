import re
import sys
from io import StringIO

import pytest

import parity_checker


def test_should_not_use_print_function_to_print_question():
    print_regex = r"^\s*print\(\s*['\"]What's your name\?['\"]\s*"
    with open(parity_checker.__file__) as f:
        for line in f.readlines():
            assert re.search(print_regex, line) is None, (
                "Function 'parity_checker' should not use 'print' function to print question. "
                "To print 'What number do you want to check?' use function 'input' with one parameter"
            )


@pytest.mark.parametrize(
    "number,parity",
    [
        ("0", "Even"),
        ("2", "Even"),
        ("24", "Even"),
        ("100", "Even"),
        ("1", "Odd"),
        ("9", "Odd"),
        ("111", "Odd"),
        ("33", "Odd"),
    ],
)
def test_even_when_number_is_even(number, parity):
    prev_stdin = sys.stdin
    string_io_stdin = StringIO(number)
    sys.stdin = string_io_stdin

    prev_stdout = sys.stdout
    string_io_stdout = StringIO()
    sys.stdout = string_io_stdout

    parity_checker.parity_checker()
    function_output = string_io_stdout.getvalue()

    assert (
        function_output.startswith("What number do you want to check?") is True
    ), (
        "Function 'parity_checker' should print question: 'What number do you want to check?' "
        "using function 'input' with one parameter"
    )

    assert function_output.endswith(f"{parity}\n") is True, (
        f"Function 'parity_checker' should print '{parity}\n' "
        f"when number is equal to {number}"
    )

    assert function_output == f"What number do you want to check?{parity}\n", (
        f"Function 'parity_checker' should print only question and result: "
        f"'What number do you want to check?{parity}\n' "
        f"when number is equal to {number}"
    )

    sys.stdout = prev_stdout
    sys.stdin = prev_stdin
