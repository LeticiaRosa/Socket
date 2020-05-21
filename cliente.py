# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:29:33 2020

@author: Letícia

Cliente: deverá solicitar ao usuário o nome do arquivo texto (.txt) e posteriormente repassar ao servidor

"""

# Cliente que envia mensagem para aplicação servidor
import socket
ip = 'localhost'
porta = 7000
endereco = (ip,porta)

while(True):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(endereco)
    print ('STATUS: CONECTADO')
    nome_arq =  str(input("Informe o nome do arquivo .txt: "))
    #envia o nome do arquivo para o servidor
    client_socket.send(nome_arq.encode())
    
    #recebe o conteudo do arquivo
    recebe = client_socket.recv(1024)   
    #armazena os dados do arquivo na variavel dados
    dados = recebe.decode('utf-8')
    
    print(dados)
    arq = 'c:\\temp2\\'+ nome_arq + '(1).txt'
    arq2 = 'c:\\temp2\\'+ nome_arq + '.txt'
    #verifica a existencia do arquivo
    try:
        arq1 = open (arq2, 'r',encoding='utf-8')
        arq1.close()
    except FileNotFoundError: print("Informe um nome de arquivo válido")    
    except OSError: print ("ERRO!")
    else: 
        # cria e salva os dados em outro arquivo 
        arquivo = open(arq, 'w',encoding='utf-8')
        arquivo.write(dados)
        arquivo.close()
        print("Arquivo {}.txt criado!".format(nome_arq))
    #fecha conexao
    client_socket.close()