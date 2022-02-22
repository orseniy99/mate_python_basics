from get_drinks_with_step import get_drinks_with_step


def test_22_when_number_of_guests_is_10_and_step_is_3():
    assert get_drinks_with_step(10, 3) == 22, (
        "Function 'get_drinks_with_step' should return 22 "
        "when number_of_guests is equal to 10 and step is equal to 3"
    )


def test_0_when_number_of_guests_is_0():
    assert get_drinks_with_step(0, 1) == 0, (
        "Function 'get_drinks_with_step' should return 0 "
        "when number_of_guests is equal to 0 and step is equal to 1"
    )


def test_5_when_number_of_guests_is_5_and_step_is_3():
    assert get_drinks_with_step(5, 3) == 5, (
        "Function 'get_drinks_with_step' should return 5 "
        "when number_of_guests is equal to 5 and step is equal to 3"
    )


def test_12_when_number_of_guests_is_18_and_step_is_10():
    assert get_drinks_with_step(18, 10) == 12, (
        "Function 'get_drinks_with_step' should return 12 "
        "when number_of_guests is equal to 18 and step is equal to 10"
    )


def test_2500_when_number_of_guests_is_100_and_step_is_2():
    assert get_drinks_with_step(100, 2) == 2500, (
        "Function 'get_drinks_with_step' should return 2500 "
        "when number_of_guests is equal to 100 and step is equal to 2"
    )
