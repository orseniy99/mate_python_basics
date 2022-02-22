from make_abbr import make_abbr


def test_nasa():
    assert make_abbr("national aeronautics space administration") == "NASA", (
        "Function 'make_abbr' should return 'NASA' when words is equal to "
        "'national aeronautics space administration'"
    )


def test_cpu():
    assert make_abbr("central processing unit") == "CPU", (
        "Function 'make_abbr' should return 'CPU' when words is equal to "
        "'central processing unit'"
    )


def test_smiles():
    assert (
        make_abbr("simplified molecular input line entry specification")
        == "SMILES"
    ), (
        "Function 'make_abbr' should return 'SMILES' when words is equal to "
        "'simplified molecular input line entry specification'"
    )


def test_ma_when_words_is_mate_academy():
    assert make_abbr("mate academy") == "MA", (
        "Function 'make_abbr' should return 'MA' when words is equal to "
        "'mate academy'"
    )


def test_empty_string_when_words_is_empty():
    assert make_abbr("") == "", (
        "Function 'make_abbr' should return an empty string "
        "when words is empty"
    )


def test_one_character():
    assert (
        make_abbr("a") == "A"
    ), "Function 'make_abbr' should return 'A' when words is equal to 'a'"
