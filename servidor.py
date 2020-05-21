# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:25:11 2020

@author: Letícia


Servidor: Ao receber o nome do arquivo, deverá verificar a existência do mesmo em uma pasta pré-configurada 
(a critério do desenvolvedor da aplicação) e enviar seu conteúdo de volta ao cliente que solicitou.

"""

# Servidor que recebe mensagens de uma aplicação cliente
import socket
   
host = ''
porta = 7000
endereco = (host, porta)

while(True):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(endereco)
    serv_socket.listen(5)
    print ('STATUS: Aguardando conexao')
    con, cliente = serv_socket.accept()     
    print ('STATUS: CONECTADO')
    print ('STATUS: Aguardando envio do nome do arquivo ...')
    recebe = con.recv(1024)
    nome_arquivo = ('c:\\temp2\\{}.txt' .format( recebe.decode('utf-8')))
    
    # verifica a existencia do arquivo 
    try:
        # abre arquivo
        arq = open (nome_arquivo, 'r',encoding='utf-8')
        dados = ''
        for linha in arq :
            dados = dados + linha
            
        #envia para o cliente o conteudo do arquivo
        con.sendto(dados.encode('utf-8'),cliente)  
        
        #fecha arquivo
        arq.close()
        
    except FileNotFoundError: con.sendto("Esse arquivo não existe!".encode('utf-8'),cliente)
    #fecha conexao
    serv_socket.close()


