from is_sorted import is_sorted


def test_true_when_box_numbers_is_12345():
    assert (
        is_sorted([1, 2, 3, 4, 5]) is True
    ), "Function 'is_sorted' should return True when box_numbers is equal to [1, 2, 3, 4, 5]"


def test_sorted_with_equal_elements():
    assert (
        is_sorted([0, 1, 1, 1, 2]) is True
    ), "Function 'is_sorted' should return True when box_numbers is equal to [0, 1, 1, 1, 2]"


def test_true_when_list_contains_only_one_element():
    assert (
        is_sorted([5]) is True
    ), "Function 'is_sorted' should return True when box_numbers is equal to [5]"


def test_true_when_box_numbers_is_empty():
    assert (
        is_sorted([]) is True
    ), "Function 'is_sorted' should return True when box_numbers is empty"


def test_false_when_box_numbers_is_42():
    assert (
        is_sorted([4, 2]) is False
    ), "Function 'is_sorted' should return False when box_numbers is equal to [4, 2]"


def test_non_sorted():
    assert is_sorted([1, 2, 3, 2, 4]) is False, (
        "Function 'is_sorted' should return False "
        "when box_numbers is equal to [1, 2, 3, 2, 4]"
    )


def test_long_non_sorted():
    assert is_sorted([1, 2, 3, 4, 10, 123, 122, 123, 123, 190]) is False, (
        "Function 'is_sorted' should return False "
        "when box_numbers is equal to [1, 2, 3, 4, 10, 123, 122, 123, 123, 190]"
    )
