import ast

def ler():
    with open('SenhasBD.txt') as arquivo: #abrimos 'SenhasBD' e apelidamos como arquivo
        texto = arquivo.read()
        return ast.literal_eval(texto)




