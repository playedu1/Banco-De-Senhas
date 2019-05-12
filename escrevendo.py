import json


def escrever(Dicionario):
    with open('SenhasBD.txt', 'w') as arquivo:
        arquivo.write(json.dumps(Dicionario))




