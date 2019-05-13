#! python3 

import json
import seguranca # nós criamos essa biblioteca
import lendo #essa aqui também!
import escrevendo #e mais uma :o
import ast
import tkinter
from tkinter import messagebox #usamos from pq queremos
from tkinter import simpledialog #uma coisa específica de tkinter
#messagebox e simpledialog são apenas para termos aquelas mensagens
#que aparecem em janelas distintas.

#Pegando o dicionário do arquivo 'senhasDB'
try:
    SenhasDict = lendo.ler()    
except FileNotFoundError:
    print("Senhas não encontradas! Criando novo banco de senhas")
    SenhasDict = {}

def atualizaList(Dicionario, listaBox): #atualiza a nossa visualização de senhas
    posicao = 0                         #temos uma variável para usar dentro do loop
    listaBox.delete(0,'end')            #deletamos todo o conteúdo da ListBox
    for i in Dicionario:                #iteramos sobre todos os elementos chave do dicionário
        listaBox.insert(posicao, i)     #em cada elemento, inserimos 
        posicao += 1


def copia():                                            #função que copia a senha do dicionário
    busca = caixaLista.get(caixaLista.curselection())   #aqui pegamos o que está selecionado na nossa ListBox
    senhaMaster = visorSM.get()                         #aqui pegamos o que foi escrito no nosso visor
    if busca in SenhasDict:                             #aqui testamos se há algum elemento no SenhasDict que corresponde à nossa busca
        print(seguranca.decode(senhaMaster, SenhasDict[busca])) #printamos se houver correspondência
        messagebox.showinfo("Information", "Senha para " + busca + " copiada.") #informamos com uma janela que a senha foi copiada.

def cadastra(): #função que cadastra a senha no dicionário
    nome = simpledialog.askstring("Cadastro de conta", "Insira o nome da conta.") #umas caixas pedindo uma string (askstring)
    senha = simpledialog.askstring("Cadastro de conta", "Insira a senha que deseja associar a essa conta") #mais uma string
    senhaMaster = simpledialog.askstring("Cadastro de conta", "Insira a senha mestre.") #mais uma string
    SenhasDict[nome] = seguranca.encode(senhaMaster, senha) #Insere no dicionário usando as 3 strings previamente fornecidas
    messagebox.showinfo("Information", "Senha cadastrada com sucesso.") #mensagem falando que deu certo
    escrevendo.escrever(SenhasDict) #aqui nós usamos escrever() para gravar o nosso dicionário em um arquivo .txt que servirá como base de dados
    atualizaList(SenhasDict, caixaLista) #atualizamos a nossa ListBox


    
#Fazemos a janela
janela = tkinter.Tk()

#Criamos os elementos da janela
visorSM = tkinter.Entry(janela)
btnCadastro = tkinter.Button(janela, text = 'Cadastrar', command = cadastra)
btnCopiar = tkinter.Button(janela, text = 'Copiar Senha', command = copia)
caixaLista = tkinter.Listbox(janela)
labelSM = tkinter.Label(janela, text = "Senha Mestre:")

#copiando os elementos do dicionário para a List Box
atualizaList(SenhasDict, caixaLista)


#configuramos os elementos
janela.geometry('200x200')

    
#Posicionamos os elementos
labelSM.pack()
visorSM.pack()
btnCadastro.pack()
btnCopiar.pack()
caixaLista.pack()

janela.mainloop()

        








