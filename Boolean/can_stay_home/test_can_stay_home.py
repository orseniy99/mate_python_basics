import re

import can_stay_home


def test_can_stay_home_should_be_defined():
    assert (
        hasattr(can_stay_home, "can_stay_home") is True
    ), "Variable can_stay_home should be defined."


def test_can_stay_home_should_be_bool():
    assert (
        isinstance(can_stay_home.can_stay_home, bool) is True
    ), "Variable can_stay_home should be bool."


def test_can_stay_home_should_be_true():
    assert (
        can_stay_home.can_stay_home
    ), "Variable can_stay_home should have value True."


def test_is_holiday_should_be_defined():
    assert (
        hasattr(can_stay_home, "is_holiday") is True
    ), "Variable is_holiday should be defined."


def test_is_vacation_should_be_defined():
    assert (
        hasattr(can_stay_home, "is_vacation") is True
    ), "Variable is_vacation should be defined."


def test_only_one_variable_should_be_changed():
    assert (
        can_stay_home.is_holiday and can_stay_home.is_vacation
    ) is False, "Only one variable should be changed."


def test_can_stay_home_declaration_should_not_be_modified():
    with open(can_stay_home.__file__, "r") as f:
        code = f.read()
        last_line_regex = "can_stay_home = is_holiday or is_vacation *#"
        assert (
            re.search(last_line_regex, code) is not None
        ), "Declaration of 'can_stay_home' shouldn't be modified."