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


# main

if __name__ == '__main__':
    # mensagem_boas_vindas
    print_hi('Romilso')

    # soma
    result = somar(30, 2)
    print(f'O resultado da soma é: {result}')

    # subtração
    result = subtrair(30, 2)
    print(f'O resultado da subtraçãoo é: {result}')

    # multiplicação
    result = multiplicar(30, 2)
    print(f'O resultado da multiplicação é: {result}')

    # divisão
    result = dividir(30, 0)
    print(f'O resultado da divisão é: {result}')

    # TESTES UNITÁRIOS

    # teste da função  'somar'


def test_somar_compacto_1():
    assert 8 == somar(5, 3)


def test_somar_compacto_2():
    assert somar(5, 3) == 8


def test_somar():
    # 1 - Configura/Prepara

    num1 = 10  # input
    num2 = 2  # input
    resultado_esperado = 12;  # output

    # 2 - Execut

    resultado_atual = somar(num1, num2)

    # 3 - Check

    assert resultado_atual == resultado_esperado


def test_subtrair():
    # 1 - Configura/Prepara

    num1 = 10  # input
    num2 = 2  # input
    resultado_esperado = 8;  # output

    # 2 - Execut

    resultado_atual = subtrair(num1, num2)

    # 3 - Check

    assert resultado_atual == resultado_esperado


def test_multiplicar():
    # 1 - Configura/Prepara

    num1 = 10  # input


num2 = 2  # input
resultado_esperado = 20;  # output

# 2 - Execut

resultado_atual = multiplicar(num1, num2)

# 3 - Check

assert resultado_atual == resultado_esperado


def test_dividir():
    1 - Configura / Prepara


num1 = 10  # input
num2 = 2  # input
resultado_esperado = 5;  # output

# 2 - Execut

resultado_atual = dividir(num1, num2)

# 3 - Check

assert resultado_atual == resultado_esperado


def test_dividir_com_zero():


# 1 - Configura/Prepara
num1 = 10  # input
num2 = 0  # input
resultado_esperado = 'Não divirás por zero';  # output

# 2 - Execut

resultado_atual = dividir(num1, num2)

# 3 - Check

assert resultado_atual == resultado_esperado

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
