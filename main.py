# Press Shift+F10 to execute it or replace it with your code.

# 1 - imports - bibliotecas

import pytest

# 2 -  class - classe


# 3 - definitions - definições = métodos e funções

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Oi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Não divirás por zero'


#main
# TEST
if __name__ == '__main__':

    #mensagem_boas_vindas
    print_hi('Romilso')

    #soma
    result = somar(30, 2)
    print(f'O resultado da soma é: {result}')

    #subtração
    result =  subtrair(30, 2)
    print(f'O resultado da subtraçãoo é: {result}')

    #multiplicação
    result = multiplicar(30, 2)
    print(f'O resultado da multiplicação é: {result}')

    # divisão
    result = dividir(30, 0)
    print(f'O resultado da divisão é: {result}')

    #TESTES UNITÁRIOS

    #teste da função 'somar'

    # Testes utilizando classes @pytest.mark.parametrize

# Testes utilizando métodos 'def'

def test_somar_compacto_1():
    assert 12 == somar(10, 2)


def test_somar_didatico():
        # 1 - Configura/Prepara

        num1 = 10  # input
        num2 = 2  # input
        resultado_esperado = 12;  # output

        # 2 - Execut

        resultado_atual = somar(num1, num2)

        # 3 - Check

        assert resultado_atual == resultado_esperado


def test_subtrair_compacto():
    assert subtrair(10, 2) == 8

def test_subtrair_didatico():

    # 1 - Configura/Prepara

    num1 = 10  # input
    num2 = 2  # input
    resultado_esperado = 8;  # output

    # 2 - Execut

    resultado_atual = subtrair(num1, num2)

    # 3 - Check

    assert resultado_atual == resultado_esperado


def test_multiplicar_compacto():
        assert multiplicar(10, 2) == 20

def test_multiplicar_didatico():
    # 1 - Configura/Prepara

    num1 = 10  # input
    num2 = 2  # input
    resultado_esperado = 20; # output

    # 2 - Execut

    resultado_atual = multiplicar(num1, num2)

    # 3 - Check

    assert resultado_atual == resultado_esperado

    def test_dividir_compacto():
        assert dividir(10, 2) == 5

def test_dividir_didatico():
    # 1 - Configura/Prepara

    num1 = 10  # input
    num2 = 2  # input
    resultado_esperado = 5;  # output

    # 2 - Execut

    resultado_atual = dividir(num1, num2)

    # 3 - Check

    assert resultado_atual == resultado_esperado

def test_dividir_com_zero_compacto():
        assert dividir(10, 0) == 'Não divirás por zero'

def test_dividir_com_zero_didatico():
    # 1 - Configura/Prepara

    num1 = 10  # input
    num2 = 0  # input
    resultado_esperado = 'Não divirás por zero' ;  # output

    # 2 - Execut

    resultado_atual = dividir(num1, num2)

    # 3 - Check

    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('num1, num2, result', [
        # valores
        (10, 2, 12),  # test 1
        (10, -2, 8),  # test 2
        (-10, 2, -8),  # test 3
        (-10, -10, -20),  # test 4
        (0, -2, -2),  # test 5
        (-10, 0, -10),  # test 6
        (0, 0, 0),  # test 7
])


def test_somar_compacto_classe_pytest_mark_parametrize(num1, num2, result):
    assert somar(num1, num2) == result


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


