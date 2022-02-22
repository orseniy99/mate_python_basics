import types

import get_tips_rating


def test_should_be_defined():
    assert (
        hasattr(get_tips_rating, "get_tips_rating") is True
    ), "Function get_tips_rating should be defined."


def test_should_be_a_function():
    assert (
        isinstance(get_tips_rating.get_tips_rating, types.FunctionType) is True
    ), "get_tips_rating should be a function."


def test_terrible_when_amount_is_0():
    assert (
        get_tips_rating.get_tips_rating(0) == "terrible"
    ), "Function get_tips_rating should return 'terrible' when amount is '0'."


def test_poor_when_amount_is_between_1_and_10_inclusive():
    assert (
        get_tips_rating.get_tips_rating(1) == "poor"
    ), "Function get_tips_rating should return 'poor' when amount is '1'."
    assert (
        get_tips_rating.get_tips_rating(10) == "poor"
    ), "Function get_tips_rating should return 'poor' when amount is '10.'"


def test_good_when_amount_is_between_11_and_20_inclusive():
    assert (
        get_tips_rating.get_tips_rating(11) == "good"
    ), "Function get_tips_rating should return 'good' when amount is '11'."
    assert (
        get_tips_rating.get_tips_rating(15) == "good"
    ), "Function get_tips_rating should return 'good' when amount is '15'."
    assert (
        get_tips_rating.get_tips_rating(20) == "good"
    ), "Function get_tips_rating should return 'good' when amount is '20'."


def test_great_when_amount_is_between_20_and_50_inclusive():
    assert (
        get_tips_rating.get_tips_rating(21) == "great"
    ), "Function get_tips_rating should return 'great' when amount is '21'."
    assert (
        get_tips_rating.get_tips_rating(25) == "great"
    ), "Function get_tips_rating should return 'great' when amount is '25'."
    assert (
        get_tips_rating.get_tips_rating(45) == "great"
    ), "Function get_tips_rating should return 'great' when amount is '45'."
    assert (
        get_tips_rating.get_tips_rating(50) == "great"
    ), "Function get_tips_rating should return 'great' when amount is '50'."


def test_excellent_when_amount_is_grater_than_50():
    assert (
        get_tips_rating.get_tips_rating(51) == "excellent"
    ), "Function get_tips_rating should return 'excellent' when amount is '51'."
    assert (
        get_tips_rating.get_tips_rating(65) == "excellent"
    ), "Function get_tips_rating should return 'excellent' when amount is '65'."
    assert (
        get_tips_rating.get_tips_rating(100) == "excellent"
    ), "Function get_tips_rating should return 'excellent' when amount is '100'."
    assert (
        get_tips_rating.get_tips_rating(110) == "excellent"
    ), "Function get_tips_rating should return 'excellent' when amount is '110'."
