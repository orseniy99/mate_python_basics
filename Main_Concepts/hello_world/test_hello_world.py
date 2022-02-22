from io import StringIO
import sys

def test_hello_world():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    from . import hello_world

    assert captured_output.getvalue() == "Hello, world!\n"

    sys.stdout = prev_stdout
