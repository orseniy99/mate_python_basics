import re

import make_tea


def test_can_make_tea_should_be_defined():
    assert (
        hasattr(make_tea, "can_make_tea") is True
    ), "Variable 'can_make_tea' is not defined."


def test_can_make_tea_should_be_false():
    assert (
        not make_tea.can_make_tea
    ), "Variable 'can_make_tea' should be False."


def test_is_hot_water_should_be_defined():
    assert (
        hasattr(make_tea, "is_water_hot") is True
    ), "Variable 'is_water_hot' should be defined."


def test_have_tea_should_be_defined():
    assert (
        hasattr(make_tea, "have_tea") is True
    ), "Variable 'have_tea' should be defined."


def test_only_one_variable_should_be_changed():
    assert (
        make_tea.is_water_hot or make_tea.have_tea
    ) is True, "Only one variable should be changed."


def test_can_make_tea_declaration_should_not_be_changed():
    with open(make_tea.__file__, "r") as f:
        code = f.read()
        last_line_regex = "can_make_tea = is_water_hot and have_tea *#"
        assert (
            re.search(last_line_regex, code) is not None
        ), "Declaration of 'can_make_tea' shouldn't be modified."
