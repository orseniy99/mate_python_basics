from scrolling_text import scrolling_text


def test_empty_list_when_string_is_empty():
    assert (
        scrolling_text("") == []
    ), "Function 'scrolling_text' should return an empty list when string is empty"


def test_one_upper_character_string():
    assert scrolling_text("A") == ["A"], (
        "Function 'scrolling_text' should return ['A'] "
        "when string is equal to 'A'"
    )


def test_one_lower_character_string():
    assert scrolling_text("a") == ["A"], (
        "Function 'scrolling_text' should return ['A'] "
        "when string is equal to 'a'"
    )


def test_string_with_same_letters():
    assert scrolling_text("aaa") == ["AAA", "AAA", "AAA"], (
        "Function 'scrolling_text' should return ['AAA', 'AAA', 'AAA'] "
        "when string is equal to 'aaa'"
    )


def test_short_string():
    assert scrolling_text("Abc") == ["ABC", "BCA", "CAB"], (
        "Function 'scrolling_text' should return ['ABC', 'BCA', 'CAB'] "
        "when string is equal to 'Abc'"
    )


def test_robot():
    assert scrolling_text("robot") == [
        "ROBOT",
        "OBOTR",
        "BOTRO",
        "OTROB",
        "TROBO",
    ], (
        "Function 'scrolling_text' should return ['ROBOT', 'OBOTR', 'BOTRO', 'OTROB', 'TROBO'] "
        "when string is equal to 'robot'"
    )


def test_string_with_spaces():
    assert scrolling_text("my word") == [
        "MY WORD",
        "Y WORDM",
        " WORDMY",
        "WORDMY ",
        "ORDMY W",
        "RDMY WO",
        "DMY WOR",
    ], (
        "Function 'scrolling_text' should return ['MY WORD', 'Y WORDM', ' WORDMY', 'WORDMY ',"
        " 'ORDMY W', 'RDMY WO', 'DMY WOR'] when string is equal to 'my word'"
    )


def test_string_with_numbers():
    assert scrolling_text("r90") == ["R90", "90R", "0R9"], (
        "Function 'scrolling_text' should return ['R90', '90R', '0R9'] "
        "when string is equal to 'r90'"
    )


def test_string_with_special_symbols():
    assert scrolling_text("?df%$") == [
        "?DF%$",
        "DF%$?",
        "F%$?D",
        "%$?DF",
        "$?DF%",
    ], (
        "Function 'scrolling_text' should return ['?DF%$', 'DF%$?', 'F%$?D', '%$?DF', '$?DF%'] "
        "when string is equal to '?df%$'"
    )
