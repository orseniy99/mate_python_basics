import assign_values


def test_brand_should_be_defined():
    assert (
            hasattr(assign_values, "brand") is True
    ), "Variable 'brand' should be defined"


def test_brand_should_be_equal_to_toyota():
    assert (
            assign_values.brand == "Toyota"
    ), "Variable 'brand' should be equal to 'Toyota'"


def test_price_should_be_defined():
    assert (
            hasattr(assign_values, "price") is True
    ), "Variable 'price' should be defined"


def test_price_should_be_equal_to_22500():
    assert (
            assign_values.price == 22500
    ), "Variable 'price' should be equal to 22500"


def test_is_sedan_should_be_defined():
    assert (
            hasattr(assign_values, "is_sedan") is True
    ), "Variable 'is_sedan' should be defined"


def test_is_sedan_should_have_value_true():
    assert assign_values.is_sedan, "Variable 'is_sedan' should have value True"


def test_owner_should_be_defined():
    assert (
            hasattr(assign_values, "owner") is True
    ), "Variable 'owner' should be defined"


def test_owner_should_be_none():
    assert assign_values.owner is None, "Variable 'owner' should be None"

