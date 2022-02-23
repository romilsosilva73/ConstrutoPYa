# 1 - imports - bibliotecas

import pytest

import csv

import requests

teste_dados_novos_usuarios = [
    ('1', 'Juca', 'Pirama', 'juca@iterasys.com.br'),       #usuário 1
    ('2', 'Agatha', 'Christie', 'agatha@iterasys.com.br')  #usuário 2
]


teste_dados_usuarios_atuais = [
    ('1', 'George', 'Bluth', 'george.bluth@reqres.in'), #usuário 1
    ('2', 'Janet', 'Weaver', 'janet.weaver@reqres.in')  #usuário 2
]

# CRUD em aplicaçõe

#CREATE          - Post     Incluir / Publicar
#REACH/RESEARCH  - Get      Consultar / Pagar
# UPDATE         - Put      Atualizar
#DELETE          - Delete   Excluir

@pytest.mark.parametrize('id, nome, sobrenome, email', teste_dados_usuarios_atuais)

def testar_dados_usuarios(id, nome, sobrenome, email): # função que testa algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print(f'Id : {id_obtido} - Nome : {nome_obtido} - Sobre nome :  {sobrenome_obtido} - Email : {email_obtido}')

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except:
        print('Falta fazer')

    # 2 -  class - classe

# 3 - definitions - definições = métodos e funções

# main

#função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users