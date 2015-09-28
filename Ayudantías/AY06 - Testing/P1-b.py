__author__ = 'patricio_lopez'
# -*- coding: utf-8 -*-


def parentesis_balanceados(string):
    """
    Verifica que solo tenga paréntesis que se cierren.
    """
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0


def pytest_generate_tests(metafunc):
    if 'valid_input' in metafunc.fixturenames:
        inputs_validos = [
            "g(x) = ((2^x)+5*(42/f(x)))",
            "4+5",
            ""
        ]
        metafunc.parametrize("valid_input", inputs_validos)
    elif 'invalid_input' in metafunc.fixturenames:
        inputs_invalidos = [
            "(2^(2^(2)) * 4",
            "(2+4))((6%3)",
        ]
        metafunc.parametrize("invalid_input", inputs_invalidos)


def test_parentesis_validos(valid_input):
    assert parentesis_balanceados(valid_input)


def test_parentesis_invalidos(invalid_input):
    assert not parentesis_balanceados(invalid_input)
