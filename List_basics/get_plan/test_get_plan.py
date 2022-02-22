from get_plan import get_plan


def test_30_percent():
    assert get_plan(1000, 6, 30) == [1300, 1690, 2197, 2856, 3712, 4825], (
        "Function 'get_plan' should return [1300, 1690, 2197, 2856, 3712, 4825] "
        "when current production is 1000, month is 6 and percent is 30"
    )


def test_50_percent():
    assert get_plan(500, 3, 50) == [750, 1125, 1687], (
        "Function 'get_plan' should return [1300, 1690, 2197, 2856, 3712, 4825] "
        "when current production is 1000, month is 6 and percent is 30"
    )


def test_list_of_zeros_when_current_production_is_0():
    assert get_plan(0, 5, 80) == [0, 0, 0, 0, 0], (
        "Function 'get_plan' should return all zeros "
        "when current production is equal to 0"
    )


def test_list_of_equal_numbers_when_percent_is_0():
    assert get_plan(1000, 3, 0) == [1000, 1000, 1000], (
        "Function 'get_plan' should return [1000, 1000, 1000] "
        "when current percent is equal to 0"
    )
