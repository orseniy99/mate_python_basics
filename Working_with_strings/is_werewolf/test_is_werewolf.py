from is_werewolf import is_werewolf


def test_true_when_target_is_empty_string():
    assert is_werewolf("") is True, (
        "Function 'is_werewolf' should return True "
        "when target is an empty string"
    )


def test_true_when_target_is_a_single_character():
    assert is_werewolf("a") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'a'"
    )


def test_true_when_target_is_bb():
    assert is_werewolf("b") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'bb'"
    )


def test_true_when_target_is_a_palindrome_word():
    assert is_werewolf("rotator") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'rotator'"
    )


def test_true_when_target_is_a_palindrome_with_upper_letters():
    assert is_werewolf("Pop") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'Pop'"
    )


def test_true_when_target_is_a_palindrome_sentence():
    assert is_werewolf("red rum sir is murder") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'red rum sir is murder'"
    )


def test_false_when_target_is_home():
    assert is_werewolf("home") is False, (
        "Function 'is_werewolf' should return False "
        "when target is equal to 'home'"
    )


def test_false_when_target_is_mate_academy():
    assert is_werewolf("Mate Academy") is False, (
        "Function 'is_werewolf' should return False "
        "when target is equal to 'Mate Academy'"
    )


def test_true_when_target_is_palindrome_sentence_with_commas():
    assert is_werewolf("no lemon, no melon") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'no lemon, no melon'"
    )


def test_true_when_target_is_palindrome_sentence_with_question_mark():
    assert is_werewolf("Was it a rat I saw?") is True, (
        "Function 'is_werewolf' should return True "
        "when target is equal to 'Was it a rat I saw?'"
    )
