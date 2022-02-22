import re
import sys
from io import StringIO

import pytest

import happy_birthday


def test_should_not_use_print_function_to_print_question():
    print_regex = r"^\s*print\(\s*['\"]What's your name\?['\"]\s*"
    with open(happy_birthday.__file__) as f:
        for line in f.readlines():
            assert not re.search(print_regex, line), (
                "Function 'happy_birthday' should not use 'print' function to print question. "
                "To print 'What's your name?' use function 'input' with one parameter"
            )


@pytest.mark.parametrize("name", ["Tom", "Jerry", "Epictetus"])
def test_happy_birthday(name):
    prev_stdin = sys.stdin
    string_io_stdin = StringIO(name)
    sys.stdin = string_io_stdin

    prev_stdout = sys.stdout
    string_io_stdout = StringIO()
    sys.stdout = string_io_stdout

    happy_birthday.happy_birthday()
    function_output = string_io_stdout.getvalue()

    assert function_output.startswith("What's your name?"), (
        "Function 'happy_birthday' should print question: 'What's your name?' "
        "using function 'input' with one parameter"
    )

    assert function_output.endswith(f"Happy birthday, {name}!\n"), (
        f"Function 'happy_birthday' should print congratulations: 'Happy birthday, {name}!' "
        f"when name is equal to {name}"
    )

    assert function_output == f"What's your name?Happy birthday, {name}!\n", (
        f"Function 'happy_birthday' should print only question and congratulations: "
        f"'What's your name?Happy birthday, {name}!\n' "
        f"when name is equal to {name}"
    )

    sys.stdout = prev_stdout
    sys.stdin = prev_stdin
