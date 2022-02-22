import types

import can_buy_beer


def test_should_be_defined():
    assert (
        hasattr(can_buy_beer, "can_buy_beer") is True
    ), "Function can_buy_beer should be defined."


def test_should_be_a_function():
    assert (
        isinstance(can_buy_beer.can_buy_beer, types.FunctionType) is True
    ), "can_buy_beer should be a function."


def test_cannot_buy_beer_when_age_is_17():
    assert (
        can_buy_beer.can_buy_beer(17) == "You can not buy beer"
    ), "Function can_buy_beer should return negative answer when age is 17."


def test_can_buy_beer_when_age_is_18():
    assert (
        can_buy_beer.can_buy_beer(18) == "You can buy beer"
    ), "Function can_buy_beer should return positive answer when age is 18."


def test_can_buy_beer_when_age_is_50():
    assert (
        can_buy_beer.can_buy_beer(50) == "You can buy beer"
    ), "Function can_buy_beer should return positive answer when age is 50."


def test_cannot_buy_beer_when_age_is_less_than_18():
    assert (
        can_buy_beer.can_buy_beer(2) == "You can not buy beer"
    ), "Function can_buy_beer should return negative answer when age is 2."
    assert (
        can_buy_beer.can_buy_beer(12) == "You can not buy beer"
    ), "Function can_buy_beer should return negative answer when age is 12."


def test_can_buy_beer_when_age_is_greater_than_18():
    assert (
        can_buy_beer.can_buy_beer(19) == "You can buy beer"
    ), "Function can_buy_beer should return positive answer when age is 19"
    assert (
        can_buy_beer.can_buy_beer(23) == "You can buy beer"
    ), "Function can_buy_beer should return positive answer when age is 23"
