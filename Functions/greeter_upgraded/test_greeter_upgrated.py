import types

from . import greeter_upgraded


def test_should_be_defined():
    assert (
        hasattr(greeter_upgraded, "greeter") is True
    ), "Function greeter should be defined."


def test_should_be_a_function():
    assert (
        isinstance(greeter_upgraded.greeter, types.FunctionType) is True
    ), "greeter should be a function."


def test_good_morning_when_part_of_the_day_is_morning():
    assert (
        greeter_upgraded.greeter("Max", "morning") == "Good morning, Max!"
    ), (
        "Function greeter should return 'Good morning, Max' "
        "when name is equal to 'Max', part_of_the_day is equal to 'morning'."
    )


def test_good_night_when_part_of_the_day_is_night():
    assert (
        greeter_upgraded.greeter("Chipollino", "night")
        == "Good night, Chipollino!"
    ), (
        "Function greeter should return 'Good night, Chipollino' "
        "when name is equal to 'Chipollino', part_of_the_day is equal to 'night'."
    )
