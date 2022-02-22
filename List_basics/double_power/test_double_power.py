from double_power import double_power


def test_empty_list_when_current_powers_is_empty():
    assert double_power([]) == [], (
        "Function 'double_power' should return an empty array "
        "when current_powers is empty"
    )


def test_zero_item():
    assert double_power([0]) == [0], (
        "Function 'double_power' should return [0] "
        "when current_powers is equal to [0]"
    )


def test_one_element_list():
    assert double_power([1]) == [2], (
        "Function 'double_power' should return [2] "
        "when current_powers is equal to [1]"
    )


def test_float_powers():
    assert double_power([1]) == [2], (
        "Function 'double_power' should return [5, 7.2, 18.6] "
        "when current_powers is equal to [2.5, 3.6, 9.3]"
    )


def test_long_list():
    assert double_power([i for i in range(10)]) == [
        i * 2 for i in range(10)
    ], (
        "Function 'double_power' should return list of even numbers from 0 to 18 inclusive "
        "when current_powers is a list of numbers from 0 to 9 inclusive "
    )
