from decrypt_message import decrypt_message


def test_long_message():
    assert (
        decrypt_message("!!!reeb gniknird ekil eW")
        == "We like drinking beer!!!"
    ), (
        "Function 'decrypt message' should return 'We like drinking beer!!!' "
        "when message is equal to '!!!reeb gniknird ekil eW'"
    )


def test_message_with_numbers():
    assert (
        decrypt_message("0202 ni eb lliw cimednap surivanoroc A")
        == "A coronavirus pandemic will be in 2020"
    ), (
        "Function 'decrypt message' should return 'A coronavirus pandemic will be in 2020' "
        "when message is equal to '0202 ni eb lliw cimednap surivanoroc A'"
    )


def test_mate_academy_message():
    assert decrypt_message("!ymedaca etaM evol I") == "I love Mate academy!", (
        "Function 'decrypt message' should return 'I love Mate academy!' "
        "when message is equal to '!ymadaca etaM evol I'"
    )
