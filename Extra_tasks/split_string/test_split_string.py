from split_string import split_string


def test_underscored_char_when_string_is_one_character():
    assert split_string("a") == ["a_"], (
        "Function 'split_string' should return an array with underscore item "
        "when input string length equal to one"
    )


def test_same_string_when_string_length_is_two():
    assert split_string("bb") == ["bb"], (
        "Function 'split_string' should return an array with one item "
        "when string length is equal to two"
    )


def test_even_length_string():
    assert split_string("abcdef") == ["ab", "cd", "ef"], (
        "Function 'split_string' should return an array of two-character strings "
        "when input string has even length"
    )
    assert split_string("acdc") == ["ac", "dc"], (
        "Function 'split_string' should return an array of two-character strings "
        "when string has even length"
    )


def test_odd_length_string():
    assert split_string("abcde") == ["ab", "cd", "e_"], (
        "Function 'split_string' should return an array of two-character strings "
        "with the underscore in the last item when string has odd length"
    )


def test_long_string_with_even_length():
    assert split_string("HYWqtNAMPDIpofCfvkyC") == [
        "HY",
        "Wq",
        "tN",
        "AM",
        "PD",
        "Ip",
        "of",
        "Cf",
        "vk",
        "yC",
    ], (
        "Function 'split_string' should return ['HY', 'Wq', 'tN', 'AM', 'PD', 'Ip', 'of', 'Cf', 'vk', 'yC'] "
        "when string is equal to 'HYWqtNAMPDIpofCfvkyC'"
    )


def test_long_string_with_odd_length():
    assert split_string("mtdUmBfzMoafzbrHijC") == [
        "mt",
        "dU",
        "mB",
        "fz",
        "Mo",
        "af",
        "zb",
        "rH",
        "ij",
        "C_",
    ], (
        "Function 'split_string' should return ['mt', 'dU', 'mB', 'fz', 'Mo', 'af', 'zb', 'rH', 'ij', 'C_'] "
        "when string is equal to 'mtdUmBfzMoafzbrHijC'"
    )


def test_string_with_underscore():
    assert split_string("abcd_") == ["ab", "cd", "__"], (
        "Function 'split_string' should return ['ab', 'cd', '__'] "
        "when string is equal to 'abcd_'"
    )
