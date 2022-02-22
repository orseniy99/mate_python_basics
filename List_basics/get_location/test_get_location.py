from get_location import get_location


def test_same_coordinates_when_commands_is_empty_array():
    assert get_location([1, 1], []) == [
        1,
        1,
    ], "Function should return the same coordinates when list commands is empty"


def test_back():
    assert get_location([2, 3], ["back"]) == [
        2,
        2,
    ], "Function should return [2, 2] when coordinates are [2, 3] and command is 'back'"


def test_forward():
    assert get_location([0, 0], ["forward"]) == [
        0,
        1,
    ], "Function should return [0, 1] when coordinates are [0, 0] and command is 'forward'"


def test_left():
    assert get_location([3, 2], ["left"]) == [
        2,
        2,
    ], "Function should return [2, 2] when coordinates are [3, 2] and command is 'left'"


def test_right():
    assert get_location([1, 2], ["right"]) == [
        2,
        2,
    ], "Function should return [2, 2] when coordinates are [1, 2] and command is 'right'"


def test_5backs():
    assert get_location([0, 5], ["back", "back", "back", "back", "back"]) == [
        0,
        0,
    ], (
        "Function should return [0, 0] when coordinates are [0, 5] and "
        "commands are ['back', 'back', 'back', 'back', 'back']"
    )


def test_circle():
    assert get_location([0, 0], ["back", "left", "forward", "right"]) == [
        0,
        0,
    ], (
        "Function should return [0, 0] when coordinates are [0, 0] and "
        "commands are ['back', 'left', 'forward', 'right']"
    )


def test_long_list():
    assert (
        get_location(
            [10, 10],
            ["back", "back", "forward", "right", "right", "right", "left"],
        )
        == [12, 9]
    ), (
        "Function should return [9, 12] when coordinates are [10, 10] and "
        "commands are ['back', 'back', 'forward', 'right', 'right', 'right', 'left']"
    )
