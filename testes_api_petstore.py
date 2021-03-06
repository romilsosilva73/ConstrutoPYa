# Press Shift+F10 to execute it or replace it with your code.

# TESTE DE API

# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste: API Pet Store


# 1 - imports - bibliotecas

import pytest

import csv

import requests
from requests import HTTPError

import _json

import pytest

url = 'https://petstore.swagger.io/v2/user'


# 2 -  class - classe


# 3 - definitions - definições = métodos e funções

#### post

def testar_incluir_usuario():
    # configura

    status_code_esperado = 200  # comunicação
    code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '1001'  # id do usuário

    # executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.post(url=url,
                             data=open('json/usuario1.json', 'rb'),
                             headers=headers
                             )
    json_body = resposta.json()

    # print(resposta) # status code 200
    print(resposta.status_code)  # status code 200
    print(resposta.json())  # responde body

    # valida

    assert resposta.status_code == status_code_esperado
    assert json_body['code'] == code_esperado
    assert json_body['type'] == type_esperado
    assert json_body['message'] == mensagem_esperada

    print(
        '\n TESTE 1  - Dados esperados : \n - status code (comunication): {}  \n - code (functional): {}  \n - type:   {} \n - message (id):  {} \n '.format(
            status_code_esperado, code_esperado, type_esperado, mensagem_esperada))

    print(
        '\n TESTE 2 - body  - Dados obtidos API : \n - status code (comunication): {}  \n - code (functional):: {}  \n - type:   {} \n - message (id) :  {} \n '.format(
            resposta.status_code, json_body['code'], json_body['type'], json_body['message']))


#### get

def testar_consultar_usuario():
    # Configura

    username = "T_user_name"

    id_esperado = 1001
    username_esperado = 'T_user_name_test'
    firstName_esperado = 'T_first_name'
    lastName_esperado = 'T_last_name'
    email_esperado = 'T_email'
    password_esperado = 'T_password'
    phone_esperado = 'T_phone'
    userStatus_esperado = 1
    status_code_esperado = 200  # comunication
    # status_code_esperado = 404 #comunication

    #### #Executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.get('https://petstore.swagger.io/v2/user/T_user_name_test', headers=headers)
    json_body = resposta.json()

    print(resposta)  # status code 200
    print(resposta.status_code)  # status code 200
    print(resposta.json())  # responde body

    # valida

    assert resposta.status_code == status_code_esperado

    assert json_body['id'] == int(id_esperado)
    assert json_body['username'] == username_esperado
    assert json_body['firstName'] == firstName_esperado
    assert json_body['lastName'] == lastName_esperado
    assert json_body['email'] == email_esperado
    assert json_body['password'] == password_esperado
    assert json_body['phone'] == phone_esperado
    assert json_body['userStatus'] == userStatus_esperado

    status_code_esperado = 200  # comunication
    # status_code_esperado = 404  # comunication #DEFEITO 404 IDENTIFICADO NA API


#### put

def testar_modificar_usuario():
    # configura

    status_code_esperado = 200  # comunicação
    code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '10012'  # id do usuário

    # executa

    headers = {'Content-Type': 'application/json'}

    # executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.put(url='https://petstore.swagger.io/v2/user/T_user_name_test',
                            data=open('json/usuario2.json', 'rb'),
                            headers=headers
                            )
    json_body = resposta.json()

    # print(resposta) # status code 200
    print(resposta.status_code)  # status code 200
    print(resposta.json())  # responde body

    # valida

    assert resposta.status_code == status_code_esperado
    assert json_body['code'] == code_esperado
    assert json_body['type'] == type_esperado
    assert json_body['message'] == mensagem_esperada

    print(
        '\n TESTE 1  - Dados esperados : \n - status code (comunication): {}  \n - code (functional): {}  \n - type:   {} \n - message (id):  {} \n '.format(
            status_code_esperado, code_esperado, type_esperado, mensagem_esperada))

    print(
        '\n TESTE 2 - body  - Dados obtidos API : \n - status code (comunication): {}  \n - code (functional):: {}  \n - type:   {} \n - message (id) :  {} \n '.format(
            resposta.status_code, json_body['code'], json_body['type'], json_body['message']))

# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users
