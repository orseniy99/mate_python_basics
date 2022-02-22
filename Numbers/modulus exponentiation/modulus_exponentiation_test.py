import modulus_exponentiation


def test_a_should_be_defined():
    assert (
            hasattr(modulus_exponentiation, "a") is True
    ), "Variable 'a' should be defined."


def test_a_should_be_an_integer():
    assert (
            isinstance(modulus_exponentiation.a, int) is True
    ), "Variable 'a' should be an integer."


def test_a_should_be_equal_to_7():
    assert modulus_exponentiation.a == 7, "Variable 'a' should be equal to 7."


def test_b_should_be_defined():
    assert (
            hasattr(modulus_exponentiation, "b") is True
    ), "Variable 'b' should be defined."


def test_b_should_be_an_integer():
    assert (
            isinstance(modulus_exponentiation.b, int) is True
    ), "Variable 'b' should be an integer."


def test_b_should_be_equal_to_2():
    assert modulus_exponentiation.b == 2, "Variable 'b' should be equal to 2."


def test_exp_should_be_defined():
    assert (
            hasattr(modulus_exponentiation, "exp") is True
    ), "Variable 'exp' should be defined."


def text_exp_should_be_an_integer():
    assert (
            isinstance(modulus_exponentiation.exp, int) is True
    ), "Variable 'exp' should be an integer."


def test_exp_should_be_equal_to_49():
    assert (
            modulus_exponentiation.exp == 49
    ), "Variable 'exp' should be equal to 49."


def test_mod_should_be_defined():
    assert (
            hasattr(modulus_exponentiation, "mod") is True
    ), "Variable 'mod' should be defined."


def test_mode_should_be_an_integer():
    assert (
            isinstance(modulus_exponentiation.mod, int) is True
    ), "Variable 'mod' should be an integer."


def test_mode_should_be_equal_to_1():
    assert (
            modulus_exponentiation.mod == 1
    ), "Variable 'mod' should be equal to 1."

