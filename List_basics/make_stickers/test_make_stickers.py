from make_stickers import make_stickers


def test_body_list():
    assert make_stickers(3, "Body") == [
        "Body detail #1",
        "Body detail #2",
        "Body detail #3",
    ], (
        "Function 'make_stickers' should return ['Body detail #1', 'Body detail #2', 'Body detail #3'] "
        "when 'details_count' is equal to 3 and robot_part is equal to 'Body'"
    )


def test_head_list():
    assert make_stickers(4, "Head") == [
        "Head detail #1",
        "Head detail #2",
        "Head detail #3",
        "Head detail #4",
    ], (
        "Function 'make_stickers' should return "
        "['Head detail #1', 'Head detail #2', 'Head detail #3', 'Head detail #4'] "
        "when 'details_count' is equal to 4 and robot_part is equal to 'Head'"
    )


def test_empty_list_when_details_count_is_0():
    assert make_stickers(0, "Foot") == [], (
        "Function 'make_stickers' should return an empty list "
        "when 'details_count' is equal to 0"
    )


def test_long_list():
    hands_list = [f"Hand detail #{i}" for i in range(1, 11)]
    assert make_stickers(10, "Hand") == hands_list, (
        f"Function 'make_stickers' should return {hands_list} "
        "when 'details_count' is equal to 10 and robot_part is equal to 'Hand'"
    )
