import re

import make_cake


def test_can_make_cake_should_be_defined():
    assert (
        hasattr(make_cake, "can_make_cake") is True
    ), "Variable 'can_make_cake' should be defined."


def test_can_make_cake_should_be_true():
    assert (
        make_cake.can_make_cake
    ), "Variable 'can_make_cake' should have value True."


def test_has_eggs_should_be_defined():
    assert (
        hasattr(make_cake, "has_eggs") is True
    ), "Variable 'has_eggs' should be defined."


def test_has_flour_should_be_defined():
    assert (
        hasattr(make_cake, "has_flour") is True
    ), "Variable 'has_flour' should be defined."


def test_has_sugar_should_be_defined():
    assert (
        hasattr(make_cake, "has_sugar") is True
    ), "Variable 'has_sugar' should be defined."


def test_can_make_cake_declaration_should_not_be_modified():
    with open(make_cake.__file__, "r") as f:
        code = f.read()
        last_line_regex = (
            "can_make_cake = has_eggs and has_flour and has_sugar *#"
        )
        assert (
            re.search(last_line_regex, code) is not None
        ), "Declaration of 'can_make_cake' shouldn't be modified."
