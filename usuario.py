# Press Shift+F10 to execute it or replace it with your code.

# 1 - imports - bibliotecas

import pytest

import csv

import requests
from requests import HTTPError

teste_dados_novos_usuarios = [
    (1, 'Juca', 'Pirama', 'juca@iterasys.com.br'),       #usuário 1
    (2, 'Agatha', 'Christie', 'agatha@iterasys.com.br')  #usuário 2
]


teste_dados_usuarios_atuais = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in', 'https://reqres.in/img/faces/1-image.jpg', 'https://reqres.in/#support-heading', 'To keep ReqRes free, contributions towards server costs are appreciated!'), #usuário 1
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in', 'https://reqres.in/img/faces/2-image.jpg', 'https://reqres.in/#support-heading', 'To keep ReqRes free, contributions towards server costs are appreciated!') #usuário 2
]

# CRUD em aplicações

#CREATE          - Post     Incluir / Publicar
#REACH/RESEARCH  - Get      Consultar / Pagar
# UPDATE         - Put      Atualizar
#DELETE          - Delete   Excluir

@pytest.mark.parametrize('id, nome, sobrenome, email, avatar, url, text', teste_dados_usuarios_atuais)

def testar_dados_usuarios(id, nome, sobrenome, email, avatar, url, text): # função que testa algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']
        avatar_obtido = jsonResponse['data']['avatar']
        url_obtido = jsonResponse['support']['url']
        text_obtido = jsonResponse['support']['text']

        #print(f'Id : {id_obtido} - Nome : {nome_obtido} - Sobre nome :  {sobrenome_obtido} - Email : {email_obtido} - Avatar : {avatar_obtido}  - URL : {url_obtido} - Texto : {text_obtido}')

        #print(f'Id : {id_obtido} - Nome : {nome_obtido} - Sobre nome :  {sobrenome_obtido} - Email : {email_obtido} - Avatar : {avatar_obtido}  - URL : {url_obtido} - Texto : {text_obtido}')

        print(f' \n Id : {id_obtido} \n  - Nome :  {nome_obtido} \n  - Sobre nome :  {sobrenome_obtido} \n  - Email :   {email_obtido} \n  - Avatar :    {avatar_obtido}  \n  - URL :   {url_obtido} \n - Texto :   {text_obtido} \n ')

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
        assert avatar_obtido == avatar
        assert url_obtido == url
        assert text_obtido == text

    except HTTPError as http_fail: # para o ISTQB, descobriu rodando é falha
        print(f'Ocorre um erro de HTTP : {http_fail}')
    except Exception as fail: # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada ocorreu : {fail}')

    # 2 -  class - classe

# 3 - definitions - definições = métodos e funções

# main

#função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users