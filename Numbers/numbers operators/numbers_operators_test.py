import re

import numbers_operators


def test_a_should_be_defined():
    assert (
            hasattr(numbers_operators, "a") is True
    ), "Variable 'a' should be defined."


def test_a_should_be_an_integer():
    assert (
            isinstance(numbers_operators.a, int) is True
    ), "Variable 'a' should be an integer."


def test_a_should_be_equal_to_10():
    assert numbers_operators.a == 10, "Variable 'a' should be equal to 10."


def test_b_should_be_defined():
    assert (
            hasattr(numbers_operators, "b") is True
    ), "Variable 'b' should be defined."


def test_b_should_be_an_integer():
    assert (
            isinstance(numbers_operators.b, int) is True
    ), "Variable 'b' should be an integer."


def test_b_should_be_equal_to_2():
    assert numbers_operators.b == 2, "Variable 'b' should be equal to 2."


def test_addition_should_be_defined():
    assert (
            hasattr(numbers_operators, "addition") is True
    ), "Variable 'addition' should be defined."


def test_addition_should_be_an_integer():
    assert (
            isinstance(numbers_operators.addition, int) is True
    ), "Variable 'addition' should be an integer."


def test_addition_should_be_result_of_adding_a_and_b():
    addition_regex = "a\s*\+\s*b"
    with open(numbers_operators.__file__) as f:
        source = f.read()
        assert (
            re.search(addition_regex, source) is not None
        ), "Variable 'addition' should contain the result of adding 'a' and 'b'."


def test_addition_should_be_equal_to_12():
    assert (
            numbers_operators.addition == 12
    ), "Variable 'addition' should be equal to 12."


def test_subtraction_should_be_defined():
    assert (
            hasattr(numbers_operators, "subtraction") is True
    ), "Variable 'subtraction' should be defined."


def test_subtraction_should_be_an_integer():
    assert (
            isinstance(numbers_operators.subtraction, int) is True
    ), "Variable 'subtraction' should be an integer."


def test_subtraction_should_be_result_of_adding_a_and_b():
    subtraction_regex = "a\s*-\s*b"
    with open(numbers_operators.__file__) as f:
        source = f.read()
        assert (
            re.search(subtraction_regex, source) is not None
        ), "Variable 'subtraction' should contain the result of subtracting 'b' from 'a'."


def test_subtraction_should_be_equal_to_8():
    assert (
            numbers_operators.subtraction == 8
    ), "Variable 'subtraction' should be equal to 8."


def test_division_should_be_defined():
    assert (
            hasattr(numbers_operators, "division") is True
    ), "Variable 'division' should be defined."


def test_division_should_be_an_integer():
    assert (
            isinstance(numbers_operators.division, int) is True
    ), "Variable 'division' should be an integer."


def test_division_should_be_result_of_adding_a_and_b():
    division_regex = r"a\s*//\s*b"
    with open(numbers_operators.__file__) as f:
        source = f.read()
        assert (
            re.search(division_regex, source) is not None
        ), "Variable 'division' should contain the result of dividing 'a' by 'b'."


def test_division_should_be_equal_to_5():
    assert (
            numbers_operators.division == 5
    ), "Variable 'division' should be equal to 5."


def test_multiplication_should_be_defined():
    assert (
            hasattr(numbers_operators, "multiplication") is True
    ), "Variable 'multiplication' should be defined."


def test_multiplication_should_be_an_integer():
    assert (
            isinstance(numbers_operators.multiplication, int) is True
    ), "Variable 'multiplication' should be an integer."


def test_multiplication_should_be_result_of_adding_a_and_b():
    multiplication_regex = "a\s*\*\s*b"
    with open(numbers_operators.__file__) as f:
        source = f.read()
        assert (
            re.search(multiplication_regex, source) is not None
        ), "Variable 'multiplication' should contain the result of multiplication 'a' and 'b'."


def test_multiplication_should_be_equal_to_20():
    assert (
            numbers_operators.multiplication == 20
    ), "Variable 'multiplication' should be equal to 20."
