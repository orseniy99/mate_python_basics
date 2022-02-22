from get_success_rate import get_success_rate


def test_60_when_statistics_is_11100():
    assert (
        get_success_rate("11100") == 60
    ), "Function 'get_success_rate' should return 60 when statistics is equal to 11100"


def test_60_when_statistics_is_1100():
    assert (
        get_success_rate("1100") == 50
    ), "Function 'get_success_rate' should return 50 when statistics is equal to 1100"


def test_0_when_statistics_is_00000():
    assert (
        get_success_rate("00000") == 0
    ), "Function 'get_success_rate' should return 0 when statistics is equal to 00000"


def test_100_when_statistics_is_111():
    assert (
        get_success_rate("111") == 100
    ), "Function 'get_success_rate' should return 100 when statistics is equal to 111"


def test_33_when_statistics_is_010():
    assert (
        get_success_rate("010") == 33
    ), "Function 'get_success_rate' should return 33 when statistics is equal to 010"


def test_13_when_statistics_is_0100000():
    assert (
        get_success_rate("0100000") == 14
    ), "Function 'get_success_rate' should return 14 when statistics is equal to 0100000"


def test_67_when_statistics_is_111100():
    assert (
        get_success_rate("111100") == 67
    ), "Function 'get_success_rate' should return 67 when statistics is equal to 111100"


def test_10_when_statistics_is_1000000000():
    assert (
        get_success_rate("1000000000") == 10
    ), "Function 'get_success_rate' should return 10 when statistics is equal to 1000000000"
