# Operacoes com arquivos e diretorios em Python:
#Algoritmo Op_ArqDir-Ex21.

import os

#Declarar variaveis globais:
nome: str = ''
nota1  : float = 0.0
nota2 : float = 0.0
nota3 : float = 0.0
nota4 : float = 0.0
valor_media : float = 0.0
situacao: str = ''
dir: str = ''
arq : str = ''
txt : str = ''

#Inicio

def main():

    #Declarar variaveis locais.
    cont : int = 1

    for cont in range(1, 6, 1):

        entrada()

    #Fim-para.
#FIM.
        

def entrada():

    #Declarar variaveis globais.
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media
    global situacao

    nome = input("Nome do aluno: ")
    nota1, nota2, nota3, nota4 = map(float, input("Notas separadas por virgula: ").split(','))

    valor_media = med(nota1, nota2, nota3, nota4)

    aprov(valor_media)

    print("Media: ", valor_media, situacao)

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media, situacao)

#Fim-segue.

def med(n1, n2, n3, n4):

    #Variavel local:
    media : float = 0.0

    media = (n1 + n2 + n3 + n4)/4

    return (media)
#Fim-segue.

def aprov(md):
    #Variavel global:
    global situacao

    if (md>=6):
        situacao = ' - Aprovado.'

    elif (md>=3):
        situacao = ' - Exame.'

    else:
        situacao = ' - Retido.'
    
    return (situacao)
    #Fim-se.
#FIm-segue.

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med, apr):
    # Variaveis globais
    global dir
    global arq

    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'

    #Variaveis locais
    linha : str = ''

    linha = ("Nome do aluno: "+ nm )+";"+(" N1 = "+str(nt1))+";"+(" N2 = "+str(nt2))+";"+(" N3 = "+str(nt3))+";"+(" N4 = "+str(nt4))+";"+(" Media = "+str(vlr_med))+(apr)+("\n")

    escreveArq(dir, arq, linha)

#Fim-segue.

def escreveArq(caminho, arquivo, linha_arq):
    #Variaveis grobais:
    global txt

    #Variaveis locais:
    file: str = ''
    tipo: str = ''
    enc: str = ''
    
    if not (os.path.exists(caminho)):
        #Criando o diretorio.
        os.mkdir(caminho)
        os.makedirs(caminho, exist_ok = True)
        os.chmod(caminho, 0o744) #Autorizacao de criacao, leitura e alteracao para o primeiro usuario, leitura para os demais.

    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        tipo = 'w'
        txt = caminho + arquivo
        enc = 'utf-8'

        if (os.path.exists(txt)): 
                tipo = 'a' 
       
        with open (txt, tipo, encoding=enc) as file:
            file.write(linha_arq)
    
    else:
        print("Diretorio invalido")
    
    #Fim-se.
#Fim-segue.

if __name__ == "__main__" :
    main()
#Fim-se.