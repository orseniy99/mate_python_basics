from get_speed_statistic import get_speed_statistic


def test_zeros_when_test_results_is_empty():
    assert get_speed_statistic([]) == [0, 0, 0], (
        "Function 'get_speed_statistic' should return [0, 0, 0] "
        "when test_results is empty"
    )


def test_single_element_list():
    assert get_speed_statistic([10]) == [10, 10, 10], (
        "Function 'get_speed_statistics' should return [10, 10, 10] "
        "when test_results is equal to [10]"
    )


def test_int_average():
    assert get_speed_statistic([10, 10, 11, 9, 12, 8]) == [8, 12, 10], (
        "Function 'get_speed_statistic' should return [8, 12, 10] "
        "when test_results is equal to [10, 10, 11, 9, 12, 8]"
    )


def test_float_average():
    assert get_speed_statistic([8, 9, 9, 9]) == [8, 9, 8], (
        "Function 'get_speed_statistic' should return [8, 9, 8] "
        "when test_results is equal to [8, 9, 9, 9] (average = (35) / 4 = 8.75; floor(average) = 8)"
    )


def test_float_max_when_test_results_contains_float_values():
    assert get_speed_statistic([4.5, 6.7, 9.2, 1]) == [1, 9.2, 5], (
        "Function 'get_speed_statistic' should return [1, 9.2, 5] "
        "when test_results is equal to [4.5, 6.7, 9.2, 1]"
    )
