import declare_variables

def test_age_should_be_defined():
    assert (
        hasattr(declare_variables, "age") is True
    ), "Variable 'age' should be defined"


def test_age_should_be_an_integer():
    assert (
        isinstance(declare_variables.age, int) is True
    ), "Variable 'age' should be an integer"


def test_age_should_be_a_positive_number():
    assert (
        declare_variables.age > 0
    ), "Variable 'age' should be a positive number"