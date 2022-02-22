from get_string_length import get_string_length


def test_0_when_empty_string():
    assert (
        get_string_length("") == 0
    ), "Function 'get_string_length' should return 0 when string is empty"


def test_1_when_string_is_a_single_character():
    assert (
        get_string_length("b") == 1
    ), "Function 'get_string_length' should return 1 when string is equal to 'b'"


def test_1_when_string_is_a_single_upper_character():
    assert (
        get_string_length("B") == 1
    ), "Function 'get_string_length' should return 1 when string is equal to 'B'"


def test_string_with_digits():
    assert (
        get_string_length("q1w2e3r4r5") == 10
    ), "Function 'get_string_length' should return 10 when string is equal to 'q1w2e3r4r5'"


def test_long_string():
    assert (
        get_string_length("qwertyqwerty") == 12
    ), "Function 'get_string_length' should return 12 when string is equal to 'qwertyqwerty'"


def test_string_with_special_symbols():
    assert (
        get_string_length("!@#$") == 4
    ), "Function 'get_string_length' should return 4 when string is equal to '!@#$'"
