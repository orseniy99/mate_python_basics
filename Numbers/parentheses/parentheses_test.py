import re
import parentheses


def test_parentheses():
    assert (
            hasattr(parentheses, "expression") is True
    ), "Variable 'expression' should be defined"
    assert (
            isinstance(parentheses.expression, int) is True
    ), "Variable 'expression' should be an integer"
    assert parentheses.expression == 10, "Variable 'expression' is not 10"

    with open(parentheses.__file__, "r") as f:
        code = f.read()
        expression_regex = "[\n]*^[\(\) ]*expression[\(\) ]*=[\(\) ]*10[\(\) ]*\*[\(\) ]*7[\(\) ]*\+[\(\) ]*8[\(\) ]*-[\(\) ]*11[\(\) ]*//[\(\) ]*4[\(\) \n]*$"
        assert (
            re.search(expression_regex, code) is not None
        ), "You should only add parentheses to expression. Do not modify it."
