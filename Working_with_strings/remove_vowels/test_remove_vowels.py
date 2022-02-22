from remove_vowels import remove_vowels


def test_single_world():
    assert remove_vowels("document") == "dcmnt", (
        "Function 'remove_vowels' should return 'dcmt' "
        "when input is equal to 'document'"
    )


def test_sentence():
    assert remove_vowels("I like my boss") == " lk m bss", (
        "Function 'remove_vowels' should return ' lk m bss' "
        "when input is equal to 'I like my boss'"
    )


def test_string_with_numbers():
    assert remove_vowels("350 euro") == "350 r", (
        "Function 'remove_vowels' should return '350 r' "
        "when input is equal to '350 euro'"
    )


def test_empty_string():
    assert remove_vowels("") == "", (
        "Function 'remove_vowels' should return an empty string "
        "when input is an empty string"
    )


def test_string_without_vowels():
    assert remove_vowels("ttrtrrt") == "ttrtrrt", (
        "Function 'remove_vowels' should return the same string "
        "when input doesn't contain vowels"
    )


def test_string_contains_only_vowels():
    assert remove_vowels("aAaaaUuuiuiu") == "", (
        "Function 'remove_vowels' should return an empty string "
        "when input contains only vowels"
    )
